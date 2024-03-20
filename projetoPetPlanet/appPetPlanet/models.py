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
