from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Utilizador
from .forms import Criar_Colab_Form

class Criar_colab(View):
    template_name = 'criar_colaboracao.html'
    def get(self, request):
        form = Criar_Colab_Form()
        return render(request, self.template_name, {
                                                    'form': form,
                                                    })
    def post(self, request):
        form_colab = Criar_Colab_Form(request.POST)

        # form_epi = EpiForm()
        #form_prato = PratoForm(request.POST)
        #print(form_register.errors)
        if form_colab.is_valid():
            primeiro_dia = form_colab['primeiro_dia'].value()
            segundo_dia = form_colab['segundo_dia'].value()
            sala_de_aula = form_colab['sala_de_aula'].value()
            percurso = form_colab['percurso'].value()

        Utilizador.objects.filter(pk=5).update(primeiro_dia=primeiro_dia, segundo_dia=segundo_dia,
                                                        sala_de_aula=sala_de_aula, percurso=percurso)

        return redirect('/register')


''' Utilizadortipo.objects.create(primeiro_dia=primeiro_dia, segundo_dia=segundo_dia,
                               sala_de_aula=sala_de_aula, percurso=percurso)'''

