from django.db import models
from funcionarios.models import Funcionario


class Cliente(models.Model):
    nome = models.CharField(max_length=100)



