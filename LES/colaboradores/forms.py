from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Utilizador

"""class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    utilizadortipo = forms.IntegerField(required=False, help_text='Optional.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'utilizadortipo', 'password1', 'password2')"""

'''CHOICES = (('Administrador', "ADMINISTRADOR"), ('Participante', "PARTICIPANTE"), ('Colaborador', "COLABORADOR"),
           ('Docente', "DOCENTE"), ('Coordenador', "COORDENADOR"))
CHOICES2 = (('Faculdade de Economia', "Faculdade de Economia"),
            ('Faculdade de Letras', "Faculdade de Letras"))'''

class Criar_Colab_Form(forms.Form):
    primeiro_dia = forms.IntegerField(label='primeiro_dia')
    segundo_dia = forms.IntegerField(label='segundo_dia')
    sala_de_aula = forms.IntegerField(label='sala_de_aula')
    percurso = forms.IntegerField(label='percurso')



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

