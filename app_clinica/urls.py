
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('website.urls')),
    path('agenda/', include('agenda.urls')),
    path('recibo/', include('recibo.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('admin/', admin.site.urls),


]
