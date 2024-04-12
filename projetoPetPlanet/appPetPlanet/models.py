from django.db import models


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cpf = models.TextField()
    nome = models.TextField()
    email = models.TextField()
    telefone = models.TextField()
    endereco = models.TextField()


class Pet(models.Model):
    id_pet = models.AutoField(primary_key=True)
    nome = models.TextField()
    especie = models.TextField()
    raca = models.TextField()
    idade = models.TextField()
    sexo = models.TextField()
    porte = models.TextField()
    alergias = models.TextField()
    id_dono = models.IntegerField(default=1)


class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome = models.TextField()
    cpf = models.TextField()
    email = models.TextField()
    telefone = models.TextField()
    endereco = models.TextField()
    salario = models.FloatField()
    cargo = models.TextField()


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField()
    preco = models.FloatField()
    estoque = models.IntegerField()
    validade = models.TextField(default='12/12/2099')
    categoria = models.TextField()


class Servico(models.Model):
    id_servico = models.AutoField(primary_key=True)
    datahora = models.DateTimeField()
    cliente_id = models.IntegerField()
    pet_id = models.IntegerField()
    servico_id = models.TextField(default=3)
    funcionario_id = models.IntegerField()
    observacoes = models.TextField()


class Venda(models.Model):
    id_venda = models.AutoField(primary_key=True)
    cliente_id = models.IntegerField()
    vendedor_id = models.IntegerField()
    formaDePagamento = models.TextField()
    itens = models.JSONField()
    datahora = models.DateTimeField()
    total = models.FloatField(default=1)
