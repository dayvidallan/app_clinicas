# Generated by Django 3.2.13 on 2022-05-05 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20220505_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='cro',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Nº CRO'),
        ),
    ]
