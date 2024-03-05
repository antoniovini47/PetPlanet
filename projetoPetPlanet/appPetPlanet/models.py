from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cpf = models.TextField()
    nome = models.TextField()
    email = models.TextField()
    telefone = models.TextField()
    endereco = models.TextField()