from django import forms
from .models import AppUser
from django.contrib.auth.forms import UserCreationForm

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'password1', 'password2', 'is_admin')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = self.cleaned_data['is_admin'] == 'iamadmin'
        if commit:
            user.save()
        return user
