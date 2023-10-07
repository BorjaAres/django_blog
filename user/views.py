from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .forms import UserCreationForm, UserAddressForm
from .models import User, Address

class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    # Redirect to the previous page after login
    def get(self, request, *args, **kwargs):
        request.session['next'] = request.META.get('HTTP_REFERER', '/')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        next_url = self.request.session.pop('next', '/')
        return redirect(next_url)

class UserLogoutView(LogoutView):
    pass

class UserAddressView():
    pass

class UserRegistrationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration.html'

    def form_valid(self, form):
        # After a successful registration, log the user in
        response = super(UserRegistrationView, self).form_valid(form)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        # Redirect to home page after registration is successful
        return '/'


