# Generated by Django 4.0.5 on 2022-08-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0028_registromunicipal_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='registromunicipal',
            name='notas',
            field=models.TextField(blank=True, null=True),
        ),
    ]
