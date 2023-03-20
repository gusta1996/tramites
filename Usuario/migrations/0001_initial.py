# Generated by Django 4.0.6 on 2022-07-19 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': '1. Provincias',
            },
        ),
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.provincias')),
            ],
            options={
                'verbose_name_plural': '2. Ciudades',
            },
        ),
    ]
