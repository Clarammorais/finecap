from django.contrib import admin
from django.urls import path
from reserva.views import index, cadastrar_reserva, deletar_reserva, detalhar_reserva


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cadastrar/', cadastrar_reserva, name='cadastrar'),
    path('deletar/<int:id>/', deletar_reserva, name='deletar'),
    path('detalhe/<int:id>/', detalhar_reserva, name='detalhar'),
]
