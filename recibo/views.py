from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
from funcionarios.models import Funcionario
from .models import Recibo, Financeiro
from .forms import ReciboForm, FinanceiroForm



@login_required(login_url='login/')
def recibo_list(request):
    template_name = 'recibo_list.html'
    objects = Financeiro.objects.order_by("id").all()
    count = Financeiro.bjects.values("paciente.cpf").annotate(Count("id"))
    contador = {'count': count}

    search = request.GET.get('search')
    if search:
        objects = objects.filter(nome__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context, contador)


class ReciboList(ListView):
    model = Financeiro
    template_name = 'recibo_list.html'
    paginate_by = 10

    def get_queryset(self):
        empresa_logada = self.request.user.paciente.clinica
        return Financeiro.objects.filter(
            paciente__clinica=empresa_logada)

    def get_queryset(self):
        queryset = super(ReciboList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(paciente__nome__icontains=search) |
                Q(paciente__cpf__icontains=search)
            )
        return queryset



class ReciboCreate(CreateView):
    model = Financeiro
    template_name = 'recibo_form.html'
    form_class = FinanceiroForm


def recibo_detail(request, pk):
    template_name = 'recibo_detail.html'
    obj = Financeiro.objects.get(pk=pk)
    meu_perfil = Funcionario.objects.all()
    context = {
        'object': obj,
        'perfil': meu_perfil

    }
    return render(request, template_name, context)


def recibo_add(request):
    form = FinanceiroForm(request.POST or None)
    template_name = 'recibo_list.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('recibo_list'))

    context = {'form': form}
    return render(request, template_name, context)


class ReciboUpdate(UpdateView):
    model = Financeiro
    template_name = 'recibo_form.html'
    form_class = FinanceiroForm



