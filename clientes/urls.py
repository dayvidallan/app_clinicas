from django.urls import path, include
from .views import PacienteList, \
    PacienteCreate, \
    PacienteUpdate, \
    paciente_detail, \
    Upload





urlpatterns = [

    #RECIBO
    path('', PacienteList.as_view(), name='paciente_list'),
    path('add-paciente/', PacienteCreate.as_view(), name='paciente_add'),
    path('<int:pk>/paciente-detail/', paciente_detail, name='paciente_detail'),
    path('<int:pk>/upload/', Upload.as_view(), name='upload'),
    path('<int:pk>/edit-paciente/', PacienteUpdate.as_view(), name='paciente_edit'),




]
