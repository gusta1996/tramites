# Generated by Django 4.0.5 on 2022-07-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requisitos',
            options={'verbose_name_plural': '2. Requisitos'},
        ),
        migrations.AlterModelOptions(
            name='tramites',
            options={'verbose_name_plural': '1. Tramites'},
        ),
        migrations.AlterField(
            model_name='requisitos',
            name='requisito',
            field=models.CharField(max_length=200),
        ),
    ]
