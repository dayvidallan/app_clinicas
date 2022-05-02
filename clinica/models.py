from django.db import models

# Create your models here.

class Clinica(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da clinica')

