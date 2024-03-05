from django.shortcuts import render
from .models import Cliente

def cadastrarCliente(request):
    return render(request, 'cliente/cadastrarCliente.html')

def listarClientes(request):
    #Criar e salvar novo cliente
    cliente = Cliente()
    cliente.nome = request.POST.get('nome')
    cliente.cpf = request.POST.get('cpf')
    cliente.email = request.POST.get('email')
    cliente.telefone = request.POST.get('telefone')
    cliente.endereco = request.POST.get('endereco')
    cliente.save()

    clientes = {
        'clientes': Cliente.objects.all()
    }

    return render(request, 'cliente/listarClientes.html', clientes)