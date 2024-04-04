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
    # urls essenciais
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),

    # url debug
    path('botaoDebug/', views.botaoDebug, name='botaoDebug'),

    # urls cliente
    path('cadastrarCliente/', views.cadastrarCliente,
         name='cadastrarCliente'),
    path('cadastrarCliente/pd/', views.preencherDadosCliente,
         name='preencherDadosCliente'),
    path('listarClientes/', views.listarClientes, name='listarClientes'),
    path('salvarNovoClienteNoBD/', views.salvarNovoClienteNoBD,
         name='salvarNovoClienteNoBD'),
    path('editarClienteNoDB/',
         views.editarClienteNoDB, name='editarClienteNoDB'),
    path('editarClienteNoDB/<int:IDCliente>',
         views.editarClienteNoDB, name='editarClienteNoDB'),
    path('excluirClienteDoBD/',
         views.excluirClienteDoBD, name='excluirClienteDoBD'),
    path('excluirClienteDoBD/<int:IDCliente>/',
         views.excluirClienteDoBD, name='excluirClienteDoBD'),
    path('infoCliente/', views.infoCliente, name='infoCliente'),
    path('infoCliente/<int:IDCliente>/',
         views.infoCliente, name='infoCliente'),


    # urls pet
    path('cadastrarPet/', views.cadastrarPet, name='cadastrarPet'),
    path('cadastrarPet/pd/', views.preencherDadosPet, name='preencherDadosPet'),
    path('listarPets/', views.listarPets, name='listarPets'),
    path('salvarNovoPetNoDB/', views.salvarNovoPetNoBD, name='salvarNovoPetNoDB'),
    path('editarPetNoDB/', views.editarPetNoDB, name='editarPetNoDB'),
    path('editarPetNoDB/<int:IDPet>',
         views.editarPetNoDB, name='editarPetNoDB'),
    path('infoPet/', views.infoPet, name='infoPet'),
    path('infoPet/<int:IDPet>/', views.infoPet, name='infoPet'),
    path('excluirPetDB/', views.excluirPetDB, name='excluirPetDB'),
    path('excluirPetDB/<int:IDPet>/', views.excluirPetDB, name='excluirPetDB'),


    # urls funcionario
    path('cadastrarFuncionario/', views.cadastrarFuncionario,
         name='cadastrarFuncionario'),
    path('cadastrarFuncionario/pd/', views.preencherDadosFuncionario,
         name='preencherDadosFuncionario'),
    path('listarFuncionarios/', views.listarFuncionarios,
         name='listarFuncionarios'),
    path('salvarNovoFuncionarioNoDB/', views.salvarNovoFuncionarioNoDB,
         name='salvarNovoFuncionarioNoDB'),
    path('editarFuncionarioNoDB/', views.editarFuncionarioNoDB,
         name='editarFuncionarioNoDB'),
    path('editarFuncionarioNoDB/<int:IDFuncionario>',
         views.editarFuncionarioNoDB, name='editarFuncionarioNoDB'),
    path('infoFuncionario/', views.infoFuncionario, name='infoFuncionario'),
    path('infoFuncionario/<int:IDFuncionario>/',
         views.infoFuncionario, name='infoFuncionario'),
    path('excluirFuncionarioDoDB/', views.excluirFuncionarioDoDB,
         name='excluirFuncionarioDoDB'),
    path('excluirFuncionarioDoDB/<int:IDFuncionario>/',
         views.excluirFuncionarioDoDB, name='excluirFuncionarioDoDB'),

    # urls produtos
    path('cadastrarProduto/', views.cadastrarProduto,
         name='cadastrarProduto'),
    path('salvarNovoProdutoNoDB/', views.salvarNovoProdutoNoDB,
         name='salvarNovoProdutoNoDB'),
    path('listarProdutos/', views.listarProdutos,
         name='listarProdutos'),
    path('infoProduto/', views.infoProduto, name='infoProduto'),
    path('infoProduto/<int:IDProduto>/',
         views.infoProduto, name='infoProduto'),
    path('excluirProdutoDoDB/', views.excluirProdutoDoDB,
         name='excluirProdutoDoDB'),
    path('excluirProdutoDoDB/<int:IDProduto>/',
         views.excluirProdutoDoDB, name='excluirProdutoDoDB'),
    path('editarProdutoNoDB/', views.editarProdutoNoDB,
         name='editarProdutoNoDB'),
    path('editarProdutoNoDB/<int:IDProduto>',
         views.editarProdutoNoDB, name='editarProdutoNoDB'),

    # urls serviços
    path('gerarServico/', views.gerarServico, name='gerarServico'),
    path('gerarServicoFiltrandoPet/',
         views.gerarServicoFiltrandoPet, name='gerarServicoFiltrandoPet'),
    path('gerarServicoFiltrandoPet/<int:IDDono>',
         views.gerarServicoFiltrandoPet, name='gerarServicoFiltrandoPet'),
    path('salvarServicoGeradoNoDB/', views.salvarServicoGeradoNoDB,
         name='salvarServicoGeradoNoDB'),
    path('listarAgenda/', views.listarAgenda, name='listarAgenda'),
    path('excluirServicoDoDB/', views.excluirServicoDoDB,
         name='excluirServicoDoDB'),
    path('excluirServicoDoDB/<int:IDServico>', views.excluirServicoDoDB,
         name='excluirServicoDoDB'),

    # urls vendas
    path('novaVenda/', views.novaVenda, name='novaVenda'),
    path('novaVenda/getDadosProduto/<int:IDProduto>',
         views.getDadosProduto, name='getDadosProduto'),
    path('concluirVenda/', views.concluirVenda, name='concluirVenda'),
    path('concluirVenda/<int:idCliente>/<str:jsonProdutos>/<int:idVendedor>/<str:formaPagamento>/<str:datahora>',
         views.concluirVenda, name='concluirVenda'),
]
