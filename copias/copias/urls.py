"""copias URL Configuration

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
from django.urls import path
from django.contrib.auth import views as auth_views

from core.views import home, fechamento_de_caixa, resumo, remover_caixa, entrar, dashboard, logout_admin, remover_caixa_resumo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('resumo/', resumo, name='resumo'),
    path('remover-caixa/<int:pk>/', remover_caixa ,name='remover_caixa'),
    path('remover-caixa-resumo/<int:pk>/', remover_caixa_resumo ,name='remover_caixa_resumo'),


    path('entrar/', entrar, name='entrar'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout-admin/', logout_admin, name='logout_admin'),
    path('fechamento-caixa',fechamento_de_caixa, name="fechamento_de_caixa"),

]
