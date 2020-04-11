from django.shortcuts import render, redirect
from django.views.generic import View

from utilizadores.models import Utilizador
from .forms import EscolaForm, EpiForm, PratoForm, TransportForm, ParticipanteForm, DadosForm, \
    TipoParticipanteForm, UtilizarDadosForm, ParticipanteIndForm, ParticipanteGrupoForm
from .models import Ementa, Escola, Inscricao, Prato, EmentaPratoInscricao, Transporteproprio, Utilizadorparticipante, \
    ParticipanteIndividual, ParticipanteGrupo


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, 'home.html')


class InscricaoView(View):
    template_name = 'inscricao.html'

    def get(self, request):
        form_prato = PratoForm()
        form_escola = EscolaForm()
        form_epi = EpiForm()
        form_trans = TransportForm()
        values = Ementa.objects.all
        escolas = Escola.objects.all
        # -----------
        form_participante = ParticipanteForm()
        radio_tipo_participante = TipoParticipanteForm()
        form_part_ind = ParticipanteIndForm()
        form_part_gru = ParticipanteGrupoForm()
        # ----------
        return render(request, self.template_name, {'form_prato': form_prato,
                                                    'form_escola': form_escola,
                                                    'form_epi': form_epi,
                                                    'values': values,
                                                    'form_trans': form_trans,
                                                    'escolas': escolas,
                                                    'form_participante': form_participante,
                                                    'radio_tipo_participante': radio_tipo_participante,
                                                    'form_part_gru': form_part_gru,
                                                    'form_part_ind': form_part_ind,
                                                    })

    def post(self, request):
        form_escola = EscolaForm(request.POST)
        form_prato = PratoForm(request.POST)
        form_epi = EpiForm(request.POST)
        form_trans = TransportForm(request.POST)
        form_participante = ParticipanteForm(request.POST)
        radio_tipo_participante = TipoParticipanteForm(request.POST)
        form_part_ind = ParticipanteIndForm(request.POST)
        form_part_gru = ParticipanteGrupoForm(request.POST)
        # ------------escola
        if form_escola.is_valid():
            nome = form_escola['nome'].value()
            morada = form_escola['morada'].value()
            codigo_postal = form_escola['codigo_postal'].value()
            contacto = form_escola['contacto'].value()
            localidade = form_escola['localidade'].value()
            Escola.objects.create(nome=nome, morada=morada, codigo_postal=codigo_postal, contacto=contacto,
                                  localidade=localidade)
            escola = Escola.objects.get(nome=nome)

            Inscricao.objects.create(escola=escola, estado="Pendente")
            inscricao = Inscricao.objects.get(escola=escola)

            # ------------inscricao grupo/individual
            if form_participante.is_valid():
                print("form_participante é valida")
                utilizador = Utilizador.objects.get(id='2')
                area_estudos = form_participante['area_estudos'].value()
                ano_estudos = form_participante['ano_estudos'].value()
                Utilizadorparticipante.objects.create(utilizador=utilizador, escola=escola,
                                                      area_estudos=area_estudos, ano_estudos=ano_estudos,
                                                      check_in=0, inscricao=inscricao,
                                                      )
                participante = Utilizadorparticipante.objects.get(inscricao=inscricao)
                if radio_tipo_participante.is_valid():
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

                # ---------prato
                if form_prato.is_valid():
                    radio_value = form_prato.cleaned_data.get("prato")
                    prato = Prato.objects.get(tipo=radio_value)
                    ementa = Ementa.objects.all().first()
                    # EmentaPratoInscricao.objects.create(ementa=ementa, prato=prato, inscricao=inscricao)
                    if form_epi.is_valid():
                        n_a_n = form_epi['numero_aluno_normal'].value()
                        n_a_e = form_epi['numero_aluno_economico'].value()
                        n_o_n = form_epi['numero_outro_normal'].value()
                        n_o_e = form_epi['numero_outro_economico'].value()
                        EmentaPratoInscricao.objects.create(ementa=ementa, prato=prato, inscricao=inscricao,
                                                            numero_aluno_normal=n_a_n,
                                                            numero_aluno_economico=n_a_e,
                                                            numero_outro_normal=n_o_n,
                                                            numero_outro_economico=n_o_e,
                                                            )
                        if form_trans.is_valid():
                            drop_value = form_trans.cleaned_data.get("tipo_transporte")
                            chegada = form_trans['hora_chegada'].value()
                            partida = form_trans['hora_partida'].value()

                            Transporteproprio.objects.create(hora_chegada=chegada, hora_partida=partida,
                                                             tipo_transporte=drop_value,
                                                             inscricao=inscricao
                                                             )
                        return redirect('/inscricao/home')
            return redirect('/inscricao')
