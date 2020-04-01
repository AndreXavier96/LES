from django import forms
from .models import Escola, EmentaPratoInscricao
from django.forms.widgets import CheckboxSelectMultiple


class EscolaForm(forms.Form):  # ModelForm):
    # class Meta:
    #     model = Escola
    #     fields = ['nome', 'morada', 'codigo_postal', 'contacto', 'localidade']
    nome = forms.CharField(label='nome', max_length=50)
    morada = forms.CharField(label='morada', max_length=50)
    codigo_postal = forms.CharField(label='codigo_postal', max_length=50)
    contacto = forms.CharField(label='contacto', max_length=50)
    localidade = forms.CharField(label='localidade', max_length=50)


CHOICES = (('carne', "CARNE"), ('peixe', "PEIXE"), ('vegetariano', "VEGETARIANO"))


class PratoForm(forms.Form):
    prato = forms.CharField(label='test', widget=forms.RadioSelect(choices=CHOICES))


class EpiForm(forms.ModelForm):
    class Meta:
        model = EmentaPratoInscricao
        fields = ['numero_aluno_normal',
                  'numero_aluno_economico'
                  ]


'''class Form(forms.ModelForm):
    class Meta:
        model = Escola, EmentaPratoInscricao
        fields = [{'nome', 'morada', 'codigo_postal', 'contacto',
                  'localidade'}, {'numero_aluno_normal',
                  'numero_aluno_economico'}
                  ]'''
