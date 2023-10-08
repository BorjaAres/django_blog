from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from user.views import UserLoginView, UserLogoutView, UserRegistrationView
from posts.views import PostCreateView, BlogHomeView, AllPostsView, PostDetailView
from utilities.views import IndexView, ContactView, AboutUsView
from posts.models import Post

User = get_user_model()

class URLTests(TestCase):

    def test_index_url(self):
        """
        Test the index URL.
        The response status code should be 200 (OK).
        The correct view function should be used.
        """
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.view_class, IndexView)

    def test_contact_url(self):
         """
         Test the contact URL.
         The response status code should be 200 (OK).
         The correct view function should be used.
         """
         url = reverse('contact')
         response = self.client.get(url)
         self.assertEqual(response.status_code, 200)
         self.assertEqual(response.resolver_match.func.view_class, ContactView)

    def test_about_us_url(self):
         """
         Test the about us URL.
         The response status code should be 200 (OK).
         The correct view function should be used.
         """
         url = reverse('about_us')
         response = self.client.get(url)
         self.assertEqual(response.status_code, 200)
         self.assertEqual(response.resolver_match.func.view_class, AboutUsView)

    def test_blog_home_url(self):
        """
        Test the blog home URL.
        The response status code should be 200 (OK).
        The correct view function should be used.
        """
        url = reverse('blog_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.view_class, BlogHomeView)

    def test_all_posts_url(self):
        """
        Test the all posts URL.
        The response status code should be 200 (OK).
        The correct view function should be used.
        """
        url = reverse('all_posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.view_class, AllPostsView)

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
        self.assertEqual(response.resolver_match.func.view_class, PostCreateView)

    def test_login_url(self):
        """
        Test the login URL.
        The response status code should be 200 (OK).
        The correct view function should be used.
        """
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.view_class, UserLoginView)


class CheckURLSettingsTests(SimpleTestCase):
    """
    Test case for checking that URLs resolve to the correct views.
    """

    def test_index_url_resolves(self):
        """
        Test that the URL for the index view resolves to the correct view.
        """
        url = reverse('index')
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_contact_url_resolves(self):
         """
         Test that the URL for the contact view resolves to the correct view.
         """
         url = reverse('contact')
         self.assertEqual(resolve(url).func.view_class, ContactView)

    def test_about_us_url_resolves(self):
         """
         Test that the URL for the about us view resolves to the correct view.
         """
         url = reverse('about_us')
         self.assertEqual(resolve(url).func.view_class, AboutUsView)

    def test_blog_home_url_resolves(self):
        """
        Test that the URL for the blog home view resolves to the correct view.
        """
        url = reverse('blog_home')
        self.assertEqual(resolve(url).func.view_class, BlogHomeView)

    def test_all_posts_url_resolves(self):
       """
       Test that the URL for all posts view resolves to the correct view.
       """
       url = reverse('all_posts')
       self.assertEqual(resolve(url).func.view_class, AllPostsView)

    def test_post_detail_url_resolves(self):
       """
       Test that the URL for post detail view resolves to the correct view.
       """
       url = reverse('post_detail', args=[1])
       # Here we assume that a post with id=1 exists in the test database
       # If not, this will return a NoReverseMatch error
       self.assertEqual(resolve(url).func.view_class, PostDetailView)

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

class CheckUrlConfigTests(SimpleTestCase):
    """
    Test case for checking that URLs resolve to the correct views.
    """

    def test_index_url_resolves(self):
        """
        Test that the URL for the index view resolves to the correct view.
        """
        url = reverse('index')
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_contact_url_resolves(self):
         """
         Test that the URL for the contact view resolves to the correct view.
         """
         url = reverse('contact')
         self.assertEqual(resolve(url).func.view_class, ContactView)

    def test_about_us_url_resolves(self):
         """
         Test that the URL for the about us view resolves to the correct view.
         """
         url = reverse('about_us')
         self.assertEqual(resolve(url).func.view_class, AboutUsView)

    def test_blog_home_url_resolves(self):
        """
        Test that the URL for the blog home view resolves to the correct view.
        """
        url = reverse('blog_home')
        self.assertEqual(resolve(url).func.view_class, BlogHomeView)

    def test_all_posts_url_resolves(self):
       """
       Test that the URL for all posts view resolves to the correct view.
       """
       url = reverse('all_posts')
       self.assertEqual(resolve(url).func.view_class, AllPostsView)

    def test_post_detail_url_resolves(self):
         """
         Test that the URL for post detail view resolves to the correct view.
         """
         url = reverse('post_detail', args=[1])
         # Here we assume that a post with id=1 exists in the test database
         # If not, this will return a NoReverseMatch error
         self.assertEqual(resolve(url).func.view_class, PostDetailView)

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


class CheckUrlPatternsTests(TestCase):
    """
    Test case for checking that URL patterns are correct.
    """

    def test_index_url_pattern(self):
        """
        Test that the index URL pattern is correct.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_contact_url_pattern(self):
        """
        Test that the contact URL pattern is correct.
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_about_us_url_pattern(self):
        """
        Test that the about us URL pattern is correct.
        """
        response = self.client.get('/about_us/')
        self.assertEqual(response.status_code, 200)

    def test_blog_home_url_pattern(self):
        """
        Test that the blog home URL pattern is correct.
        """
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_all_posts_url_pattern(self):
        """
        Test that the all posts URL pattern is correct.
        """
        response = self.client.get('/posts/all_posts/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_pattern(self):
        """
        Test that the post detail URL pattern is correct.
        """
        self.user = User.objects.create_superuser('testuser', 'test@example.com', 'testpassword')
        self.client.login(email='test@example.com', password='testpassword')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

        response = self.client.get('/posts/1/')
        # Here we assume that a post with id=1 exists in the test database
        # If not, this will return a 404 error
        self.assertEqual(response.status_code, 200)

    def test_post_create_url_pattern(self):
        """
        Test that the post create URL pattern is correct.
        """
        self.user = User.objects.create_superuser('testuser', 'test@example.com', 'testpassword')
        self.client.login(email='test@example.com', password='testpassword')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

        response = self.client.get('/posts/post/new/')
        self.assertEqual(response.status_code, 200)

    def test_login_url_pattern(self):
         """
         Test that the login URL pattern is correct.
         """
         response = self.client.get('/user/login/')
         self.assertEqual(response.status_code, 200)

    def test_logout_url_pattern(self):
         """
         Test that the logout URL pattern is correct.
         """
         response = self.client.get('/user/logout/')
         # Here we expect a redirect after logout
         self.assertEqual(response.status_code, 302)

    def test_register_url_pattern(self):
         """
         Test that the register URL pattern is correct.
         """
         response = self.client.get('/user/register/')
         self.assertEqual(response.status_code, 200)




