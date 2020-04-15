from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import RegisterForm
from django.contrib import messages
from django.views.generic import View
from .models import Utilizador, Utilizadortipo, Unidadeorganica
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/utilizadores/login')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/utilizadores/success')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})


def success(request):
    context = {}
    context['user'] = request.user
    return render(request = request,
                    template_name = "success.html",
                    context={})

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {
        'form': form
    })

def password_change_done(request):
    messages.info(request, "Password changed")
    return render(request, 'password_change_done.html')
