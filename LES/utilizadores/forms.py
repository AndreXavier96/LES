from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Utilizador, Campus, Unidadeorganica, Utilizadortipo

"""class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    utilizadortipo = forms.IntegerField(required=False, help_text='Optional.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'utilizadortipo', 'password1', 'password2')"""

CHOICES = (('Administrador', "ADMINISTRADOR"), ('Participante', "PARTICIPANTE"), ('Colaborador', "COLABORADOR"),
           ('Docente', "DOCENTE"), ('Coordenador', "COORDENADOR"))
CHOICES2 = (('Faculdade de Economia', "Faculdade de Economia"),
            ('Faculdade de Letras', "Faculdade de Letras"))

class RegisterForm(forms.Form):
    # utilizadortipo = forms.IntegerField(label='utilizadortipo')
    utilizadortipo = forms.CharField(label='utilizadortipo', widget=forms.Select(choices=CHOICES))
    email = forms.CharField(label='email', max_length=50)
    password_digest = forms.CharField(label='password_digest', widget=forms.PasswordInput)
    nome = forms.CharField(label='nome', max_length=50)
    data_nascimento = forms.DateField(label='data_nascimento')
    numero_telemovel = forms.IntegerField(label='numero_telemovel')
    cartao_cidadao = forms.IntegerField(label='cartao_cidadao')
    deficiencias = forms.CharField(label='deficiencias', max_length=50)
    permitir_localizacao = forms.IntegerField(label='permitir_localizacao')
    utilizar_dados_pessoais = forms.IntegerField(label='utilizar_dados_pessoais')
    # unidadeorganica = forms.CharField(label='unidadeorganica', max_length=50)
    unidadeorganica = forms.CharField(label='unidadeorganica', widget=forms.Select(choices=CHOICES2))



""" utilizadortipo = forms.IntegerField(label='utilizadortipo')
 password_digest = forms.CharField(label='password_digest', max_length=50)
 data_nascimento = forms.DateField(label='data_nascimento')
 numero_telemovel = forms.IntegerField(label='numero_telemovel')
 cartao_cidadao = forms.IntegerField(label='cartao_cidadao')
 deficiencias = forms.CharField(label='deficiencias', max_length=50)
 permitir_localizacao = forms.IntegerField(label='permitir_localizacao')
 utilizar_dados_pessoais = forms.IntegerField(label='utilizar_dados_pessoais')
 validado = forms.IntegerField(label='validado')
 unidadeorganica = forms.CharField(label='unidadeorganica', max_length=50)"""

"""'email', 'utilizadortipo', 'data_nascimento', 'numero_telemovel', 'cartao_cidadao', 'deficiencias',
                  'permitir_localizacao', 'utilizar_dados_pessoais', 'unidadeorganica',"""

"""['nome', 'email', 'utilizadortipo', 'data_nascimento', 'numero_telemovel', 'cartao_cidadao', 'deficiencias',
                  'permitir_localizacao', 'utilizar_dados_pessoais', 'unidadeorganica',  'password_digest']"""
