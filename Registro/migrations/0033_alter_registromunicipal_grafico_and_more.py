# Generated by Django 4.0.5 on 2022-08-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0032_registromunicipal_grafico_registromunicipal_puntos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registromunicipal',
            name='grafico',
            field=models.ImageField(blank=True, null=True, upload_to='graficos'),
        ),
        migrations.AlterField(
            model_name='registromunicipal',
            name='puntos',
            field=models.ImageField(blank=True, null=True, upload_to='puntos'),
        ),
    ]
