from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .models import User


def register(request):
    form = UserCreationForm()
    return render(request=request,
                  template_name="register/register.html",
                  context={"form": form})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print("a")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = NameForm()

    return render(request, 'register/register.html', {'form': form})
