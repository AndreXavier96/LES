from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Utilizadortipo


class RegisterForm(UserCreationForm):
    class Meta:
        model = Utilizadortipo
        fields = ['nome', 'email', 'utilizadortipo', 'data_nascimento', 'numero_telemovel', 'cartao_cidadao', 'deficiencias',
                  'permitir_localizacao', 'utilizar_dados_pessoais', 'unidadeorganica',  'password1', 'password2']

