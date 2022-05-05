# Generated by Django 3.2.13 on 2022-05-04 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('servico', models.CharField(max_length=100)),
                ('data', models.DateField(blank=True, null=True)),
                ('valor', models.CharField(blank=True, max_length=11, null=True, verbose_name='R$ valor')),
                ('observacao', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]