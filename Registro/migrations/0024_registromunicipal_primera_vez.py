# Generated by Django 4.0.5 on 2022-08-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0023_registromunicipal_no_adeudar_e'),
    ]

    operations = [
        migrations.AddField(
            model_name='registromunicipal',
            name='primera_vez',
            field=models.BooleanField(default=False),
        ),
    ]
