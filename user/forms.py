from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

