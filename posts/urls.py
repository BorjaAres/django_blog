from django.urls import path
from user import views as user_views
from . import views

urlpatterns = [
    path('posts/', views.BlogHomeView.as_view(), name='blog_home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/all_posts/', views.AllPostsView.as_view(), name='all_posts'),
    path('posts/post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/search_results/', views.search_results, name='search_results'),
]