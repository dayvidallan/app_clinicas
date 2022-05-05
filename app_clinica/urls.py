
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('clinica.urls')),
    path('agenda/', include('agenda.urls')),
    path('recibo/', include('recibo.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('prontuario/', include('clientes.urls')),
    path('admin/', admin.site.urls),


]
