from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='username', max_length=100)
    your_password = forms.CharField(label='password', max_length=100)


