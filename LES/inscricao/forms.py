from django import forms

CHOICE_BOL = (('sim', "Sim"), ('nao', "Não"))

CHOICES_AREA = (('escolha', {'label': 'Escolher', 'hidden': True}), ('ciencias', "Ciências e Tecnologias"),
                ('humanidades', "Línguas e Humanidades"),
                ('artes', "Artes Visuais"), ('socioeconomicas', "Ciências Socioeconómicas"))


class EscolaForm(forms.Form):
    nome = forms.CharField(label='nome_escola', max_length=50, required=False)
    morada = forms.CharField(label='morada', max_length=50, required=False)
    codigo_postal = forms.CharField(label='codigo_postal', max_length=50, required=False)
    contacto = forms.IntegerField(label='contacto', max_value=999999999, min_value=0, required=False)
    localidade = forms.CharField(label='localidade', max_length=50, required=False)


class EmentaInscricaoForm(forms.Form):
    numero_aluno_normal = forms.IntegerField(initial=0)
    numero_outro_normal = forms.IntegerField(initial=0)


class ParticipanteForm(forms.Form):
    area_estudos = forms.CharField(label='area_estudos', required=True,
                                   widget=forms.SelectWithHidden(choices=CHOICES_AREA))
    ano_estudos = forms.IntegerField(label='ano_estudos', required=True)


class ParticipanteGrupoForm(forms.Form):
    turma = forms.CharField(label='turma', required=True)
    total_participantes = forms.IntegerField(label='total_participantes', required=True)
    total_professores = forms.IntegerField(label='total_professores', required=True)


class ParticipanteIndForm(forms.Form):
    acompanhantes = forms.IntegerField(label='acompanhantes', required=True)


class QuerRefeicaoForm(forms.Form):
    QuerRefeicao = forms.CharField(label="Deseja refeição?",
                                   widget=forms.RadioSelect(choices=CHOICE_BOL,
                                                            attrs={'onchange': 'CheckRefeicao(this.value);'})
                                   )


class TransporteParaCampusForm(forms.Form):
    QuerTransportePara = forms.CharField(label="Vai desejar transporte entre a estação e algum dos Campus?",
                                         widget=forms.RadioSelect(choices=CHOICE_BOL,
                                                                  attrs={'onchange': 'paraCampus(this.value);'})
                                         )


class TransporteEntreCampusForm(forms.Form):
    QuerTransporteEntre = forms.CharField(label="Vai desejar transporte entre os Campus?",
                                          widget=forms.RadioSelect(choices=CHOICE_BOL,
                                                                   attrs={'onchange': 'entreCampus(this.value);'})
                                          )
