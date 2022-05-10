from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

from .models import Recibo
from .forms import ReciboForm


@login_required(login_url='login/')
def recibo_list(request):
    template_name = 'financeiros_list.html'
    objects = Recibo.objects.order_by("id").all()
    count = Recibo.bjects.values("cpf").annotate(Count("id"))
    contador = {'count': count}

    search = request.GET.get('search')
    if search:
        objects = objects.filter(nome__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context, contador)


class ReciboList(ListView):
    model = Recibo
    template_name = 'financeiros_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ReciboList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(cpf__icontains=search)
            )
        return queryset



class ReciboCreate(CreateView):
    model = Recibo
    template_name = 'recibo_form.html'
    form_class = ReciboForm


def recibo_detail(request, pk):
    template_name = 'recibo_detail.html'
    obj = Recibo.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def recibo_add(request):
    form = ReciboForm(request.POST or None)
    template_name = 'financeiros_list.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('recibo_list'))

    context = {'form': form}
    return render(request, template_name, context)


class ReciboUpdate(UpdateView):
    model = Recibo
    template_name = 'recibo_form.html'
    form_class = ReciboForm

