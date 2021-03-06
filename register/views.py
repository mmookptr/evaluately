from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .form import AppUserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User


def register(request):
    form = AppUserCreationForm()
    return render(request=request,
                  template_name="register/register.html",
                  context={"form": form})


def get_name(request):
    if request.method == 'POST':
        form = AppUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data['is_admin'] == 'iamadmin':
                user.is_superuser = True
                user.is_staff = True
            user.save()

            return HttpResponseRedirect(reverse('index'))

    return render(request, 'register/register.html', {'form': form})
