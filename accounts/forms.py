from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class StudentRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']
