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

app_name = "utilizadores"

urlpatterns = [
    path("register/", views.register, name='register'),
    path("logout", views.logout, name="logout"),
    path("login/", views.login, name="login"),
    path("password_change/", views.password_change, name="password-change"),
    path("password_change_done/", views.password_change_done, name="password-change-done"),



]
