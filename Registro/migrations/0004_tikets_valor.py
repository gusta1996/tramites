# Generated by Django 4.0.5 on 2022-07-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0003_tikets'),
    ]

    operations = [
        migrations.AddField(
            model_name='tikets',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=9),
        ),
    ]