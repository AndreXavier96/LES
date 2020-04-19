"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from .views import register





urlpatterns = [

    path('admin/', admin.site.urls),
    path("register/", register.as_view(), name='add'),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("success/", views.success, name="success"),

        # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
        path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done1.html'),
            name='password_change_done'),

        path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
            name='password_change'),

        path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done1.html'),
         name='password_reset_done'),

        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm1.html'), name='password_reset_confirm'),
        path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form1.html'), name='password_reset'),

        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete1.html'),
         name='password_reset_complete'),
    ]



