from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from LES.utils import render_to_pdf
from utilizadores.models import Utilizador
from .forms import EmentaInscricaoForm, \
    ParticipanteIndForm, QuerRefeicaoForm, TransporteEntreCampusForm, \
    TransporteParaCampusForm
from .models import Ementa, Escola, Inscricao, Utilizadorparticipante, ParticipanteIndividual, ParticipanteGrupo, \
    EmentaInscricao, Transporteproprio, Atividade, SessaoAtividade, SessaoAtividadeInscricao


def remove_all_space(string):
    return string.replace(" ", "")


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, 'home.html')


class InscricaoView(View):
    template_name = 'inscricao.html'

    def get(self, request):
        form_ementa_inscricao = EmentaInscricaoForm()
        values = Ementa.objects.all
        escolas = Escola.objects.all
        # -----------
        form_part_ind = ParticipanteIndForm()
        radio_refeicao = QuerRefeicaoForm()
        # ------------------
        atividades = Atividade.objects.all
        sessaoatividade = SessaoAtividade.objects.all
        transporte_para_campus = TransporteParaCampusForm(initial={'sim': 'Sim'})
        transporte_entre_campus = TransporteEntreCampusForm(initial={'nao': 'Não'})
        # ---------------
        auth_user = request.user
        utilizador = Utilizador.objects.get(pk=auth_user.id)
        # ----------------------
        return render(request, self.template_name, {'form_ementa_inscricao': form_ementa_inscricao,
                                                    'values': values,
                                                    'escolas': escolas,
                                                    'form_part_ind': form_part_ind,
                                                    'radio_refeicao': radio_refeicao,
                                                    'atividades': atividades,
                                                    'sessaoatividade': sessaoatividade,
                                                    'transporte_para_campus': transporte_para_campus,
                                                    'transporte_entre_campus': transporte_entre_campus,
                                                    'auth_user': auth_user,
                                                    'utilizador': utilizador
                                                    })

    def post(self, request):
        form_ementa_inscricao = EmentaInscricaoForm(request.POST)
        form_part_ind = ParticipanteIndForm(request.POST)
        radio_refeicao = QuerRefeicaoForm(request.POST)

        # ------------escola
        escola_escolhida = request.POST['Escola']
        if escola_escolhida != "Escolher":
            if form_ementa_inscricao.is_valid() and radio_refeicao.is_valid():
                if escola_escolhida == 'others':
                    nome = request.POST['nome'].value()
                    morada = request.POST['morada'].value()
                    codigo_postal = request.POST['codigo_postal'].value()
                    contacto = request.POST['contacto'].value()
                    localidade = request.POST['localidade'].value()
                    Escola.objects.create(nome=nome, morada=morada, codigo_postal=codigo_postal, contacto=contacto,
                                          localidade=localidade)
                    escola = Escola.objects.get(nome=nome)
                else:
                    escola = Escola.objects.get(nome=escola_escolhida)
                inscricao = Inscricao.objects.create(escola=escola, estado="Pendente")
                # ------------inscricao grupo/individual
                # session user--------------------------------------
                auth_user = request.user
                utilizador = Utilizador.objects.get(pk=auth_user.id)
                # session user--------------------------------------

                area_estudos = request.POST['area_estudos']
                ano_estudos = request.POST['ano_estudos']
                Utilizadorparticipante.objects.create(utilizador=utilizador, escola=escola,
                                                      area_estudos=area_estudos, ano_estudos=ano_estudos,
                                                      check_in=0, inscricao=inscricao,
                                                      )
                participante = Utilizadorparticipante.objects.get(inscricao=inscricao)
                radio_value_tipo_part = utilizador.utilizadortipo.tipo
                if radio_value_tipo_part == "Participante em Grupo":
                    turma = request.POST['turma']
                    total_participantes = request.POST['total_participantes']
                    total_professores = request.POST['total_professores']
                    ParticipanteGrupo.objects.create(total_participantes=total_participantes,
                                                     total_professores=total_professores,
                                                     turma=turma, participante=participante,
                                                     )
                    participante2 = ParticipanteGrupo.objects.get(participante=participante)
                elif radio_value_tipo_part == "Participante Individual":
                    acompanhantes = form_part_ind['acompanhantes'].value()
                    ParticipanteIndividual.objects.create(acompanhantes=acompanhantes,
                                                          participante=participante,
                                                          )
                    participante2 = ParticipanteGrupo.objects.get(participante=participante)
                # ---------refeicao
                # radio_value_refeicao = radio_refeicao.cleaned_data.get("QuerRefeicao")
                n_aluno = form_ementa_inscricao['numero_aluno_normal'].value()
                n_outro = form_ementa_inscricao['numero_outro_normal'].value()
                # preco_total = request.POST['preco_total'].value()
                ementa = Ementa.objects.first()
                EmentaInscricao.objects.create(ementa=ementa, inscricao=inscricao,
                                               numero_aluno_normal=n_aluno,
                                               numero_outro_normal=n_outro
                                               )
                ementainscricao = EmentaInscricao.objects.get(inscricao=inscricao)
                # -----------transporte
                drop_value = request.POST['tipo_transporte']
                trans_para_campus = ""
                trans_entre_campus = ""
                if drop_value == "autocarro" or drop_value == "comboio":
                    trans_para_campus_value = request.POST['QuerTransportePara']
                    if trans_para_campus_value == "sim":
                        trans_para_campus = request.POST['qual']
                    else:
                        trans_para_campus = "nao"
                    trans_entre_campus_value = request.POST['QuerTransporteEntre']
                    if trans_entre_campus_value == 'sim':
                        trans_entre_campus = request.POST['transporte_campus']
                    else:
                        trans_entre_campus = "nao"
                chegada = remove_all_space(request.POST['timepicker-one'])
                partida = remove_all_space(request.POST['timepicker-two'])
                entre_campus_horario = remove_all_space(request.POST['timepicker-three'])
                Transporteproprio.objects.create(hora_chegada=chegada, hora_partida=partida,
                                                 tipo_transporte=drop_value,
                                                 transporte_para_campus=trans_para_campus,
                                                 transporte_entre_campus=trans_entre_campus,
                                                 hora_entre_campus=entre_campus_horario,
                                                 inscricao=inscricao
                                                 )
                transporte = Transporteproprio.objects.get(inscricao=inscricao)
                row_count = int(request.POST['row_countt'])
                if row_count > 0:
                    rows_deleted_count = request.POST['row_deletedd']
                    list_deleted = []
                    for y in range(int(rows_deleted_count)):
                        list_deleted.append(request.POST['row_deleted_' + str(y)])
                    for x in range(row_count):
                        if str(x) not in list_deleted:
                            sessao_actividade_id = request.POST['sessao_atividade_' + str(x)]
                            n_inscritos = request.POST['inscritos_sessao_' + str(x)]
                            sessao_actividade = SessaoAtividade.objects.get(pk=sessao_actividade_id)
                            SessaoAtividadeInscricao.objects.create(sessao_atividade=sessao_actividade,
                                                                    inscricao=inscricao, numero_alunos=n_inscritos
                                                                    )
                            novo_numero_alunos = SessaoAtividade.objects.get(pk=sessao_actividade_id).n_alunos - int(
                                n_inscritos)
                            sessao_actividade.n_alunos = novo_numero_alunos
                            sessao_actividade.save()
                    sessao = SessaoAtividadeInscricao.objects.filter(inscricao=inscricao)
                    data = {
                        'participante': participante,
                        'utilizador': utilizador,
                        'participantetipo': participante2,
                        'sessao': sessao,
                        'transporte': transporte,
                        'eminsc': ementainscricao,
                    }
                    email = EmailMessage()
                    email.subject = 'Inscricao Dia Aberto'
                    email.body = 'Seguem em anexo um pdf com os dados relativos á sua Inscricao'
                    email.from_email = settings.EMAIL_HOST_USER
                    email.to = ['xavi.6696@gmail.com']
                    pdf = render_to_pdf(data)
                    # preview------------------------------------
                    # if pdf:
                    #     response = HttpResponse(pdf, content_type='application/pdf')
                    #     filename = "PrivacyRequest_%s.pdf" % "1234"
                    #     content = "inline; filename='%s'" % filename
                    #     response['Content-Disposition'] = content
                    #     return response
                    email.attach('inscricao.pdf', pdf.getvalue(), 'application/pdf')
                    email.send()
                    return render(request, 'home.html', context={'MSG': "Inscricao com Sucesso"})
                else:
                    return render(request, 'home.html', context={'MSG': "Deve de escolher pelo menos uma Sessao"})
        else:
            return render(request, 'home.html', context={'MSG': "Deve de escolher uma Escola"})
        return render(request, 'home.html', context={'MSG': "erro"})
