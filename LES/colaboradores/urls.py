"""
LES URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from .views import register
from .views import Criar_colab, Editar_colab

app_name = "colaboradores"

urlpatterns = [
    path("criar_colab/", Criar_colab.as_view(), name='criar_colab'),
    path("editar_colab/", Editar_colab.as_view(), name='editar_colab'),
]
