from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
from funcionarios.models import Funcionario
from .forms import ConsultaForm
from .models import Consulta
from .models import Paciente
from .forms import PacienteForm


@login_required(login_url='login/')
def paciente_list(request):
    template_name = 'paciente_list.html'
    objects = Paciente.objects.order_by("id").all()
    count = Paciente.bjects.values("cpf").annotate(Count("id"))
    contador = {'count': count}

    search = request.GET.get('search')
    if search:
        objects = objects.filter(nome__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context, contador)


class PacienteList(ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    paginate_by = 10

    def get(self, request):
        template_name = 'paciente_list.html'
        object = Paciente.objects.all()
        empresa_logada = self.request.user.funcionario.id
        perfil = Funcionario.objects.filter(user=empresa_logada)
        contex = {

            'perfil': perfil,
            'object_list': object,
        }
        return render(request, template_name, contex)



    def get_queryset(self):
        queryset = super(PacienteList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(cpf__icontains=search)
            )
        return queryset


class PacienteCreate(CreateView):
    model = Paciente
    template_name = 'paciente_form.html'
    form_class = PacienteForm


def paciente_detail(request, pk):
    template_name = 'paciente_detail.html'
    obj = Paciente.objects.get(pk=pk)
    object = Consulta.objects.filter(paciente=obj)
    meu_perfil = Funcionario.objects.all()
    context = {
        'object': obj,
        'object_list': object,
        'perfil': meu_perfil

    }
    return render(request, template_name, context)



def paciente_add(request):
    form = PacienteForm(request.POST or None)
    template_name = 'paciente_list.html'
    meu_perfil = Funcionario.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('paciente_list'))

    context = {

        'form': form,
        'perfil': meu_perfil


    }
    return render(request, template_name, context)


class PacienteUpdate(UpdateView):
    model = Paciente
    template_name = 'paciente_form.html'
    form_class = PacienteForm


class Upload(CreateView):
    model = Paciente
    template_name = 'paciente_form.html'
    form_class = PacienteForm


# CONSULTAS


class ConsultaCreate(CreateView):
    model = Consulta
    template_name = 'paciente_form.html'
    form_class = ConsultaForm


class ConsultaList(ListView):
    model = Paciente
    template_name = 'consulta_list.html'
    paginate_by = 10