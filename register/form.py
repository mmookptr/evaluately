from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AppUserCreationForm(UserCreationForm):
    is_admin = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_admin')
