from django.shortcuts import render
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
    return render(
        request,
        "Dia_Aberto/login.html",
        {
            'content': " Login"
            }
        )

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
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")