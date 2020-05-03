from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import RegisterForm
from .models import Utilizador, Utilizadortipo, Unidadeorganica, Departamento, UnidadeorganicaDepartamento


class register(View):
    template_name = 'register.html'

    def get(self, request):
        form = RegisterForm()
        utilizadortipo = Utilizadortipo.objects.all
        departamento = Departamento.objects.all
        unidadeorganica = Unidadeorganica.objects.all
        unidadeorganica_dep = UnidadeorganicaDepartamento.objects.all
        return render(request, self.template_name, {
            'form': form,
            'utilizadortipo': utilizadortipo,
            'departamento': departamento,
            'unidadeorganica': unidadeorganica,
            'unidadeorganica_dep': unidadeorganica_dep
        })

    def post(self, request):
        form_register = RegisterForm(request.POST)
        # form_epi = EpiForm()
        # form_prato = PratoForm(request.POST)
        print(form_register.errors)
        if form_register.is_valid():
            # regex = '\w[\w\.-]*@\w[\w\.-]+\.\w+'
            # print("dasd")
            # print(form_register.errors)
            utilizadortipo_value = request.POST['utilizadortipo']
            utilizadortipo = Utilizadortipo.objects.get(tipo=utilizadortipo_value)
            # print(utilizadortipo)
            # print(utilizadortipo_value)
            email = form_register['email'].value()
            print(email)
            password_digest = form_register['password_digest'].value()
            password_conf = form_register['password_conf'].value()
            if password_digest != password_conf:
                messages.error(request, "as passwords não coincidem")
                return redirect('/utilizadores/register/')
            nome = form_register['nome'].value()
            data_nascimento = request.POST['data_nascimento']
            numero_telemovel = form_register['numero_telemovel'].value()
            cartao_cidadao = form_register['cartao_cidadao'].value()
            deficiencias = form_register['deficiencias'].value()
            # permitir_localizacao = form_register['permitir_localizacao'].value()
            permitir_localizacao = request.POST['permitir_localizacao']
            if permitir_localizacao == "sim":
                permitir_localizacao = 1
            else:
                permitir_localizacao = 0
            # utilizar_dados_pessoais = form_register['utilizar_dados_pessoais'].value()
            utilizar_dados_pessoais = request.POST['utilizar_dados_pessoais']
            if utilizar_dados_pessoais == "sim":
                utilizar_dados_pessoais = 1
            else:
                utilizar_dados_pessoais = 0

            print(utilizadortipo_value)
            if utilizadortipo_value == "Participante Individual" or utilizadortipo_value == "Participante em Grupo":
                unidadeorganica = None
                departamento = None
            else:
                unidadeorganica1 = request.POST['unidadeorganica']
                print(unidadeorganica1)
                unidadeorganica = Unidadeorganica.objects.get(nome=unidadeorganica1)
                if unidadeorganica1 == "Escola Superior de Gestão, Hotelaria e Turismo" or unidadeorganica1 == "Faculdade de Economia" or unidadeorganica1 == "Departamento de Ciências Biomédicas e Medicina":
                    departamento = None
                    print("noneeeee")
                else:
                    departamento = request.POST['departamento']
                    print(departamento)
                    departamento = Departamento.objects.get(nome=departamento)

            print(unidadeorganica)
            #departamento = request.POST['departamento']
            print(departamento)
            #unidadeorganica = Unidadeorganica.objects.get(nome=unidadeorganica)
            #departamento = request.POST['departamento']
           # departamento = Departamento.objects.get(nome=departamento)

            User.objects.create_user(username=email, password=password_digest)
            Utilizador.objects.create(utilizadortipo=utilizadortipo, email=email,
                                      nome=nome, data_nascimento=data_nascimento, numero_telemovel=numero_telemovel,
                                      cartao_cidadao=cartao_cidadao, deficiencias=deficiencias,
                                      permitir_localizacao=permitir_localizacao,
                                      utilizar_dados_pessoais=utilizar_dados_pessoais,
                                      unidadeorganica=unidadeorganica, departamento=departamento)
            """escola = Escola.objects.get(nome=nome)
            Inscricao.objects.create(escola=escola)
            inscricao = Inscricao.objects.get(escola=escola)

            if form_prato.is_valid():
                radio_value = form_prato.cleaned_data.get("prato")
                prato = Prato.objects.get(tipo=radio_value)

                ementa = Ementa.objects.all().first()
                EmentaPratoInscricao.objects.create(ementa=ementa, prato=prato, inscricao=inscricao)

            return redirect('/inscricao/home')"""
        return redirect('/utilizadores/login')


def logout_request(request):
    logout(request)
    messages.info(request, "Terminou a sessão com sucesso")
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
                return redirect('/utilizadores/success')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Email ou Password inválida")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})


def success(request):
    context = {}
    context['user'] = request.user
    return render(request=request,
                  template_name="success.html",
                  context={})

#  def password_change(request):
#   if request.method == 'POST':
#      form = PasswordChangeForm(request.user, request.POST)
#     if form.is_valid():
#        user = form.save()
#       update_session_auth_hash(request, user)
#      messages.success(request, 'Your password was successfully updated!')
#     return redirect('change_password')
# else:
#   messages.error(request, 'Please correct the error below.')
#   else:
#      form = PasswordChangeForm(request.user)
# return render(request, 'password_change.html', {
#    'form': form
# })
#
# def password_change_done(request):
# messages.info(request, "Password changed")
# return render(request, 'password_change_done.html')
#