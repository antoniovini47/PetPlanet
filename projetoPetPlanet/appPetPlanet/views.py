from django.shortcuts import render
from .models import Cliente
from .gerarNomePet import gerarNomePet
from .gerarPessoa import gerarDadosCliente
import sqlite3


def home(request):
    return render(request, 'home.html')


def cadastrarCliente(request):
    return render(request, 'cliente/cadastrarCliente.html')


def preencherDadosCliente(request):
    args = gerarDadosCliente()
    return render(request, 'cliente/cadastrarCliente.html', args)


def limparBD(request):
    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_cliente WHERE id_cliente>1')
    bd.commit()
    bd.close()
    return render(request, 'home.html')


def salvarNovoClienteNoBD(request):
    cliente = Cliente()
    cliente.nome = request.POST.get('nome')
    cliente.cpf = request.POST.get('cpf')
    cliente.email = request.POST.get('email')
    cliente.telefone = request.POST.get('telefone')
    cliente.endereco = request.POST.get('endereco')
    cliente.save()
    return render(request, 'cliente/cadastrarCliente.html')


def excluirClienteDoBD(request, IDCliente):
    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_cliente WHERE id_cliente='+str(IDCliente))
    bd.commit()
    bd.close()
    clientes = {
        'clientes': Cliente.objects.all()
    }
    return render(request, 'cliente/listarClientes.html', clientes)


def listarClientes(request):
    clientes = {
        'clientes': Cliente.objects.all()
    }
    return render(request, 'cliente/listarClientes.html', clientes)


def infoCliente(request, IDCliente):
    cliente = Cliente.objects.get(id_cliente=IDCliente)
    return render(request, 'cliente/infoCliente.html', {'cliente': cliente})


def preencherDadosPet(request):
    nomePet = gerarNomePet()
    return render(request, 'pet/cadastrarPet.html', nomePet)
