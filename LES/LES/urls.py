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

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    #  path('', include('Dia_Aberto.urls')),
    path('admin/', admin.site.urls),
    path('inscricao/', include('inscricao.urls')),
    path('utilizadores/', include('utilizadores.urls')),
    path('notificacao/', include('notificacao.urls')),
    path('colaboradores/', include('colaboradores.urls')),
    path('notificacao/', include('notificacao.urls')),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form1.html',
                                                                 html_email_template_name='registration/password_reset_email1.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done1.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm1.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete1.html'),
         name='password_reset_complete'),

]
