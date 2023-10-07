from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Comment
from .forms import CommentForm
from posts.models import Post

# Handles the POST request for the post detail page(PostDetailView)
class PostComment(LoginRequiredMixin, SingleObjectMixin, FormView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Post
    form_class = CommentForm
    template_name = 'post_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = self.object
        comment.save()

        return super().form_valid(form)
    def get_success_url(self):
        post = self.get_object()

        return reverse('post_detail', kwargs={'pk':post.pk}) + '#comments'


