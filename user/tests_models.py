from django.test import TestCase
from django.contrib.auth import get_user_model
from .forms import UserCreationForm

class TestUserManager(TestCase):
    """Test case for the UserManager in the User app."""

    @classmethod
    def setUpTestData(cls):
        """Set up the test environment before each test method is run."""
        cls.User = get_user_model()

    def test_create_valid_user(self):
        """Test creating a user with valid data."""
        user = self.User.objects.create_user(
            username='testuser', email='testuser@example.com', password='password', first_name='Test', last_name='User')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('password'))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_user_without_email(self):
        """Test creating a user without an email raises a ValueError."""
        with self.assertRaisesMessage(ValueError, 'Email is required'):
            user = self.User.objects.create_user(
                username='testuser', email='', password='password')

    def test_create_user_without_username(self):
        """Test creating a user without a username is invalid."""
        form = UserCreationForm({
            'username': '',
            'email': 'testuser@example.com',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertFalse(form.is_valid())
        self.assertFormError(form, 'username', 'This field is required.')

    def test_create_user_without_password(self):
        """Test creating a user without a password is invalid."""
        form = UserCreationForm({
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': '',
            'password2': ''
        })
        self.assertFalse(form.is_valid())
        self.assertFormError(form, 'password1', 'This field is required.')

    def test_create_user_without_last_name(self):
        """Test creating a user without a last name is valid."""
        user = self.User.objects.create_user(
            username='testuser', email='testuser@example.com', password='password', first_name='Test', last_name='')
        self.assertEqual(user.last_name, '')

    def test_create_valid_superuser(self):
        """Test creating a superuser with valid data."""
        user = self.User.objects.create_superuser(
            username='testadmin', email='testadmin@example.com', password='password')
        self.assertEqual(user.email, 'testadmin@example.com')
        self.assertTrue(user.check_password('password'))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_superuser_without_email(self):
        """Test creating a superuser without an email raises a ValueError."""
        with self.assertRaisesMessage(ValueError, 'Email is required'):
            user = self.User.objects.create_superuser(
                username='testadmin', email='', password='password')


class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user instance for testing
        cls.user = get_user_model().objects.create_user(
            username='testuser', email='testuser@example.com', password='password')

    def test_user_str_returns_email(self):
        # Test that the user's string representation is their email
        self.assertEqual(str(self.user), 'testuser@example.com')

    def test_user_is_active_by_default(self):
        # Test that the user is active by default
        self.assertTrue(self.user.is_active)

    def test_user_is_not_staff_by_default(self):
        # Test that the user is not staff by default
        self.assertFalse(self.user.is_staff)

    def test_user_is_not_superuser_by_default(self):
        # Test that the user is not superuser by default
        self.assertFalse(self.user.is_superuser)

