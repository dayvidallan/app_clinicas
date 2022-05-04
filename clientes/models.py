from django.db import models
from funcionarios.models import Funcionario


class Paciente(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da clinica')
    funcinario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)


