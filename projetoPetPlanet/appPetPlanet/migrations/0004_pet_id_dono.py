# Generated by Django 5.0.2 on 2024-03-20 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPetPlanet', '0003_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='id_dono',
            field=models.IntegerField(default=1),
        ),
    ]
