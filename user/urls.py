from django.urls import path
from . import views
from posts import views as posts_views


urlpatterns = [
    path('user/login/', UserLoginView.as_view(), name='login'),
    path('user/logout/', UserLogoutView.as_view(), name='logout'),
    path('user/register/', UserRegistrationView.as_view(), name='register'),
    path('posts/post/new/', posts_views.PostCreateView.as_view(), name='post_create'),
]
