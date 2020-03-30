from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(
        request,
        "Dia_Aberto/index.html",
        {
            'content': " hello"
        }
    )


def login(request):
    form = AuthenticationForm()
    return render(request=request,
                  template_name="Dia_Aberto/login.html",
                  context={"form": form})


def register(request):
    return render(
        request,
        "Dia_Aberto/register.html",
        {
            'content': " Register"
        }
    )


def inscricao(request):
    return render(
        request,
        "Dia_Aberto/inscricao.html",
        {
            'content': " paquito"
        }
    )


def logout_request(request):
    logout(request)
    #messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")
