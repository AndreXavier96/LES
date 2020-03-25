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

<<<<<<< HEAD
def register(request):
    return render(
        request,
        "Dia_Aberto/register.html",
        {
            'content': " Register"
=======

def inscricao(request):
    return render(
        request,
        "Dia_Aberto/inscricao.html",
        {
            'content': " paquito"
>>>>>>> a78af35ae88cfeac685958d4b3925b078a718c63
            }
        )