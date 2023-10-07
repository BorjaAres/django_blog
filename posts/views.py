from django.views.generic import ListView, DetailView, View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Post
from comments import views as comments_views
from comments.forms import CommentForm


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog_home.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-date']

class AllPostsView(ListView):
    model = Post
    template_name = 'all_posts.html'
    context_object_name = 'posts'
    # ordering = ['-date']

# Combine PostDisplay and PostComment into one view
class PostDetailView(View, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = comments_views.PostComment.as_view()
        return view(request, *args, **kwargs)

# Handles the GET request for the post detail page
class PostDisplay(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content', 'image',]  # Customize the fields as needed

    def dispatch(self, request, *args, **kwargs):
        # Check if the user is a superuser or staff member
        if not (self.request.user.is_superuser or self.request.user.is_staff):
            # If not, redirect to a permission denied page or raise a 403 Forbidden error
            return HttpResponseForbidden("Permission Denied")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Set the post's author to the current user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the detail view of the newly created post
        return reverse('post_detail', kwargs={'pk': self.object.pk})

# Handles the POST request for the post detail page


