from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from user.views import UserLoginView, UserLogoutView, UserRegistrationView
from posts.views import PostCreateView

User = get_user_model()

class URLTests(TestCase):
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

    def test_logout_url(self):
         """
         Test the logout URL.
         The response status code should be 302 (Found), as we expect a redirect after logout.
         The correct view function should be used.
         """
         url = reverse('logout')
         response = self.client.get(url)
         self.assertEqual(response.status_code, 302)
         self.assertEqual(response.resolver_match.func.view_class, UserLogoutView)

    def test_register_url(self):
         """
         Test the register URL.
         The response status code should be 200 (OK).
         The correct view function should be used.
         """
         url = reverse('register')
         response = self.client.get(url)
         self.assertEqual(response.status_code, 200)
         self.assertEqual(response.resolver_match.func.view_class, UserRegistrationView)

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


class CheckURLSettingsTests(SimpleTestCase):
    """
    Test case for checking that URLs resolve to the correct views.
    """

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

    def test_post_create_url_resolves(self):
        """
        Test that the URL for the post create view resolves to the correct view.
        """
        url = reverse('post_create')
        self.assertEqual(resolve(url).func.view_class, PostCreateView)

class CheckUrlConfigTests(SimpleTestCase):
    """
    Test case for checking that URLs resolve to the correct views.
    """

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

    def test_post_create_url_resolves(self):
        """
        Test that the URL for the post create view resolves to the correct view.
        """
        url = reverse('post_create')
        self.assertEqual(resolve(url).func.view_class, PostCreateView)
