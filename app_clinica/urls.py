
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('clinica.urls')),
    path('agenda/', include('agenda.urls')),
    path('recibo/', include('recibo.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('prontuario/', include('clientes.urls')),
    path('admin/', admin.site.urls),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]