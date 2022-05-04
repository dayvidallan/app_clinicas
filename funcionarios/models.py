from django.db import models
from django.contrib.auth.models import User
from clinica.models import Clinica

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    clinica = models.ForeignKey(Clinica, on_delete=models.PROTECT)



    def __str__(self):
        return self.nome



