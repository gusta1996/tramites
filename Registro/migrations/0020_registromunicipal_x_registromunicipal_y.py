# Generated by Django 4.0.5 on 2022-08-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0019_registromunicipal_ruc'),
    ]

    operations = [
        migrations.AddField(
            model_name='registromunicipal',
            name='x',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='registromunicipal',
            name='y',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
