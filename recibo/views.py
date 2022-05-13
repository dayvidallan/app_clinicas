from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
from funcionarios.models import Funcionario
from .models import Financeiros
from .forms import FinanceirosForm



@login_required(login_url='login/')
def recibo_list(request):
    template_name = 'financeiros_list.html'
    objects = Financeiros.objects.order_by("id").all()
    count = Financeiros.bjects.values("paciente.cpf").annotate(Count("id"))
    contador = {'count': count}

    search = request.GET.get('search')
    if search:
        objects = objects.filter(nome__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context, contador)



class ReciboList(ListView):
    model = Financeiros
    template_name = 'financeiros_list.html'

    def get(self, request):
        template_name = 'financeiros_list.html'
        empresa_logada = self.request.user.funcionario.id
        object = Financeiros.objects.all()
        perfil = Funcionario.objects.filter(user=empresa_logada)
        contex = {

                'perfil': perfil,
                'object_list': object,

            }
        return render(request, template_name, contex)


class ReciboCreate(CreateView):
    model = Financeiros
    template_name = 'recibo_form.html'
    form_class = FinanceirosForm


def recibo_detail(request, pk):
    template_name = 'recibo_detail.html'
    obj = Financeiros.objects.get(pk=pk)
    empresa_logada = request.user
    meu_perfil = Funcionario.objects.filter(user=empresa_logada)
    context = {
        'object': obj,
        'perfil': meu_perfil

    }
    return render(request, template_name, context)



def recibo_add(request):
    form = FinanceirosForm(request.POST or None)
    template_name = 'financeiros_list.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('recibo_list'))

    context = {'form': form}
    return render(request, template_name, context)


class ReciboUpdate(UpdateView):
    model = Financeiros
    template_name = 'recibo_form.html'
    form_class = FinanceirosForm




#RELATORIO

class RelatorioList(ListView):
    model = Financeiros

    template_name = 'relatorio_list.html'


    paginate_by = 10