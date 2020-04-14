from django.shortcuts import render, redirect
from django.views.generic import View

from utilizadores.models import Utilizador
from .forms import EscolaForm, EmentaInscricaoForm, TransportForm, ParticipanteForm, \
    TipoParticipanteForm, ParticipanteIndForm, ParticipanteGrupoForm, QuerRefeicaoForm
from .models import Ementa, Escola, Inscricao, Utilizadorparticipante, ParticipanteIndividual, ParticipanteGrupo, \
    EmentaInscricao, Transporteproprio, Atividade, SessaoAtividade


def remove(string):
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
        form_trans = TransportForm()
        values = Ementa.objects.all
        escolas = Escola.objects.all
        # -----------
        form_participante = ParticipanteForm()
        radio_tipo_participante = TipoParticipanteForm()
        form_part_ind = ParticipanteIndForm()
        form_part_gru = ParticipanteGrupoForm()
        radio_refeicao = QuerRefeicaoForm()
        # ------------------
        atividades = Atividade.objects.all
        sessaoatividade = SessaoAtividade.objects.all
        # campus = Atividade.objects.filter(localizacao__andar="1")
        return render(request, self.template_name, {'form_escola': form_escola,
                                                    'form_ementa_inscricao': form_ementa_inscricao,
                                                    'values': values,
                                                    'form_trans': form_trans,
                                                    'escolas': escolas,
                                                    'form_participante': form_participante,
                                                    'radio_tipo_participante': radio_tipo_participante,
                                                    'form_part_gru': form_part_gru,
                                                    'form_part_ind': form_part_ind,
                                                    'radio_refeicao': radio_refeicao,
                                                    'atividades': atividades,
                                                    'sessaoatividade': sessaoatividade,
                                                    })

    def post(self, request):
        form_escola = EscolaForm(request.POST)
        form_ementa_inscricao = EmentaInscricaoForm(request.POST)
        form_trans = TransportForm(request.POST)
        form_participante = ParticipanteForm(request.POST)
        radio_tipo_participante = TipoParticipanteForm(request.POST)
        form_part_ind = ParticipanteIndForm(request.POST)
        form_part_gru = ParticipanteGrupoForm(request.POST)
        radio_refeicao = QuerRefeicaoForm(request.POST)
        # ------------escola
        escola_escolhida = request.POST['Escola']
        print("escola:")
        print(escola_escolhida)
        print(form_escola.errors)
        if form_escola.is_valid() and form_participante.is_valid() and \
                radio_tipo_participante.is_valid() and form_ementa_inscricao.is_valid() and \
                radio_refeicao.is_valid() and form_trans.is_valid():
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
            print("form_participante é valida")
            utilizador = Utilizador.objects.get(id='2')
            area_estudos = form_participante['area_estudos'].value()
            ano_estudos = form_participante['ano_estudos'].value()
            Utilizadorparticipante.objects.create(utilizador=utilizador, escola=escola,
                                                  area_estudos=area_estudos, ano_estudos=ano_estudos,
                                                  check_in=0, inscricao=inscricao,
                                                  )
            participante = Utilizadorparticipante.objects.get(inscricao=inscricao)
            radio_value_tipo_part = radio_tipo_participante.cleaned_data.get("TipoParticipante")
            if radio_value_tipo_part == "grupo":
                print("grupo")
                turma = form_part_gru['turma'].value()
                total_participantes = form_part_gru['total_participantes'].value()
                total_professores = form_part_gru['total_professores'].value()
                ParticipanteGrupo.objects.create(total_participantes=total_participantes,
                                                 total_professores=total_professores,
                                                 turma=turma, participante=participante,
                                                 )
            elif radio_value_tipo_part == "individual":
                print("individual")
                acompanhantes = form_part_ind['acompanhantes'].value()
                ParticipanteIndividual.objects.create(acompanhantes=acompanhantes,
                                                      participante=participante,
                                                      )
            # ---------refeicao
            print(radio_refeicao.errors)
            radio_value_refeicao = radio_refeicao.cleaned_data.get("QuerRefeicao")
            print(radio_value_refeicao)
            n_aluno = form_ementa_inscricao['numero_aluno_normal'].value()
            n_outro = form_ementa_inscricao['numero_outro_normal'].value()
            print(n_aluno)
            print(n_outro)
            ementa = Ementa.objects.first()
            EmentaInscricao.objects.create(ementa=ementa, inscricao=inscricao,
                                           numero_aluno_normal=n_aluno,
                                           numero_outro_normal=n_outro
                                           )
            # -----------transporte
            drop_value = form_trans.cleaned_data.get("tipo_transporte")
            trans_campus = 0
            if form_trans['transporte_campus'].value() == "sim":
                trans_campus = 1
            chegada = remove(request.POST['timepicker-one'])
            partida = remove(request.POST['timepicker-two'])
            Transporteproprio.objects.create(hora_chegada=chegada, hora_partida=partida,
                                             tipo_transporte=drop_value,
                                             transporte_campus=trans_campus,
                                             inscricao=inscricao
                                             )
            return redirect('/inscricao/home')
        return redirect('/inscricao')

    # def post(self, request):
    #     form_escola = EscolaForm(request.POST)
    #     form_ementa_inscricao = EmentaInscricaoForm(request.POST)
    #     form_trans = TransportForm(request.POST)
    #     form_participante = ParticipanteForm(request.POST)
    #     radio_tipo_participante = TipoParticipanteForm(request.POST)
    #     form_part_ind = ParticipanteIndForm(request.POST)
    #     form_part_gru = ParticipanteGrupoForm(request.POST)
    #     radio_refeicao = QuerRefeicaoForm(request.POST)
    #     # ------------escola
    #     escola_escolhida = request.POST['Escola']
    #     print("escola:")
    #     print(escola_escolhida)
    #     print(form_escola.errors)
    #     if form_escola.is_valid() and escola_escolhida == 'others':
    #         nome = form_escola['nome'].value()
    #         morada = form_escola['morada'].value()
    #         codigo_postal = form_escola['codigo_postal'].value()
    #         contacto = form_escola['contacto'].value()
    #         localidade = form_escola['localidade'].value()
    #         Escola.objects.create(nome=nome, morada=morada, codigo_postal=codigo_postal, contacto=contacto,
    #                               localidade=localidade)
    #         escola = Escola.objects.get(nome=nome)
    #     else:
    #         escola = Escola.objects.get(nome=escola_escolhida)
    #     inscricao = Inscricao.objects.create(escola=escola, estado="Pendente")
    #     # inscricao = Inscricao.objects.get(escola=escola)
    #
    #     # ------------inscricao grupo/individual
    #     if form_participante.is_valid():
    #         print("form_participante é valida")
    #         utilizador = Utilizador.objects.get(id='2')
    #         area_estudos = form_participante['area_estudos'].value()
    #         ano_estudos = form_participante['ano_estudos'].value()
    #         Utilizadorparticipante.objects.create(utilizador=utilizador, escola=escola,
    #                                               area_estudos=area_estudos, ano_estudos=ano_estudos,
    #                                               check_in=0, inscricao=inscricao,
    #                                               )
    #         participante = Utilizadorparticipante.objects.get(inscricao=inscricao)
    #         if radio_tipo_participante.is_valid():
    #             radio_value_tipo_part = radio_tipo_participante.cleaned_data.get("TipoParticipante")
    #             if radio_value_tipo_part == "grupo":
    #                 print("grupo")
    #                 turma = form_part_gru['turma'].value()
    #                 total_participantes = form_part_gru['total_participantes'].value()
    #                 total_professores = form_part_gru['total_professores'].value()
    #                 ParticipanteGrupo.objects.create(total_participantes=total_participantes,
    #                                                  total_professores=total_professores,
    #                                                  turma=turma, participante=participante,
    #                                                  )
    #             elif radio_value_tipo_part == "individual":
    #                 print("individual")
    #                 acompanhantes = form_part_ind['acompanhantes'].value()
    #                 ParticipanteIndividual.objects.create(acompanhantes=acompanhantes,
    #                                                       participante=participante,
    #                                                       )
    #
    #             # ---------refeicao
    #             print(radio_refeicao.errors)
    #             if form_ementa_inscricao.is_valid() and radio_refeicao.is_valid():
    #                 radio_value_refeicao = radio_refeicao.cleaned_data.get("QuerRefeicao")
    #                 print(radio_value_refeicao)
    #                 n_aluno = form_ementa_inscricao['numero_aluno_normal'].value()
    #                 n_outro = form_ementa_inscricao['numero_outro_normal'].value()
    #                 print(n_aluno)
    #                 print(n_outro)
    #                 ementa = Ementa.objects.first()
    #                 EmentaInscricao.objects.create(ementa=ementa, inscricao=inscricao,
    #                                                numero_aluno_normal=n_aluno,
    #                                                numero_outro_normal=n_outro
    #                                                )
    #                 # -----------transporte
    #                 if form_trans.is_valid():
    #                     drop_value = form_trans.cleaned_data.get("tipo_transporte")
    #                     if form_trans['transporte_campus'].value() == "sim":
    #                         trans_campus = 1
    #                     else:
    #                         trans_campus = 0
    #                     chegada = remove(request.POST['timepicker-one'])
    #                     partida = remove(request.POST['timepicker-two'])
    #                     Transporteproprio.objects.create(hora_chegada=chegada, hora_partida=partida,
    #                                                      tipo_transporte=drop_value,
    #                                                      transporte_campus=trans_campus,
    #                                                      inscricao=inscricao
    #                                                      )
    #                     return redirect('/inscricao/home')
    #     return redirect('/inscricao')
