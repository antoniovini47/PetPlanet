from django.shortcuts import render
from .models import Cliente
import sqlite3


def home(request):
    return render(request, 'home.html')


def cadastrarCliente(request):
    return render(request, 'cliente/cadastrarCliente.html')


def limparBD(request):
    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_cliente WHERE cpf = 45679812345')
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


def listarClientes(request):
    clientes = {
        'clientes': Cliente.objects.all()
    }
    return render(request, 'cliente/listarClientes.html', clientes)
