from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
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

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {
        'form': form
    })

def password_change_done(request):
    messages.info(request, "Password changed")
    return render(request, 'password_change_done.html')