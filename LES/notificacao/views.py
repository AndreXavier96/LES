from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.views.generic import View
from .forms import NotificacaoForm
from .models import Notificacao, Utilizador, Utilizadortipo


class notificacao(View):
    template_name = 'notificacao.html'
    def get(self, request):
        form = NotificacaoForm()
        # ---------------get autenticated user
        auth_user = request.user
        utilizador_env = Utilizador.objects.get(pk=auth_user.id)
        # ----------------------
        return render(request, self.template_name, {
                                                    'form': form,
                                                    'utilizador_env': utilizador_env
                                                    })
    def post(self, request):
        form_notificacao = NotificacaoForm(request.POST)
        print(form_notificacao.errors)
        if form_notificacao.is_valid():
            print('asd')
            assunto = form_notificacao['assunto'].value()
            conteudo = form_notificacao['conteudo'].value()
            hora = datetime.now()
            prioridade = form_notificacao['prioridade'].value()
            #utilizador_env = form_notificacao['utilizador_env'].value()
            auth_user = request.user
            utilizador_env = Utilizador.objects.get(pk=auth_user.id)
            #utilizador_env = Utilizador.objects.get(pk=1)
            #utilizador_env_value = form_notificacao.cleaned_data.get("utilizador_env")
            #print(utilizador_env_value)
            #utilizador_env = Utilizador.objects.get(nome=utilizador_env_value)
            utilizador_rec= form_notificacao['utilizador_rec'].value()
            utilizador_rec1 = Utilizador.objects.get(email=utilizador_rec)
            teste = form_notificacao['teste'].value()
            if len(teste)!=0:
                print("1,2")
                print(teste)
                id_u= Utilizadortipo.objects.get(tipo=teste)
                print(id_u)
                teste1=Utilizador.objects.all().filter(utilizadortipo=id_u)
                print(teste1)
                for x in teste1:
                    print(x)
                    Notificacao.objects.create(assunto=assunto, conteudo=conteudo, hora=hora,
                                           prioridade=prioridade, utilizador_env=utilizador_env,
                                           utilizador_rec=x)
            #teste1= Utilizador.objects.get(utilizadortipo=id_u)
            else:
                Notificacao.objects.create(assunto=assunto, conteudo=conteudo, hora=hora,
                                       prioridade=prioridade, utilizador_env=utilizador_env,
                                       utilizador_rec=utilizador_rec1)
        return redirect('/notificacao')

