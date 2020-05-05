from datetime import date

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from LES.utils import render_to_pdf
from utilizadores.models import Utilizador
from .models import Ementa, Escola, Inscricao, Utilizadorparticipante, ParticipanteIndividual, ParticipanteGrupo, \
    EmentaInscricao, Transporteproprio, Atividade, SessaoAtividade, SessaoAtividadeInscricao, Percursos


def remove_all_space(string):
    return string.replace(" ", "")


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, 'home.html')


class InscricaoView(View):
    template_name = 'inscricao.html'

    def get(self, request):
        values = Ementa.objects.all
        escolas = Escola.objects.all
        atividades = Atividade.objects.all
        sessaoatividade = SessaoAtividade.objects.all
        auth_user = request.user
        utilizador = Utilizador.objects.get(pk=auth_user.id)
        today = date.today()
        age = today.year - utilizador.data_nascimento.year - ((today.month, today.day) < (
            utilizador.data_nascimento.month, utilizador.data_nascimento.day
        ))
        return render(request, self.template_name, {
            'values': values,
            'escolas': escolas,
            'atividades': atividades,
            'sessaoatividade': sessaoatividade,
            'auth_user': auth_user,
            'utilizador': utilizador,
            'age': age,
        })

    def post(self, request):
        # ------------escola
        escola_escolhida = request.POST['Escola']
        print(escola_escolhida)
        if escola_escolhida != "Escolher":
            if escola_escolhida == 'others':
                nome = request.POST['nome']
                morada = request.POST['morada']
                codigo_postal = request.POST['codigo_postal']
                contacto = request.POST['contacto']
                localidade = request.POST['localidade']
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
                acompanhantes = request.POST['acompanhantes']
                uploaded_file = request.FILES['myfile']
                print("uploaded_file")
                print(uploaded_file)
                fs = FileSystemStorage()
                fs_saved = 'LES/inscricao/static/autorizacao/inscricao' + \
                           str(inscricao.id)
                fs.save(fs_saved, uploaded_file)
                ParticipanteIndividual.objects.create(autorizacao=0,
                                                      ficheiro_autorizacao=fs_saved,
                                                      acompanhantes=acompanhantes,
                                                      participante=participante,
                                                      )
                participante2 = ParticipanteIndividual.objects.get(participante=participante)
            # ---------refeicao
            n_aluno = request.POST['numero_aluno_normal']
            n_outro = request.POST['numero_outro_normal']
            ementa = Ementa.objects.first()
            EmentaInscricao.objects.create(ementa=ementa, inscricao=inscricao,
                                           numero_aluno_normal=n_aluno,
                                           numero_outro_normal=n_outro
                                           )
            ementainscricao = EmentaInscricao.objects.get(inscricao=inscricao)
            # -----------transporte------------------------------------
            drop_value = request.POST['tipo_transporte']
            trans_para_campus = "nao"
            if drop_value == "autocarro" or drop_value == "comboio":
                trans_para_campus_value = request.POST['QuerTransportePara']
                if trans_para_campus_value == "sim":
                    trans_para_campus = "sim"
            else:
                trans_para_campus = "nao"
            trans_entre_campus_value = request.POST['QuerTransporteEntre']
            if trans_entre_campus_value == 'ida':
                trans_entre_campus = "só ida"
            elif trans_entre_campus_value == 'idavolta':
                trans_entre_campus = "ida e volta"
            else:
                trans_entre_campus = "nao"
            Transporteproprio.objects.create(tipo_transporte=drop_value,
                                             transporte_para_campus=trans_para_campus,
                                             transporte_entre_campus=trans_entre_campus,
                                             inscricao=inscricao
                                             )
            transporte = Transporteproprio.objects.get(inscricao=inscricao)
            chegada = remove_all_space(request.POST['timepicker-one'])
            partida = remove_all_space(request.POST['timepicker-two'])
            entre_campus_ida = remove_all_space(request.POST['timepicker-three'])
            entre_campus_volta = remove_all_space(request.POST['timepicker-four'])
            if drop_value == "autocarro" or drop_value == "comboio":
                trans_para_campus_value = request.POST['QuerTransportePara']
                if trans_para_campus_value == "sim":
                    destino = request.POST['qual']
                    if drop_value == "autocarro":
                        origem = "estacao autocarros"
                    else:
                        origem = "estacao comboios"
                    Percursos.objects.create(origem=origem,
                                             destino=destino,
                                             hora=chegada,
                                             transporteproprio=transporte
                                             )
                    if trans_entre_campus_value == 'ida':
                        if destino == 'penha':
                            destino = 'gambelas'
                        elif destino == 'gambelas':
                            destino = 'penha'
                    Percursos.objects.create(origem=destino,
                                             destino=origem,
                                             hora=partida,
                                             transporteproprio=transporte
                                             )
            origementre = ""
            destinoentre = ""
            if trans_entre_campus_value == 'ida' or trans_entre_campus_value=='idavolta':
                trans_entre_campus = request.POST['transporte_campus']
                if trans_entre_campus == "penha_para_gambelas":
                    origementre = "penha"
                    destinoentre = "gambelas"
                elif trans_entre_campus == "gambelas_para_penha":
                    origementre = "gambelas"
                    destinoentre = "penha"
                Percursos.objects.create(origem=origementre,
                                         destino=destinoentre,
                                         hora=entre_campus_ida,
                                         transporteproprio=transporte
                                         )
                if trans_entre_campus_value=='idavolta':
                    Percursos.objects.create(origem=destinoentre,
                                             destino=origementre,
                                             hora=entre_campus_ida,
                                             transporteproprio=transporte
                                             )
            # ----------------------sessao------------------
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
                        sessaoactividade = SessaoAtividade.objects.get(pk=sessao_actividade_id)
                        SessaoAtividadeInscricao.objects.create(sessaoAtividade=sessaoactividade,
                                                                inscricao=inscricao, numero_alunos=n_inscritos
                                                                )
                        novo_numero_alunos = SessaoAtividade.objects.get(pk=sessao_actividade_id).n_alunos - int(
                            n_inscritos)
                        sessaoactividade.n_alunos = novo_numero_alunos
                        sessaoactividade.save()
                sessao = SessaoAtividadeInscricao.objects.filter(inscricao=inscricao)
                data = {
                    'participante': participante,
                    'utilizador': utilizador,
                    'participantetipo': participante2,  # sem erro, if corre sempre
                    'sessao': sessao,
                    'transporte': transporte,
                    'eminsc': ementainscricao,
                }
                email = EmailMessage()
                email.subject = 'Inscricao Dia Aberto'
                email.body = 'Seguem em anexo um pdf com os dados relativos á sua Inscricao'
                email.from_email = settings.EMAIL_HOST_USER
                email.to = [utilizador.email]
                pdf = render_to_pdf(data)
                # preview------------------comentar para enviar email----------
                # if pdf:
                #     response = HttpResponse(pdf, content_type='application/pdf')
                #     filename = "PrivacyRequest_%s.pdf" % "1234"
                #     content = "inline; filename='%s'" % filename
                #     response['Content-Disposition'] = content
                #     return response
                # ----------------------------------------------------------------
                email.attach('inscricao.pdf', pdf.getvalue(), 'application/pdf')
                email.send()
                return render(request, 'home.html', context={'MSG': "Inscricao com Sucesso"})
            else:
                return render(request, 'home.html', context={'MSG': "Deve de escolher pelo menos uma Sessao"})
        else:
            return render(request, 'home.html', context={'MSG': "Deve de escolher uma Escola"})
