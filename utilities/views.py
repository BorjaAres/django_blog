from django.views.generic import ListView, DetailView, TemplateView, View
from posts.models import Post
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from .models import ContactMessage


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'latest_posts'
    queryset = Post.objects.order_by('-date')[:4]


class ContactView(View):
    template_name = 'contact.html'  # Specify your template name here

    def get(self, request):
        # Handle GET request
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Handle POST request
        form = ContactForm(request.POST)
        if form.is_valid():
            # If the user is logged in, use their username and email
            if request.user.is_authenticated:
                name = request.user.username
                email = request.user.email
            else:
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Save the user's message to the database
            contact_message = ContactMessage(name=name, email=email, message=message)
            contact_message.save()

            send_mail(
                'Contact Form Submission',
                f'Message from {name}: {message}',
                'email',
                ['your_email@example.com'],
                fail_silently=False,
            )

        return render(request, self.template_name, {'form': form})


class AboutUsView(TemplateView):
    template_name = 'about_us.html'
