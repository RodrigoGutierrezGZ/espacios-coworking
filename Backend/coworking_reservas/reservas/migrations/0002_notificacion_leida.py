# Generated by Django 5.0.1 on 2024-11-20 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='leida',
            field=models.BooleanField(default=False),
        ),
    ]
