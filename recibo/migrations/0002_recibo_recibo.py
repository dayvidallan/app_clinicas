# Generated by Django 3.2.13 on 2022-05-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recibo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibo',
            name='recibo',
            field=models.BooleanField(default=False),
        ),
    ]
