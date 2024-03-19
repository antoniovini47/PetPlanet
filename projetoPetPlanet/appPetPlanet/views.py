from django.shortcuts import render
from .models import Cliente
import sqlite3
import requests
import json


def home(request):
    return render(request, 'home.html')


def cadastrarCliente(request):
    return render(request, 'cliente/cadastrarCliente.html')


def preencherDadosCliente(request):
    url = 'https://www.4devs.com.br/ferramentas_online.php'
    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.4devs.com.br',
        'referer': 'https://www.4devs.com.br/gerador_de_pessoas',
    }
    data = 'acao=gerar_pessoa&sexo=I&pontuacao=S&idade=0&cep_estado=&txt_qtde=1&cep_cidade='
    solicitacao = requests.post(url, headers=header, data=data).json()

    # Convertendo 'solicitação' para uma String json
    dadosBrutos = json.dumps(solicitacao)
    # removendo os caracteres "[" e "]" para transformar cada item em um objeto json e não todos em uma única lista
    dadosBrutos = dadosBrutos.replace("[", "")
    dadosBrutos = dadosBrutos.replace("]", "")
    # retornando para json
    dadosPessoa = json.loads(dadosBrutos)

    # Passando os argumentos
    args = {
        'nomeCliente': dadosPessoa['nome'],
        'cpfCliente': dadosPessoa['cpf'],
        'emailCliente': dadosPessoa['email'],
        'telefoneCliente': dadosPessoa['celular'],
        'enderecoCliente': dadosPessoa['endereco'],
        'numeroCliente': dadosPessoa['numero'],
        'bairroCliente': dadosPessoa['bairro'],
        'cidadeCliente': dadosPessoa['cidade'],
        'estadoCliente': dadosPessoa['estado'],
        'enderecoCompletoCliente': str(dadosPessoa['endereco']) + ", "
        + str(dadosPessoa['numero']) + ", "
        + str(dadosPessoa['bairro']) + ", "
        + str(dadosPessoa['cidade']) + " - "
        + str(dadosPessoa['estado']),
    }
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
