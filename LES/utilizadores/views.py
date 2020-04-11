from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import RegisterForm
from django.contrib import messages
from django.views.generic import View
from .models import Utilizador, Utilizadortipo, Unidadeorganica

class register(View):
    template_name = 'register.html'
    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {
                                                    'form': form,
                                                    })
    def post(self, request):
        form_register = RegisterForm(request.POST)

        # form_epi = EpiForm()
        #form_prato = PratoForm(request.POST)
        print(form_register.errors)
        if form_register.is_valid():
            print("dasd")
            print(form_register.errors)
            utilizadortipo_value = form_register.cleaned_data.get("utilizadortipo")
            utilizadortipo = Utilizadortipo.objects.get(tipo=utilizadortipo_value)
            print(utilizadortipo)
            print(utilizadortipo_value)
            email = form_register['email'].value()
            password_digest = form_register['password_digest'].value()
            nome = form_register['nome'].value()
            data_nascimento = form_register['data_nascimento'].value()
            numero_telemovel = form_register['numero_telemovel'].value()
            cartao_cidadao = form_register['cartao_cidadao'].value()
            deficiencias = form_register['deficiencias'].value()
            permitir_localizacao = form_register['permitir_localizacao'].value()
            utilizar_dados_pessoais = form_register['utilizar_dados_pessoais'].value()
            unidadeorganica_value = form_register.cleaned_data.get("unidadeorganica")
            print(unidadeorganica_value)
            unidadeorganica = Unidadeorganica.objects.get(nome=unidadeorganica_value)

            Utilizador.objects.create(utilizadortipo=utilizadortipo, email=email, password_digest=password_digest,
                                      nome=nome, data_nascimento=data_nascimento, numero_telemovel=numero_telemovel,
                                      cartao_cidadao=cartao_cidadao, deficiencias=deficiencias,
                                      permitir_localizacao=permitir_localizacao,
                                      utilizar_dados_pessoais=utilizar_dados_pessoais,
                                       unidadeorganica=unidadeorganica)
            """escola = Escola.objects.get(nome=nome)

            Inscricao.objects.create(escola=escola)
            inscricao = Inscricao.objects.get(escola=escola)

            if form_prato.is_valid():
                radio_value = form_prato.cleaned_data.get("prato")
                prato = Prato.objects.get(tipo=radio_value)

                ementa = Ementa.objects.all().first()
                EmentaPratoInscricao.objects.create(ementa=ementa, prato=prato, inscricao=inscricao)

            return redirect('/inscricao/home')"""
        return redirect('/register')