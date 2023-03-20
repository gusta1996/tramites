# Generated by Django 4.0.5 on 2022-07-21 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tramites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('detalle', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requisitos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisito', models.CharField(max_length=60)),
                ('detalle', models.TextField(blank=True, null=True)),
                ('tramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.tramites')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroMunicipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.tramites')),
            ],
        ),
    ]