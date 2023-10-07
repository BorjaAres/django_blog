from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from posts.models import Post

class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'latest_posts'
    queryset = Post.objects.order_by('-date')[:4]

class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutUsView(TemplateView):
    template_name = 'about_us.html'


