from django.urls import reverse, resolve
from django.test import TestCase
from .views import BlogHomeView, PostDetailView, AllPostsView, PostCreateView
from user.views import UserLoginView, UserLogoutView, UserRegistrationView
from .models import Post
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase

User = get_user_model()

class URLTests(TestCase):
    def test_blog_home_url(self):
        """
        Test the blog home URL.
        The response status code should be 200 (OK).
        The correct view function should be used.
        """
        url = reverse('blog_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__, BlogHomeView.as_view().__name__)

    def test_post_detail_url(self):
        """
        Test the post detail URL with a valid post id.
        The response status code should be 200 (OK).
        The correct view function should be used.
        """
        self.user = User.objects.create_superuser('testuser', 'test@example.com', 'testpassword')
        self.client.login(email='test@example.com', password='testpassword')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

        url = reverse('post_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__, PostCreateView.as_view().__name__)

    def test_all_posts_url(self):
        """
        Test the all posts URL.
        The response status code should be 200 (OK).
        The correct view function should be used.
        """
        url = reverse('all_posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__, AllPostsView.as_view().__name__)

    def test_post_create_url(self):
        """
        Test the post create URL.
        The response status code should be 200 (OK).
        The correct view function should be used.
        """
        self.user = User.objects.create_superuser('testuser', 'test@example.com', 'testpassword')
        self.client.login(email='test@example.com', password='testpassword')

        url = reverse('post_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__, PostCreateView.as_view().__name__)

    def test_login_url(self):
        """
        Test the login URL.
        The response status code should be 200 (OK).
        The correct view function should be used.
        """
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__, UserLoginView.as_view().__name__)

    def test_logout_url(self):
         """
         Test the logout URL.
         The response status code should be 302 (Found), as we expect a redirect after logout.
         The correct view function should be used.
         """
         url = reverse('logout')
         response = self.client.get(url)
         self.assertEqual(response.status_code, 302)
         self.assertEqual(response.resolver_match.func.__name__, UserLogoutView.as_view().__name__)

    def test_register_url(self):
         """
         Test the register URL.
         The response status code should be 200 (OK).
         The correct view function should be used.
         """
         url = reverse('register')
         response = self.client.get(url)
         self.assertEqual(response.status_code, 200)
         self.assertEqual(response.resolver_match.func.__name__, UserRegistrationView.as_view().__name__)

class CheckURLSettingsTests(SimpleTestCase):
    """
    Test case for checking that URLs resolve to the correct views.
    """

    def test_blog_home_url_resolves(self):
        """
        Test that the URL for the blog home view resolves to the correct view.
        """
        url = reverse('blog_home')
        self.assertEqual(resolve(url).func.view_class, BlogHomeView)

    def test_post_detail_url_resolves(self):
        """
        Test that the URL for the post detail view resolves to the correct view.
        """
        url = reverse('post_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_all_posts_url_resolves(self):
        """
        Test that the URL for the all posts view resolves to the correct view.
        """
        url = reverse('all_posts')
        self.assertEqual(resolve(url).func.view_class, AllPostsView)

    def test_post_create_url_resolves(self):
        """
        Test that the URL for the post create view resolves to the correct view.
        """
        url = reverse('post_create')
        self.assertEqual(resolve(url).func.view_class, PostCreateView)

    def test_login_url_resolves(self):
        """
        Test that the URL for the login view resolves to the correct view.
        """
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, UserLoginView)

    def test_logout_url_resolves(self):
         """
         Test that the URL for the logout view resolves to the correct view.
         """
         url = reverse('logout')
         self.assertEqual(resolve(url).func.view_class, UserLogoutView)

    def test_register_url_resolves(self):
         """
         Test that the URL for the register view resolves to the correct view.
         """
         url = reverse('register')
         self.assertEqual(resolve(url).func.view_class, UserRegistrationView)

class CheckUrlConfigTests(SimpleTestCase):
    """
    Test case for checking that URLs resolve to the correct views.
    """

    def test_blog_home_url_resolves(self):
        """
        Test that the URL for the blog home view resolves to the correct view.
        """
        url = reverse('blog_home')
        self.assertEqual(resolve(url).func.view_class, BlogHomeView)

    def test_post_detail_url_resolves(self):
        """
        Test that the URL for the post detail view resolves to the correct view.
        """
        url = reverse('post_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_all_posts_url_resolves(self):
        """
        Test that the URL for the all posts view resolves to the correct view.
        """
        url = reverse('all_posts')
        self.assertEqual(resolve(url).func.view_class, AllPostsView)

    def test_post_create_url_resolves(self):
        """
        Test that the URL for the post create view resolves to the correct view.
        """
        url = reverse('post_create')
        self.assertEqual(resolve(url).func.view_class, PostCreateView)

    def test_login_url_resolves(self):
        """
        Test that the URL for the login view resolves to the correct view.
        """
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, UserLoginView)

    def test_logout_url_resolves(self):
         """
         Test that the URL for the logout view resolves to the correct view.
         """
         url = reverse('logout')
         self.assertEqual(resolve(url).func.view_class, UserLogoutView)

    def test_register_url_resolves(self):
         """
         Test that the URL for the register view resolves to the correct view.
         """
         url = reverse('register')
         self.assertEqual(resolve(url).func.view_class, UserRegistrationView)



