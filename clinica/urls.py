from django.urls import path
from .views import clinica


urlpatterns = [
    path('', clinica, name="clinica"),



]
