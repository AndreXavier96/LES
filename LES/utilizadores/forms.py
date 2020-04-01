from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Utilizador


class RegisterForm(UserCreationForm):
    class Meta:
        model = Utilizador
        fields = ['nome', 'email', 'utilizadortipo', 'data_nascimento', 'numero_telemovel', 'cartao_cidadao', 'deficiencias',
                  'permitir_localizacao', 'utilizar_dados_pessoais', 'unidadeorganica',  'password1', 'password2']



        class reset_form(forms.Form):

            oldpassword = forms.CharField(max_length=20, widget=forms.TextInput(
                attrs={'type': 'password', 'placeholder': 'your old Password', 'class': 'span'}))
            newpassword1 = forms.CharField(max_length=20, widget=forms.TextInput(
                attrs={'type': 'password', 'placeholder': 'New Password', 'class': 'span'}))
            newpassword2 = forms.CharField(max_length=20, widget=forms.TextInput(
                attrs={'type': 'password', 'placeholder': 'Confirm New Password', 'class': 'span'}))

            def clean(self):
                if 'newpassword1' in self.cleaned_data and 'newpassword2' in self.cleaned_data:
                    if self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
                        raise forms.ValidationError(_("The two password fields did not match."))
                return self.cleaned_data