from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    tipo_utilizador = forms.CharField(max_length=30, required=False, help_text='Required.')
    data_nascimento = forms.DateField(required=True, help_text='Required.')
    n_tele = forms.IntegerField(required=True, help_text='Required.')
    c_cidadao = forms.IntegerField(required=True, help_text='Required.')
    deficiencias = forms.BooleanField(required=True, help_text='Required.')
    localizacao = forms.BooleanField(required=True, help_text='Required.')
    dados_pessoais = forms.BooleanField(required=True, help_text='Required.')
    unidade_organica = forms.BooleanField(required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'email', 'tipo_utilizador', 'data_nascimento', 'n_tele', 'c_cidadao', 'deficiencias',
                  'localizacao', 'dados_pessoais', 'unidade_organica',  'password1', 'password2', )