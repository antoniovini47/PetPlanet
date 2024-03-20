# Generated by Django 5.0.2 on 2024-03-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPetPlanet', '0002_rename_endereço_cliente_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id_pet', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('especie', models.TextField()),
                ('raca', models.TextField()),
                ('idade', models.TextField()),
                ('sexo', models.TextField()),
                ('porte', models.TextField()),
                ('alergias', models.TextField()),
            ],
        ),
    ]
