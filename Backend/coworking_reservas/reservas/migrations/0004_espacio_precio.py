# Generated by Django 5.0.1 on 2024-11-20 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_alter_notificacion_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='espacio',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]