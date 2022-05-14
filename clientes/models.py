from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone


class Paciente(models.Model):
    nome = models.CharField(max_length=100, unique=False)
    cpf = models.CharField(max_length=14, unique=False, verbose_name='Nº CPF')
    rg = models.CharField(max_length=14, unique=False)
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=100, unique=False, verbose_name='Nº telefone celular')
    endereco = models.CharField(max_length=100, unique=False)
    data_consulta = models.DateTimeField(default=timezone.now)
    anamnesi = models.TextField(null=True, blank=True, verbose_name='Ananimese')
    upload = models.FileField(upload_to='perfil', null=True, blank=True)

    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse_lazy('paciente_list')


    def __str__(self):
        return self.nome


class Procedimento(models.Model):
    procedimeto = models.CharField(max_length=14, null=True, blank=True)
    custo_medio = models.CharField(max_length=11, blank=True, null=True, verbose_name='Custo Médio R$')


    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse_lazy('financeiros_list')

    def __str__(self):
        return self.procedimeto


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_consulta = models.DateTimeField(default=timezone.now)
    anamnesi = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Ananimese')
    upload = models.FileField(upload_to='upload', null=True, blank=True, verbose_name='Documentos')

    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse_lazy('paciente_list')

    def __ini__(self):
        return self.paciente

