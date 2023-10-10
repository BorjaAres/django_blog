from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from user.views import UserLoginView, UserLogoutView, UserRegistrationView
from posts.views import PostCreateView, BlogHomeView, AllPostsView, PostDetailView
from utilities.views import IndexView, ContactView, AboutUsView
from posts.models import Post

User = get_user_model()

class StatusCodeTests(TestCase):
    """
    Test case for checking status codes.
    """

    def test_index_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact_status_code(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_us_status_code(self):
        url = reverse('about_us')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_home_status_code(self):
        url = reverse('blog_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_all_posts_status_code(self):
        url = reverse('all_posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail_status_code(self):
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
        )

        post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=user,
        )

        url = reverse('post_detail', args={post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_create_status_code_unauthorized_user(self):
        url = reverse('post_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_post_create_status_code_authorized_user(self):
        self.user = User.objects.create_superuser(
            username='testuser', email='testadmin@example.com', password='testpassword')
        self.client.login(email='testadmin@example.com', password='testpassword')

        url = reverse('post_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_status_code(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_logout_status_code(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_register_status_code(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class ViewResolutionTests(SimpleTestCase):
    """
    Test case for checking view resolution.
    """

    def test_index_view_resolution(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_contact_view_resolution(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func.view_class, ContactView)

    def test_about_us_view_resolution(self):
        url = reverse('about_us')
        self.assertEqual(resolve(url).func.view_class, AboutUsView)

    def test_blog_home_view_resolution(self):
        url = reverse('blog_home')
        self.assertEqual(resolve(url).func.view_class, BlogHomeView)

    def test_all_posts_view_resolution(self):
        url = reverse('all_posts')
        self.assertEqual(resolve(url).func.view_class, AllPostsView)

    def test_post_detail_view_resolution(self):
        url = reverse('post_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_post_create_view_resolution(self):
        url = reverse('post_create')
        self.assertEqual(resolve(url).func.view_class, PostCreateView)

    def test_login_view_resolution(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, UserLoginView)

    def test_logout_view_resolution(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, UserLogoutView)

    def test_register_view_resolution(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, UserRegistrationView)

class URLPatternTests(TestCase):
    """
    Test case for the URLs in the user application.
    """

    def test_index_url_pattern(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_contact_url_pattern(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_about_us_url_pattern(self):
        response = self.client.get('/about_us/')
        self.assertEqual(response.status_code, 200)

    def test_blog_home_url_pattern(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_all_posts_url_pattern(self):
        response = self.client.get('/posts/all_posts/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_pattern(self):
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
        )

        post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=user,
        )

        response = self.client.get(f'/posts/{post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_create_url_pattern_unauthorized_user(self):
        response = self.client.get('/posts/post/new/')
        self.assertEqual(response.status_code, 403)

    def test_post_create_url_pattern_authorized_user(self):
        self.user = User.objects.create_superuser(
            username='testuser', email='testadmin@example.com', password='testpassword')

        self.client.login(email='testadmin@example.com', password='testpassword')

        response = self.client.get('/posts/post/new/')
        self.assertEqual(response.status_code, 200)

    def test_login_url_pattern(self):
        response = self.client.get('/user/login/')
        self.assertEqual(response.status_code, 200)

    def test_logout_url_pattern(self):
        response = self.client.get('/user/logout/')
        self.assertEqual(response.status_code, 302)

    def test_register_url_pattern(self):
        response = self.client.get('/user/register/')
        self.assertEqual(response.status_code, 200)

