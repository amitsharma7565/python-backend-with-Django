from django import forms
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class RegisterForm(UserCreationForm):
    class Meta:
        model= User
        fields =['username', 'email', 'password1', 'password2']


