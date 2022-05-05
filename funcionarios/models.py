from django.db import models
from django.contrib.auth.models import User
from clinica.models import Clinica

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    clinica = models.ForeignKey(Clinica, on_delete=models.PROTECT)
    cpf = models.CharField(max_length=14, blank=True, null=True, verbose_name='Nº CPF')
    especialidade = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    apresent = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')

    imagem = models.ImageField(upload_to='perfils', null=True, blank=True)

    def __str__(self):
        return self.name



    def __str__(self):
        return self.nome



