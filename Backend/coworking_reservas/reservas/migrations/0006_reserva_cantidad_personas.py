# Generated by Django 5.0.1 on 2024-12-17 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0005_reserva_bloques_seleccionados'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='cantidad_personas',
            field=models.PositiveIntegerField(default=1),
        ),
    ]