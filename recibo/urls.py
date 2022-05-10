from django.urls import path, include
from .views import ReciboList, \
    ReciboCreate, \
    ReciboUpdate, \
    recibo_detail





urlpatterns = [

    #RECIBO
    path('', ReciboList.as_view(), name='financeiros_list'),
    path('add-recibo/', ReciboCreate.as_view(), name='recibo_add'),
    path('<int:pk>/detail/', recibo_detail, name='recibo_detail'),
    path('<int:pk>/edit-recibo/', ReciboUpdate.as_view(), name='recibo_edit'),





]
