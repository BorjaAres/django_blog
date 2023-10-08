from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from unittest.mock import patch


class UserLoginViewTest(TestCase):
    def setUp(self):
        """Set up test client and test user."""
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser', email='testuser@example.com', password='12345')
        self.login_url = reverse('login')  # replace 'login' with the actual name of your login url

    def test_login_page(self):
        """Test that the login page loads correctly."""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view(self):
        """Test that a user can log in with correct credentials."""
        # Send POST request with login data
        response = self.client.post(
            self.login_url, {'username': 'testuser', 'email': 'testuser@example.com', 'password': '12345'})
        # Check that the response indicates a successful request
        self.assertEqual(response.status_code, 200)  # check for OK

    def test_next_url_is_set(self):
        """Test that the next session variable is set to the previous page URL."""
        # Send GET request to login view
        response = self.client.get(self.login_url)
        # Check that 'next' is set in session
        self.assertEqual(self.client.session['next'], '/')

    def test_redirect_after_login(self):
        """Test that a user is redirected to the previous page after logging in."""
        # Send GET request to another page
        response = self.client.get('/posts/')
        # Log in the user and follow redirects
        response = self.client.post(
            self.login_url, {'email': 'testuser@example.com', 'password': '12345'}, follow=True)
        # Check that the final response indicates a successful request
        self.assertEqual(response.status_code, 200)  # check for OK
        # Check that the final response is the correct page
        self.assertContains(response, 'posts')

    def test_user_logout_view(self):
        """Test that a user can log out and is redirected to the home page."""
        # Log in the user
        self.client.login(email='testuser@example.com', password='12345')
        url = reverse('logout')
        response = self.client.get(url)
        # Check that the response indicates a successful redirect
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        # Check that the response redirects to the home page
        self.assertRedirects(response, '/')
        # Check that the user is logged out
        self.assertNotIn('_auth_user_id', self.client.session)

class UserRegistrationViewTest(TestCase):
    def setUp(self):
        """Set up test client and registration URL."""
        self.client = Client()
        self.register_url = reverse('register')

    def test_registration_page(self):
        """Test that the registration page loads correctly."""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')

    def test_register_view(self):
        """Test that a user can register with valid data."""
        # Send POST request with registration data
        response = self.client.post(
            self.register_url, {'username': 'testuser', 'password1': 'abcdef123456', 'password2': 'abcdef123456'})
        # Check that the response indicates a successful request
        self.assertEqual(response.status_code, 200)  # check for OK


