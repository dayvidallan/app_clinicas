# Generated by Django 3.2.13 on 2022-05-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='upload'),
        ),
    ]
