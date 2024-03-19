"""
URL configuration for projetoPetPlanet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from appPetPlanet import views

urlpatterns = [
    # rota, view responsável, nome de referencia
    path('', views.home, name='home'),

    path('cadastrarCliente/', views.cadastrarCliente,
         name='cadastrarCliente'),

    path('cadastrarCliente/pdc', views.preencherDadosCliente,
         name='preencherDadosCliente'),

    path('listarClientes/', views.listarClientes, name='listarClientes'),

    path('salvarNovoClienteNoBD/', views.salvarNovoClienteNoBD,
         name='salvarNovoClienteNoBD'),

    path('excluirClienteDoBD/',
         views.excluirClienteDoBD, name='excluirClienteDoBD'),
    path('excluirClienteDoBD/<int:IDCliente>/',
         views.excluirClienteDoBD, name='excluirClienteDoBD'),

    path('limparBD/', views.limparBD, name='limparBD'),


    path('infoCliente/', views.infoCliente, name='infoCliente'),
    path('infoCliente/<int:IDCliente>/',
         views.infoCliente, name='infoCliente'),
]
