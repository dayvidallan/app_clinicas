from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import (
    ListView

)
from .models import Funcionario


def home(request):
    return render(request, 'recibo_detail.html')


class home(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionarios.user
        meu_perfil = Funcionario.objects.filter(
                funcionario__user=empresa_logada)


