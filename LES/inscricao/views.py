from django.shortcuts import render, redirect
from .models import Inscricao, Escola
from .forms import InscricaoForm

'''
 def view_inscricao(request):
    newinscricao = inscricaoForm()
    return render(request=request,
               template_name="inscricao.html",
                )
 '''


def create_inscricao(request):
    form = InscricaoForm(request.POST)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'inscricao.html', context)
