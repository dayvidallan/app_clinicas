from django.db import models
from django.urls import reverse_lazy
from clientes.models import Paciente
from funcionarios.models import Funcionario
from django.utils import timezone
from django.db.models import Sum





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



class Financeiros(models.Model):
    profissional = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    servico = models.CharField(max_length=100, unique=False)
    data = models.DateTimeField(default=timezone.now)
    valor = models.CharField(max_length=11, blank=True, null=True, verbose_name='R$ Valor')
    observacao = models.TextField(null=True, blank=True)
    recibo = models.BooleanField(verbose_name='Gerar Recibo?', default=False)

    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse_lazy('financeiros_list')


    def total_horas_extra(self):
        total = self.Financeiros.all(
            ).aggregate(
            Sum('valor'))['valor__sum']
        return total or 0



