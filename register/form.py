from django import forms
from .models import User

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='username', max_length=100)
#     your_password = forms.CharField(label='password', max_length=100)
#     confirm_password = forms.CharField(widget=forms.PasswordInput())

#     class Meta:
#         model = User
#         fields = ('yourname', 'password')
