# Generated by Django 4.0.5 on 2022-07-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0012_registromunicipal_es_usado_registromunicipal_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registromunicipal',
            name='fecha',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]
