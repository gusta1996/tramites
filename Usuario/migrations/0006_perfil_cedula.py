# Generated by Django 4.0.5 on 2022-08-04 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0005_alter_perfil_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='cedula',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
