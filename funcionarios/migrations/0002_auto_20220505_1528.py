# Generated by Django 3.2.13 on 2022-05-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='apresent',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='bairro',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cidade',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Nº CPF'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='endereco',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='especialidade',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='estado',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='perfils'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='nrTelCelular',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='texto',
            field=models.TextField(blank=True, null=True),
        ),
    ]
