from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from utilities import views as utilities_views
from posts import views as posts_views
from comments import views as comments_views
from user import views as user_views

path('posts/<int:pk>/', posts_views.PostDetailView.as_view(), name='post_detail'),