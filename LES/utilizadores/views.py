from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/utilizadores/login')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/utilizadores/success')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def success(request):
    context = {}
    context['user'] = request.user
    return render(request = request,
                    template_name = "success.html",
                    context={})