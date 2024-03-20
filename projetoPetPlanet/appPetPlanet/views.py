from django.shortcuts import render
from .models import Cliente
from .models import Pet
from .gerarPet import gerarDadosPet
from .gerarPessoa import gerarDadosCliente
import sqlite3


# Função temporária, para debug
def limparBD(request):
    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_cliente WHERE id_cliente>1')
    bd.commit()
    bd.close()
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')

# FUNÇÕES CLIENTE


def cadastrarCliente(request):
    return render(request, 'cliente/cadastrarCliente.html')


def preencherDadosCliente(request):
    args = gerarDadosCliente()
    return render(request, 'cliente/cadastrarCliente.html', args)


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

# FUNÇÕES DO PET


def cadastrarPet(request):
    return render(request, 'pet/cadastrarPet.html')


def salvarNovoPetNoBD(request):
    pet = Pet()
    pet.nome = request.POST.get('nome')
    pet.especie = request.POST.get('especie')
    pet.raca = request.POST.get('raca')
    pet.idade = request.POST.get('idade')
    pet.sexo = request.POST.get('sexo')
    pet.porte = request.POST.get('porte')
    pet.alergias = request.POST.get('alergias')
    pet.save()
    return render(request, 'pet/cadastrarPet.html')


def listarPets(request):
    pets = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pet/listarPets.html', pets)


def infoPet(request, IDPet):
    pet = Pet.objects.get(id_pet=IDPet)
    return render(request, 'pet/infoPet.html', {'pet': pet})


def excluirPetDB(request, IDPet):
    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_pet WHERE id_pet='+str(IDPet))
    bd.commit()
    bd.close()
    pets = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pet/listarPets.html', pets)


def preencherDadosPet(request):
    args = gerarDadosPet()
    return render(request, 'pet/cadastrarPet.html', args)
