from django.shortcuts import render
from .models import Inscricao


def inscricao_prof(request):
    return render(request=request,
                  template_name="inscricao.html",
                  context={"inscricao": Inscricao.objects.all}
                  )
