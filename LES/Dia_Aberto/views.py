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

def inscricao(request):
    return render(
        request,
        "Dia_Aberto/inscricao.html",
        {
            'content': " paquito"
            }
        )