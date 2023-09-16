from django.shortcuts import render, redirect
from .models import Formulario
from .forms import FormularioForm

# Create your views here.

def formulario(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormularioForm()

    datos = Formulario.objects.all()

    return render(request, 'formulario.html', {'form': form, 'datos': datos})

def editar(request, idalumo):
    dato = Formulario.objects.get(idalumo=idalumo)
    if request.method == 'POST':
        form = FormularioForm(request.POST, instance=dato)
        if form.is_valid():
            form.save()
            return redirect('formulario')
    else:
        form = FormularioForm(instance=dato)
    return render(request, 'editar.html', {'form': form})

def eliminar(request, idalumo):
    dato = Formulario.objects.get(idalumo=idalumo)
    dato.delete()
    return redirect('formulario')