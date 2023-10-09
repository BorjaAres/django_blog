from django.urls import path
from . import views
from posts import views as posts_views


urlpatterns = [
    path('user/login/', views.UserLoginView.as_view(), name='login'),
    path('user/logout/', views.UserLogoutView.as_view(), name='logout'),
    path('user/register/', views.UserRegistrationView.as_view(), name='register'),
]
