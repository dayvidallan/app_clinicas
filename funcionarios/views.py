from django.http import HttpResponse
from django.shortcuts import render
from .models import Funcionario


def home(request):
    return render(request, 'recibo_detail.html')


def home(request):

    meu_perfil = Funcionario.objects.all()

    data = {
            'perfil': meu_perfil,
            }

    return render(request, 'recibo_detail.html', data)
