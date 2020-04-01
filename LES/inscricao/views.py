from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import EscolaForm, EpiForm, PratoForm
from .models import Prato, Ementa, Escola, Inscricao, EmentaPratoInscricao


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        return render()


class InscricaoView(View):
    template_name = 'inscricao.html'

    def get(self, request):
        # form_escola = EscolaForm()
        # form_epi = EpiForm()
        form = PratoForm()
        form2 = EscolaForm()
        return render(request, self.template_name, {'pratos': Prato.objects.all,
                                                    'ementas': Ementa.objects.all,
                                                    'form': form,
                                                    # 'epis': form_epi,
                                                    'form2': form2,
                                                    })

    def post(self, request):
        form_escola = EscolaForm(request.POST)

        # form_epi = EpiForm()
        form_prato = PratoForm(request.POST)
        if form_escola.is_valid():
            nome = form_escola['nome'].value()
            morada = form_escola['morada'].value()
            codigo_postal = form_escola['codigo_postal'].value()
            contacto = form_escola['contacto'].value()
            localidade = form_escola['localidade'].value()
            Escola.objects.create(nome=nome, morada=morada, codigo_postal=codigo_postal, contacto=contacto,
                                  localidade=localidade)
            escola = Escola.objects.get(nome=nome)

            Inscricao.objects.create(escola=escola)
            inscricao = Inscricao.objects.get(escola=escola)

            if form_prato.is_valid():
                radio_value = form_prato.cleaned_data.get("prato")
                prato = Prato.objects.get(tipo=radio_value)

                ementa = Ementa.objects.all().first()
                EmentaPratoInscricao.objects.create(ementa=ementa, prato=prato, inscricao=inscricao)

            return redirect('/inscricao/home')
        return redirect('/inscricao')

        # elif "price" in request.POST:
        # products_query = Product.objects.filter(categoria=category_title_Query).order_by('price')

        # -----------------------------------------------
        # if form_escola.is_valid(): # and form_epi.is_valid():
        # form_escola.save()
        # instance = form_epi.save(commit=False)
        # instance.ementa = '1'
        # instance.prato = '1'
        # instance.inscricao = '1'
        #     return redirect('/home')
        # return redirect('/inscricao')


'''def create_inscricao(request):
    form_escola = EscolaForm(request.POST or None)
    # form_prato = PratoForm(request.POST)
    if form_escola.is_valid():
        form_escola.save()
    #  if form_prato.is_valid():
    #    form_prato.save()
    # var = request.POST.getlist('tipos')
    context = {
        'form_escola': form_escola,
        # 'form_prato': form_prato
        'pratos': Prato.objects.all,
    }
    return render(request, 'inscricao.html', context)'''
