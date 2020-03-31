from django.shortcuts import render
from .models import Inscricao, Escola


def escola(request):
    return render(request=request,
                  template_name="inscricao.html",
                  context={"escolas": Escola.objects.all}
                  )
