from django.test import TestCase, SimpleTestCase, override_settings
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .views import UserLoginView, UserLogoutView, UserRegistrationView
from posts.views import PostCreateView


User = get_user_model()

@override_settings(ROOT_URLCONF='user.urls')
class StatusCodeTests(TestCase):
    """
    Test case for checking status codes.
    """
    def test_logout_status_code(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


@override_settings(ROOT_URLCONF='user.urls')
class ViewResolutionTests(SimpleTestCase):
    """
    Test case for checking view resolution.
    """
    def test_login_view_resolution(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, UserLoginView)

    def test_logout_view_resolution(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, UserLogoutView)

    def test_register_view_resolution(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, UserRegistrationView)

@override_settings(ROOT_URLCONF='user.urls')
class URLPatternTests(TestCase):
    """
    Test case for the URLs in the user application.
    """

    def test_logout_url_pattern(self):
        response = self.client.get('/user/logout/')
        self.assertEqual(response.status_code, 302)
