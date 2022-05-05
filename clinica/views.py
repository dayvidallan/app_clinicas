from django.contrib.auth.decorators import login_required
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
from django.shortcuts import render

from .models import Clinica


@login_required(login_url='login/')
def clinica(request):
    template_name = 'index.html'
    object = Clinica.objects.all()
    context = {'object_list': object}
    return render(request, template_name, context)
