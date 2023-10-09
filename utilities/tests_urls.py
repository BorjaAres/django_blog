from django.test import TestCase, SimpleTestCase, override_settings
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from user.views import UserLoginView, UserLogoutView, UserRegistrationView
from posts.views import PostCreateView, BlogHomeView, AllPostsView, PostDetailView
from utilities.views import IndexView, ContactView, AboutUsView
from posts.models import Post

User = get_user_model()

@override_settings(ROOT_URLCONF='utilities.urls')
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
@override_settings(ROOT_URLCONF='utilities.urls')
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

@override_settings(ROOT_URLCONF='utilities.urls')
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
