from django.shortcuts import get_object_or_404, redirect, render
from reserva.forms import ReservaModelForm
from .models import Reserva


def index(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'index.html', context)


def detalhar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    return render(request, 'detalhe.html', {'reserva': reserva})


def cadastrar_reserva(request):
    if request.method == 'POST':
        form = ReservaModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ReservaModelForm()
            return redirect('index')
        else:
            form = ReservaModelForm(request.POST)
    else:
        form = ReservaModelForm()
    return render(request, 'form.html', {'form': form})


def deletar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('cadastrar')
