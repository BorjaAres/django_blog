from django.contrib.auth.models import UserManager, AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone

# Define a custom user manager
class CustomUserManager(UserManager):
    # Method to create a user
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        # Normalize the email by lowercasing the domain part of it
        email = self.normalize_email(email)
        # Create a user object
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    # Method to create a regular user
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)

        return self._create_user(username, email, password, **extra_fields)

    # Method to create a superuser
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        return self._create_user(username, email, password, **extra_fields)

# Define a custom user model
class User(AbstractUser, PermissionsMixin):
    # Define fields for the model
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Set to false to require email confirmation before login or to deactive user
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    # Specify the manager for the model
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email
