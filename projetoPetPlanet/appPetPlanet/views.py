from django.shortcuts import render
from django.http import JsonResponse
from .models import Cliente
from .models import Pet
from .models import Funcionario
from .models import Produto
from .models import Servico
from .models import Venda
from .gerarPet import gerarDadosPet
from .gerarPessoa import gerarDadosCliente
import sqlite3
import random

# DEBUG


def botaoDebug(request):
    # Cria funções temporárias para testes e correções de bugs

    teste = Venda.objects.get(id_venda=1)
    print(teste.itens)

    print("Botão executado com sucesso")
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


def editarClienteNoDB(request, IDCliente):
    cliente = Cliente()
    cliente.nome = request.POST.get('nome')
    cliente.cpf = request.POST.get('cpf')
    cliente.email = request.POST.get('email')
    cliente.telefone = request.POST.get('telefone')
    cliente.endereco = request.POST.get('endereco')

    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute("UPDATE appPetPlanet_cliente SET nome='" +
                   str(cliente.nome) + "' WHERE id_cliente=" + str(IDCliente))
    cursor.execute("UPDATE appPetPlanet_cliente SET cpf='" +
                   str(cliente.cpf) + "' WHERE id_cliente=" + str(IDCliente))
    cursor.execute("UPDATE appPetPlanet_cliente SET email='" +
                   str(cliente.email) + "' WHERE id_cliente=" + str(IDCliente))
    cursor.execute("UPDATE appPetPlanet_cliente SET telefone='" +
                   str(cliente.telefone) + "' WHERE id_cliente=" + str(IDCliente))
    cursor.execute("UPDATE appPetPlanet_cliente SET endereco='" +
                   str(cliente.endereco) + "' WHERE id_cliente=" + str(IDCliente))
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
    pets = Pet.objects.filter(id_dono=IDCliente)
    args = {
        'cliente': cliente,
        'pets': pets,
    }
    return render(request, 'cliente/infoCliente.html', args)

# FUNÇÕES DO PET


def cadastrarPet(request):
    clientes = {
        'clientes': Cliente.objects.all()
    }
    return render(request, 'pet/cadastrarPet.html', clientes)


def salvarNovoPetNoBD(request):
    pet = Pet()
    pet.nome = request.POST.get('nome')
    pet.especie = request.POST.get('especie')
    pet.raca = request.POST.get('raca')
    pet.idade = request.POST.get('idade')
    pet.sexo = request.POST.get('sexo')
    pet.porte = request.POST.get('porte')
    pet.alergias = request.POST.get('alergias')
    pet.id_dono = request.POST.get('dono')
    pet.save()
    return render(request, 'pet/cadastrarPet.html')


def listarPets(request):
    pets = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pet/listarPets.html', pets)


def infoPet(request, IDPet):
    pet = Pet.objects.get(id_pet=IDPet)
    try:
        dono = Cliente.objects.get(id_cliente=pet.id_dono)
    except Cliente.DoesNotExist:
        dono = Cliente()
        dono.nome = "Sem dono definido"
    args = {
        'pet': pet,
        'dono': dono,
        'clientes': Cliente.objects.all(),
    }
    return render(request, 'pet/infoPet.html', args)


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


def editarPetNoDB(request, IDPet):
    pet = Pet()
    pet.nome = request.POST.get('nome')
    pet.especie = request.POST.get('especie')
    pet.raca = request.POST.get('raca')
    pet.idade = request.POST.get('idade')
    pet.sexo = request.POST.get('sexo')
    pet.porte = request.POST.get('porte')
    pet.alergias = request.POST.get('alergias')
    pet.id_dono = request.POST.get('dono')

    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute("UPDATE appPetPlanet_pet SET nome='" +
                   str(pet.nome) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET especie='" +
                   str(pet.especie) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET raca='" +
                   str(pet.raca) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET idade='" +
                   str(pet.idade) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET sexo='" +
                   str(pet.sexo) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET porte='" +
                   str(pet.porte) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET alergias='" +
                   str(pet.alergias) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET id_dono='" +
                   str(pet.id_dono) + "' WHERE id_pet=" + str(IDPet))

    bd.commit()
    bd.close()

    pets = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pet/listarPets.html', pets)


def preencherDadosPet(request):
    args = gerarDadosPet()
    args.update({'clientes': Cliente.objects.all()})
    return render(request, 'pet/cadastrarPet.html', args)

# FUNÇÕES DO FUNCIONÁRIO


def cadastrarFuncionario(request):
    return render(request, 'funcionario/cadastrarFuncionario.html')


def salvarNovoFuncionarioNoDB(request):
    funcionario = Funcionario()
    funcionario.nome = request.POST.get('nome')
    funcionario.cpf = request.POST.get('cpf')
    funcionario.email = request.POST.get('email')
    funcionario.telefone = request.POST.get('telefone')
    funcionario.endereco = request.POST.get('endereco')
    funcionario.salario = request.POST.get('salario')
    funcionario.cargo = request.POST.get('cargo')
    funcionario.save()
    return render(request, 'funcionario/cadastrarFuncionario.html')


def listarFuncionarios(request):
    funcionarios = {
        'funcionarios': Funcionario.objects.all()
    }
    return render(request, 'funcionario/listarFuncionarios.html', funcionarios)


def preencherDadosFuncionario(request):
    args = gerarDadosCliente()
    args.update({'cargo': random.choice(["Groomer", "Atendente de Loja", "Veterinário", "Banho e Tosa", "Recepcionista",
                "Esteticista Animal", "Auxiliar de Veterinária", "Faz o cafézinho", "Auxiliar de Banho e Tosa"])})
    args.update({'salario': random.randint(1412, 3000)})
    return render(request, 'funcionario/cadastrarFuncionario.html', args)


def infoFuncionario(request, IDFuncionario):
    args = {
        'funcionario': Funcionario.objects.get(id_funcionario=IDFuncionario),
    }
    return render(request, 'funcionario/infoFuncionario.html', args)


def excluirFuncionarioDoDB(request, IDFuncionario):
    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_funcionario WHERE id_funcionario='+str(IDFuncionario))
    bd.commit()
    bd.close()

    funcionarios = {
        'funcionarios': Funcionario.objects.all()
    }
    return render(request, 'funcionario/listarFuncionarios.html', funcionarios)


def editarFuncionarioNoDB(request, IDFuncionario):
    funcionario = Funcionario()
    funcionario.nome = request.POST.get('nome')
    funcionario.cpf = request.POST.get('cpf')
    funcionario.email = request.POST.get('email')
    funcionario.telefone = request.POST.get('telefone')
    funcionario.endereco = request.POST.get('endereco')
    funcionario.salario = request.POST.get('salario')
    funcionario.cargo = request.POST.get('cargo')

    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute("UPDATE appPetPlanet_funcionario SET nome='" +
                   str(funcionario.nome) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET cpf='" +
                   str(funcionario.cpf) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET email='" +
                   str(funcionario.email) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET telefone='" +
                   str(funcionario.telefone) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET endereco='" +
                   str(funcionario.endereco) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET salario='" +
                   str(funcionario.salario) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET cargo='" +
                   str(funcionario.cargo) + "' WHERE id_funcionario=" + str(IDFuncionario))
    bd.commit()
    bd.close()

    funcionarios = {
        'funcionarios': Funcionario.objects.all()
    }
    return render(request, 'funcionario/listarFuncionarios.html', funcionarios)

# FUNÇÕES DOS PRODUTOS


def cadastrarProduto(request):
    return render(request, 'produto/cadastrarProduto.html')


def salvarNovoProdutoNoDB(request):
    produto = Produto()
    produto.nome = request.POST.get('nome')
    produto.preco = request.POST.get('preco')
    produto.estoque = request.POST.get('estoque')
    produto.validade = request.POST.get('validade')
    produto.categoria = request.POST.get('categoria')
    produto.save()
    return render(request, 'produto/cadastrarProduto.html')


def listarProdutos(request):
    produtos = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'produto/listarProdutos.html', produtos)


def infoProduto(request, IDProduto):
    args = {
        'produto': Produto.objects.get(id_produto=IDProduto),
    }
    return render(request, 'produto/infoProduto.html', args)


def excluirProdutoDoDB(request, IDProduto):
    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_produto WHERE id_produto='+str(IDProduto))
    bd.commit()
    bd.close()
    produtos = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'produto/listarProdutos.html', produtos)


def editarProdutoNoDB(request, IDProduto):
    produto = Produto()
    produto.nome = request.POST.get('nome')
    produto.preco = request.POST.get('preco')
    produto.estoque = request.POST.get('estoque')
    produto.validade = request.POST.get('validade')
    produto.categoria = request.POST.get('categoria')

    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute("UPDATE appPetPlanet_produto SET nome='" +
                   str(produto.nome) + "' WHERE id_produto=" + str(IDProduto))
    cursor.execute("UPDATE appPetPlanet_produto SET preco='" +
                   str(produto.preco) + "' WHERE id_produto=" + str(IDProduto))
    cursor.execute("UPDATE appPetPlanet_produto SET estoque='" +
                   str(produto.estoque) + "' WHERE id_produto=" + str(IDProduto))
    cursor.execute("UPDATE appPetPlanet_produto SET validade='" +
                   str(produto.validade) + "' WHERE id_produto=" + str(IDProduto))
    cursor.execute("UPDATE appPetPlanet_produto SET categoria='" +
                   str(produto.categoria) + "' WHERE id_produto=" + str(IDProduto))
    bd.commit()
    bd.close()

    produtos = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'produto/listarProdutos.html', produtos)


# FUNÇÕES SERVIÇOS
def gerarServico(request):
    args = {
        'clientes': Cliente.objects.all(),
        'funcionarios': Funcionario.objects.all(),
        'produtos': Produto.objects.filter(categoria='Serviços'),
        'pets': Pet.objects.all(),
    }
    return render(request, 'servico/gerarServico.html', args)


def gerarServicoFiltrandoPet(request, IDDono):
    clienteSelecionado = Cliente.objects.get(id_cliente=IDDono)
    clientes = Cliente.objects.all()
    pets = Pet.objects.filter(id_dono=IDDono)
    args = {
        # Conserto de bug
        'clienteSelecionado': clienteSelecionado,
        'clientes': clientes,
        'funcionarios': Funcionario.objects.all(),
        'produtos': Produto.objects.filter(categoria='Serviços'),
        'pets': pets,
    }
    return render(request, 'servico/gerarServico.html', args)


def salvarServicoGeradoNoDB(request):
    servico = Servico()
    servico.datahora = request.POST.get('datahora')
    servico.cliente_id = request.POST.get('cliente_id')
    servico.pet_id = request.POST.get('pet_id')
    servico.servico_id = request.POST.get('servico_id')
    servico.funcionario_id = request.POST.get('funcionario_id')
    servico.observacoes = request.POST.get('observacoes')
    servico.save()

    args = {
        'clientes': Cliente.objects.all(),
        'funcionarios': Funcionario.objects.all(),
        'produtos': Produto.objects.filter(categoria='Serviços'),
        'pets': Pet.objects.all(),
    }

    return render(request, 'servico/gerarServico.html', args)


def listarAgenda(request):
    clientes = Cliente.objects.all(),
    funcionarios = Funcionario.objects.all(),
    produtos = Produto.objects.all(),
    pets = Pet.objects.all(),
    agenda = Servico.objects.all(),
    agendaOrganizada = Servico.objects.order_by('datahora').all()

    args = {
        'clientes': clientes,
        'funcionarios': funcionarios,
        'produtos': produtos,
        'pets': pets,
        'agenda': agenda,
        'agendaOrganizada': etiquetarAgenda(agendaOrganizada)
    }
    return render(request, 'servico/listarAgenda.html', args)


def etiquetarAgenda(agenda):
    agendaOrganizada = agenda
    for servico in agendaOrganizada:
        try:
            servico.cliente_id = Cliente.objects.get(
                id_cliente=servico.cliente_id).nome
        except:
            servico.cliente_id = "CLIENTE EXCLUÍDO"
        try:
            servico.funcionario_id = Funcionario.objects.get(
                id_funcionario=servico.funcionario_id).nome
        except:
            servico.funcionario_id = "FUNCIONÁRIO EXCLUÍDO"
        try:
            servico.servico_id = Produto.objects.get(
                id_produto=servico.servico_id).nome
        except:
            servico.servico_id = "SERVIÇO EXCLUÍDO"
        try:
            servico.pet_id = Pet.objects.get(
                id_pet=servico.pet_id).nome
        except:
            servico.pet_id = "PET EXCLUÍDO"
    return agendaOrganizada


def excluirServicoDoDB(request, IDServico):

    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_servico WHERE id_servico='+str(IDServico))
    bd.commit()
    bd.close()

    args = {
        'clientes': Cliente.objects.all(),
        'funcionarios': Funcionario.objects.all(),
        'produtos': Produto.objects.all(),
        'pets': Pet.objects.all(),
        'agenda': Servico.objects.all(),
        'agendaOrganizada': etiquetarAgenda(Servico.objects.order_by('datahora').all())
    }
    return render(request, 'servico/listarAgenda.html', args)

# Funções vendas


def novaVenda(request):
    args = {
        'clientes': Cliente.objects.all(),
        'produtos': Produto.objects.all(),
        'funcionarios': Funcionario.objects.all(),
    }
    return render(request, 'venda/novaVenda.html', args)


# API's para comunicação com o DB
def getDadosProduto(request, IDProduto):
    print(f'Iniciou, IDProduto: {IDProduto}')
    produto = Produto.objects.get(id_produto=IDProduto)
    dados = {
        'id_produto': produto.id_produto,
        'nome': produto.nome,
        'preco': produto.preco,
        'estoque': produto.estoque,
        'validade': produto.validade,
        'categoria': produto.categoria,
    }
    return JsonResponse(dados)


def concluirVenda(request, idCliente, jsonProdutos, idVendedor, formaPagamento, datahora):

    venda = Venda()

    venda.cliente_id = idCliente
    venda.itens = jsonProdutos
    venda.vendedor_id = idVendedor
    venda.formaDePagamento = formaPagamento
    venda.datahora = datahora

    print(f'venda.cliente_id: {venda.cliente_id}')
    print(f'venda.itens: {venda.itens}')
    print(f'venda.vendedor_id: {venda.vendedor_id}')
    print(f'venda.formaDePagamento: {venda.formaDePagamento}')
    print(f'venda.datahora: {venda.datahora}')

    venda.save()

    return render(request, 'home.html')
