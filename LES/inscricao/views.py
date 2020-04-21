from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail

from utilizadores.models import Utilizador
from .forms import EscolaForm, EmentaInscricaoForm, ParticipanteForm, \
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
        form_escola = EscolaForm()
        form_ementa_inscricao = EmentaInscricaoForm()
        values = Ementa.objects.all
        escolas = Escola.objects.all
        # -----------
        form_participante = ParticipanteForm()
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
        return render(request, self.template_name, {'form_escola': form_escola,
                                                    'form_ementa_inscricao': form_ementa_inscricao,
                                                    'values': values,
                                                    'escolas': escolas,
                                                    'form_participante': form_participante,
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
        form_escola = EscolaForm(request.POST)
        form_ementa_inscricao = EmentaInscricaoForm(request.POST)
        form_participante = ParticipanteForm(request.POST)
        form_part_ind = ParticipanteIndForm(request.POST)
        radio_refeicao = QuerRefeicaoForm(request.POST)

        # ------------escola
        escola_escolhida = request.POST['Escola']
        if escola_escolhida != "Escolher":
            if form_escola.is_valid() and form_participante.is_valid() and \
                    form_ementa_inscricao.is_valid() and radio_refeicao.is_valid():
                if escola_escolhida == 'others':
                    nome = form_escola['nome'].value()
                    morada = form_escola['morada'].value()
                    codigo_postal = form_escola['codigo_postal'].value()
                    contacto = form_escola['contacto'].value()
                    localidade = form_escola['localidade'].value()
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

                area_estudos = form_participante['area_estudos'].value()
                ano_estudos = form_participante['ano_estudos'].value()
                Utilizadorparticipante.objects.create(utilizador=utilizador, escola=escola,
                                                      area_estudos=area_estudos, ano_estudos=ano_estudos,
                                                      check_in=0, inscricao=inscricao,
                                                      )
                participante = Utilizadorparticipante.objects.get(inscricao=inscricao)
                radio_value_tipo_part = utilizador.utilizadortipo.tipo
                if radio_value_tipo_part == "Participante em Grupo":
                    turma = request.POST['turma'].value()
                    total_participantes = request.POST['total_participantes'].value()
                    total_professores = request.POST['total_professores'].value()
                    ParticipanteGrupo.objects.create(total_participantes=total_participantes,
                                                     total_professores=total_professores,
                                                     turma=turma, participante=participante,
                                                     )
                elif radio_value_tipo_part == "Participante Individual":
                    acompanhantes = form_part_ind['acompanhantes'].value()
                    ParticipanteIndividual.objects.create(acompanhantes=acompanhantes,
                                                          participante=participante,
                                                          )
                # ---------refeicao
                # radio_value_refeicao = radio_refeicao.cleaned_data.get("QuerRefeicao")
                n_aluno = form_ementa_inscricao['numero_aluno_normal'].value()
                n_outro = form_ementa_inscricao['numero_outro_normal'].value()
                ementa = Ementa.objects.first()
                EmentaInscricao.objects.create(ementa=ementa, inscricao=inscricao,
                                               numero_aluno_normal=n_aluno,
                                               numero_outro_normal=n_outro
                                               )
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
                    send_mail(
                        'Inscricao Dia Aberto',
                        'Seguem em anexo um pdf com os dados relativos á sua Inscricao',
                        'xavidolol@gmail.com',
                        [utilizador.email],
                    )
                    return render(request, 'home.html', context={'MSG': "Inscricao com Sucesso"})
                else:
                    return render(request, 'home.html', context={'MSG': "Deve de escolher pelo menos uma Sessao"})
        else:
            return render(request, 'home.html', context={'MSG': "Deve de escolher uma Escola"})
        return redirect('/inscricao')
