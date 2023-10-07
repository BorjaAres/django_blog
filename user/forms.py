from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Address

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_address', 'city', 'postal_code', 'country']
        widgets = {
            'street_address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }
