from django import forms


class EscolaForm(forms.Form):  # ModelForm):
    nome = forms.CharField(label='nome_escola', max_length=50)
    morada = forms.CharField(label='morada', max_length=50)
    codigo_postal = forms.CharField(label='codigo_postal', max_length=50)
    contacto = forms.IntegerField(label='contacto', max_value=999999999, min_value=0)
    localidade = forms.CharField(label='localidade', max_length=50)


CHOICES_PRATO = (('carne', "CARNE"), ('peixe', "PEIXE"), ('vegetariano', "VEGETARIANO"))


class PratoForm(forms.Form):
    prato = forms.CharField(label='test', widget=forms.RadioSelect(choices=CHOICES_PRATO))


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
    hora_chegada = forms.TimeField(label='hora_chegada', required=False)
    hora_partida = forms.TimeField(label='hora_partida', required=False)
    tipo_transporte = forms.CharField(label='tipo_transporte', widget=forms.Select(choices=CHOICES_TRANS))


class ParticipanteForm(forms.Form):
    area_estudos = forms.CharField(label='area_estudos', required=True)
    ano_estudos = forms.IntegerField(label='ano_estudos', required=True)


class ParticipanteGrupoForm(forms.Form):
    turma = forms.CharField(label='turma', required=True)
    total_participantes = forms.IntegerField(label='total_participantes', required=True)
    total_professores = forms.IntegerField(label='total_professores', required=True)


class ParticipanteIndForm(forms.Form):
    acompanhantes = forms.CharField(label='acompanhantes', required=True)


CHOICE_TIPO_PARTICIPANTE = (('individual', "individual"), ('grupo', "grupo"))


class TipoParticipanteForm(forms.Form):
    TipoParticipante = forms.CharField(label='TipoParticipante (automatico com a sessao)',
                                       widget=forms.RadioSelect(choices=CHOICE_TIPO_PARTICIPANTE,
                                                                attrs={'onchange': 'CheckTipoParticipante(this.value);'}
                                                                ))


CHOICE_BOL = (('sim', "sim"), ('nao', "nao"))


class UtilizarDadosForm(forms.Form):
    bol = forms.CharField(label="Utilizar dados da conta para inscrição?",
                          widget=forms.RadioSelect(choices=CHOICE_BOL,
                                                   attrs={'onchange': 'CheckUtilizar(this.value);'}
                                                   ))


class DadosForm(forms.Form):
    nome = forms.CharField(label='nome', required=False)
    email = forms.EmailField(label='email', required=False)
    contacto = forms.IntegerField(label='telemovel', required=False)
