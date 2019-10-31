from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .form import NameForm
from django.http import HttpResponseRedirect
from .models import User

# Create your views here.
def register(request):
    form = UserCreationForm
    return render(request = request,
                  template_name = "register/register.html",
                  context={"form":form})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.data.get('your_name')
            password = form.data.get('your_password')
            user = User(username = name, password = password)
            user.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/register/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'register.html', {'form': form})