# Generated by Django 4.0.5 on 2022-08-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0010_perfil_nacionalidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='empresa',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
