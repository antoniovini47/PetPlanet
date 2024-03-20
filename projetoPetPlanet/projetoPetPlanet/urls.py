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
from django.contrib import admin
from appPetPlanet import views

urlpatterns = [
    # url temporaria, para debug
    path('limparBD/', views.limparBD, name='limparBD'),

    # urls essenciais
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),

    # urls cliente
    path('cadastrarCliente/', views.cadastrarCliente,
         name='cadastrarCliente'),
    path('cadastrarCliente/pd/', views.preencherDadosCliente,
         name='preencherDadosCliente'),
    path('listarClientes/', views.listarClientes, name='listarClientes'),
    path('salvarNovoClienteNoBD/', views.salvarNovoClienteNoBD,
         name='salvarNovoClienteNoBD'),
    path('excluirClienteDoBD/',
         views.excluirClienteDoBD, name='excluirClienteDoBD'),
    path('excluirClienteDoBD/<int:IDCliente>/',
         views.excluirClienteDoBD, name='excluirClienteDoBD'),
    path('infoCliente/', views.infoCliente, name='infoCliente'),
    path('infoCliente/<int:IDCliente>/',
         views.infoCliente, name='infoCliente'),


    # urls pet
    path('cadastrarPet/', views.cadastrarPet, name='cadastrarPet'),
    path('cadastrarPet/pd/', views.cadastrarPet, name='preencherDadosPet'),
    path('listarPets/', views.listarPets, name='listarPets'),
    path('salvarNovoPetNoDB/', views.salvarNovoPetNoBD, name='salvarNovoPetNoDB'),
    path('infoPet/', views.infoPet, name='infoPet'),
    path('infoPet/<int:IDPet>/', views.infoPet, name='infoPet'),
    path('excluirPetDB/', views.excluirPetDB, name='excluirPetDB'),
    path('excluirPetDB/<int:IDPet>/', views.excluirPetDB, name='excluirPetDB'),
]
