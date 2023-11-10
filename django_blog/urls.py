from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from utilities import views as utilities_views
from posts import views as posts_views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', utilities_views.IndexView.as_view(), name='index'),
    path('contact/', utilities_views.ContactView.as_view(), name='contact'),
    path('about_us/', utilities_views.AboutUsView.as_view(), name='about_us'),
    path('posts/', posts_views.BlogHomeView.as_view(), name='blog_home'),
    path('posts/all_posts/', posts_views.AllPostsView.as_view(), name='all_posts'),
    path('posts/<int:pk>/', posts_views.PostDetailView.as_view(), name='post_detail'),
    path('posts/post/new/', posts_views.PostCreateView.as_view(), name='post_create'),
    path('posts/search_results/', posts_views.search_results, name='search_results'),
    path('user/login/', user_views.UserLoginView.as_view(), name='login'),
    path('user/logout/', user_views.UserLogoutView.as_view(), name='logout'),
    path('user/register/', user_views.UserRegistrationView.as_view(), name='register'),
]

# when DEBUG is True, this code adds URL patterns that enable Django to serve media files directly during development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)