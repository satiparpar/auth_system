from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from auth_system.config.models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'password', 'confirm_password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(required=True)
