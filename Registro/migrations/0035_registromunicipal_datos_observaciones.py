# Generated by Django 4.0.5 on 2022-08-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0034_registromunicipal_clave_catastral'),
    ]

    operations = [
        migrations.AddField(
            model_name='registromunicipal',
            name='datos_observaciones',
            field=models.TextField(blank=True, null=True),
        ),
    ]
