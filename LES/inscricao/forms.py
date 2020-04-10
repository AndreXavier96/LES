from django import forms


# class EscolaForm(forms.Form):  # ModelForm):
#     nome = forms.CharField(label='nome', max_length=50)
#     morada = forms.CharField(label='morada', max_length=50)
#     codigo_postal = forms.CharField(label='codigo_postal', max_length=50)
#     contacto = forms.IntegerField(label='contacto', max_value=999999999, min_value=0)
#     localidade = forms.CharField(label='localidade', max_length=50)

class EscolaForm(forms.Form):  # ModelForm):
    nome = forms.CharField(label='nome_escola', max_length=50)
    morada = forms.CharField(label='morada', max_length=50)
    codigo_postal = forms.CharField(label='codigo_postal', max_length=50)
    contacto = forms.IntegerField(label='contacto', max_value=999999999, min_value=0)
    localidade = forms.CharField(label='localidade', max_length=50)


CHOICES = (('carne', "CARNE"), ('peixe', "PEIXE"), ('vegetariano', "VEGETARIANO"))


class PratoForm(forms.Form):
    prato = forms.CharField(label='test', widget=forms.RadioSelect(choices=CHOICES))


class EpiForm(forms.Form):
    numero_aluno_normal = forms.IntegerField(label='numero_aluno_normal', initial=0)
    numero_aluno_economico = forms.IntegerField(label='numero_aluno_economico', initial=0)
    numero_outro_normal = forms.IntegerField(label='numero_outro_normal', initial=0)
    numero_outro_economico = forms.IntegerField(label='numero_outro_economico', initial=0)


CHOICES_TRANS = (('proprio', "Transporte Proprio"),
                 ('comboio', "Comboio"),
                 ('autocarro', "Autocarro")
                 )


class TransportForm(forms.Form):
    dateTimeOptions = {
        'format': 'dd/mm/yyyy HH:ii P',
        'autoclose': True,
        'showMeridian': True
    }

    hora_chegada = forms.TimeField(label='hora_chegada',required=False)
    hora_partida = forms.DateField(label='hora_partida', widget=forms.DateInput(attrs={'class':'timepicker'}))
    tipo_transporte = forms.CharField(label='tipo_transporte', widget=forms.Select(choices=CHOICES_TRANS))
