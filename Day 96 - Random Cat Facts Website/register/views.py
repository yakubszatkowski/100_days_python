from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response, user)
            return redirect('/') 
        else:
            print('wrongform')
    else:
        form = RegisterForm()
    return render(response, "register.html", {'form': form})