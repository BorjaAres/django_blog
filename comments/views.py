from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import CommentForm
from .models import Post, Comment
from django.views.generic.edit import UpdateView, DeleteView


# Handles the POST request for the post detail page(PostDetailView)
class PostComment(LoginRequiredMixin, SingleObjectMixin, FormView):
    login_url = '/login/'  # URL where users are redirected if not logged in
    redirect_field_name = 'redirect_to'  # Name of the query parameter carrying the redirect URL
    model = Post  # The model associated with this view
    form_class = CommentForm  # The form used for posting comments
    template_name = 'post_detail.html'  # The template to render the view

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Get the Post object associated with the comment
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request  # Pass the request object to the form
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)  # Save the comment but don't commit it to the database yet
        comment.user = self.request.user  # Set the user of the comment to the currently logged-in user
        comment.post = self.object  # Set the associated Post for the comment
        comment.save()  # Save the comment with the user and post information

        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()  # Get the associated Post object

        # Redirect to the post detail page with the post's primary key and add #comments to scroll to the comment section
        return reverse('post_detail', kwargs={'pk': post.pk}) + '#comments'


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'comment_form.html'
    fields = ['text']

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
