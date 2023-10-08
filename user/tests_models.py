from django.test import TestCase
from django.contrib.auth import get_user_model
from .forms import UserCreationForm

class UserManagerTest(TestCase):
    def setUp(self):
        self.User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(
            username='testuser', email='testuser@example.com', password='password', first_name='Test', last_name='User')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('password'))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            user = self.User.objects.create_user(
                username='testuser', email='', password='password')

    def test_create_user_without_username(self):
        form = UserCreationForm({
            'username': '',
            'email': 'testuser@example.com',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertFalse(form.is_valid())

    def test_create_user_without_password(self):
        form = UserCreationForm({
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': '',
            'password2': ''
        })
        self.assertFalse(form.is_valid())
    def test_create_user_without_first_name(self):
        user = self.User.objects.create_user(
            username='testuser', email='testuser@example.com', password='password', first_name='', last_name='User')
        self.assertEqual(user.first_name, '')


    def test_create_user_without_last_name(self):
        user = self.User.objects.create_user(
            username='testuser', email='testuser@example.com', password='password', first_name='Test', last_name='')
        self.assertEqual(user.last_name, '')

    def test_create_user_without_first_name_and_last_name(self):
        user = self.User.objects.create_user(
            username='testuser', email='testuser@example.com', password='password', first_name='', last_name='')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_create_superuser(self):
        user = self.User.objects.create_superuser(
            username='testadmin', email='testadmin@example.com', password='password')
        self.assertEqual(user.email, 'testadmin@example.com')
        self.assertTrue(user.check_password('password'))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_superuser_without_email(self):
        with self.assertRaises(ValueError):
            user = self.User.objects.create_superuser(
                username='testadmin', email='', password='password')

    def test_create_superuser_without_username(self):
        with self.assertRaises(ValueError):
            user = self.User.objects.create_superuser(
                username='', email='testadmin@example.com', password='password')

    def test_create_superuser_without_password(self):
        with self.assertRaises(ValueError):
            user = self.User.objects.create_superuser(
                username='testadmin', email='testadmin@example.com', password='')

class UserTest(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username='testuser', email='testuser@example.com', password='password')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser@example.com')

    def test_user_is_active(self):
        self.assertTrue(self.user.is_active)

    def test_user_is_not_staff(self):
        self.assertFalse(self.user.is_staff)

    def test_user_is_not_superuser(self):
        self.assertFalse(self.user.is_superuser)