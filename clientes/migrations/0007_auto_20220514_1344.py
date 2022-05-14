# Generated by Django 3.2.13 on 2022-05-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_rename_procedimeto_consulta_anamnesi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='anamnesi',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ananimese'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='anamnesi',
            field=models.TextField(blank=True, null=True, verbose_name='Ananimese'),
        ),
    ]
