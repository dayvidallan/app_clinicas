# Generated by Django 3.2.13 on 2022-05-14 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20220514_0932'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consulta',
            new_name='Procedimento',
        ),
    ]