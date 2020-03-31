from django import forms
from .models import Escola


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Escola
        fields = ['nome', 'morada', 'codigo_postal', 'contacto', 'localidade']
