from django import forms

CHOICE_BOL = (('sim', "Sim"), ('nao', "Não"))


class EmentaInscricaoForm(forms.Form):
    numero_aluno_normal = forms.IntegerField(initial=0, min_value=0)
    numero_outro_normal = forms.IntegerField(initial=0, min_value=0)


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


class FileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField(label="Autorização")
