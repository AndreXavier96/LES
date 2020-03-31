from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login

def register(request):
    form = UserCreationForm
    return render(request,
                  "utilizadores/register.html",
                  context={"form":form})