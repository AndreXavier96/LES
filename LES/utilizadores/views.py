from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register(request):
    form = UserCreationForm
    return render(request,
                  "register.html",
                  context={"form": form})


def logout(request):
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "login.html",
                  context={"form":form})
