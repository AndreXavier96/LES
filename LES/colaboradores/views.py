from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Utilizador
#from .forms import Criar_Colab_Form, Editar_Colab_From


class Criar_colab(View):
    template_name = 'criar_colaboracao.html'
    def get(self, request):
        #form = Criar_Colab_Form()
        return render(request, self.template_name, {
                                                    #'form': form,
                                                    })
    def post(self, request):
        '''form_colab = Criar_Colab_Form(request.POST)
        #print(form_register.errors)
        if form_colab.is_valid():
            primeiro_dia = form_colab['primeiro_dia'].value()
            segundo_dia = form_colab['segundo_dia'].value()
            sala_de_aula = form_colab['sala_de_aula'].value()
            percurso = form_colab['percurso'].value()'''
        primeiro_dia = request.POST['primeiro_dia']
        segundo_dia = request.POST['segundo_dia']
        sala_de_aula = request.POST['sala_de_aula']
        percurso = request.POST['percurso']
        if primeiro_dia == "sim":
            primeiro_dia = 1
        else:
            primeiro_dia = 0

        if segundo_dia == "sim":
            segundo_dia = 1
        else:
            segundo_dia = 0

        if sala_de_aula == "sim":
            sala_de_aula = 1
        else:
            sala_de_aula = 0

        if percurso == "sim":
            percurso = 1
        else:
            percurso = 0
        '''if form_colab.is_valid():
            primeiro_dia = form_colab['primeiro_dia'].value()
            segundo_dia = form_colab['segundo_dia'].value()
            sala_de_aula = form_colab['sala_de_aula'].value()
            percurso = form_colab['percurso'].value()
        '''
        Utilizador.objects.filter(pk=3).update(primeiro_dia=primeiro_dia, segundo_dia=segundo_dia,
                                               sala_de_aula=sala_de_aula, percurso=percurso)

        return redirect('/register')

class Editar_colab(View):
    template_name = 'editar_colaboracao.html'
    def get(self,request):
        obj = Utilizador.objects.get(pk=3)
        #form = Editar_Colab_Form()
        #form = Editar_Colab_Form(instance=Utilizador.objects.get(pk=3))
        return render(request,self.template_name, {
                                                    #'form': form,
                                                    'obj': obj,
                                                    })
    def post(self, request):
        primeiro_dia = request.POST['primeiro_dia']
        segundo_dia = request.POST['segundo_dia']
        sala_de_aula = request.POST['sala_de_aula']
        percurso = request.POST['percurso']
        if primeiro_dia == "sim":
            primeiro_dia = 1
        else:
            primeiro_dia = 0

        if segundo_dia == "sim":
            segundo_dia = 1
        else:
            segundo_dia = 0

        if sala_de_aula == "sim":
            sala_de_aula = 1
        else:
            sala_de_aula = 0

        if percurso == "sim":
            percurso = 1
        else:
            percurso = 0
        '''if form_colab.is_valid():
            primeiro_dia = form_colab['primeiro_dia'].value()
            segundo_dia = form_colab['segundo_dia'].value()
            sala_de_aula = form_colab['sala_de_aula'].value()
            percurso = form_colab['percurso'].value()
        '''
        Utilizador.objects.filter(pk=3).update(primeiro_dia=primeiro_dia, segundo_dia=segundo_dia,
                                                        sala_de_aula=sala_de_aula, percurso=percurso)

        return redirect('/register')


