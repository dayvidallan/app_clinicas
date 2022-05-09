from django.db import models
from django.urls import reverse_lazy
from clientes.models import Paciente
from django.utils import timezone
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw




class Recibo(models.Model):
    nome = models.CharField(max_length=100, unique=False)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=100, unique=False)
    endereco = models.CharField(max_length=100, unique=False)
    servico = models.CharField(max_length=100, unique=False)
    data = models.DateField(null=True, blank=True)
    valor = models.CharField(max_length=11, blank=True, null=True, verbose_name='R$ valor')
    observacao = models.TextField(null=True, blank=True)
    recibo = models.BooleanField(verbose_name='Gerar recibo?', default=False)

    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse_lazy('recibo_list')

    def __str__(self):
        return self.nome


class Financeiro(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    servico = models.CharField(max_length=100, unique=False)
    data = models.DateTimeField(default=timezone.now)
    valor = models.CharField(max_length=11, blank=True, null=True, verbose_name='R$ Valor')
    observacao = models.TextField(null=True, blank=True)
    recibo = models.BooleanField(verbose_name='Gerar Recibo?', default=False)

    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse_lazy('recibo_list')

