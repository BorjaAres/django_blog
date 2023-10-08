from django.urls import path
from . import views as utilities_views
from posts import views as posts_views
from user import views as user_views

urlpatterns = [
    path('', utilities_views.IndexView.as_view(), name='index'),
    path('contact/', utilities_views.ContactView.as_view(), name='contact'),
    path('about_us/', utilities_views.AboutUsView.as_view(), name='about_us'),
    path('posts/', posts_views.BlogHomeView.as_view(), name='blog_home'),
    path('posts/all_posts/', posts_views.AllPostsView.as_view(), name='all_posts'),
    path('posts/<int:pk>/', posts_views.PostDetailView.as_view(), name='post_detail'),
    path('posts/post/new/', posts_views.PostCreateView.as_view(), name='post_create'),
    path('login/',user_views.UserLoginView.as_view(), name='login'),
]
