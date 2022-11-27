from django.shortcuts import render,redirect
from seleccion.forms import FormJugador
from seleccion.models import Jugador
from . import forms

def index(request):
    return render(request, 'seleccion/index.html')

def listadoJugadores(request):
    jugadores = Jugador.objects.all()
    data = {'jugadores': jugadores}
    return render(request, 'seleccion/jugadores.html', data)

def agregarJugadores(request):
    form = FormJugador()
    if request.method == 'POST':
        form = FormJugador(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'seleccion/agregarJugadores.html', data)

def eliminarJugadores(request, id):
    jugadores = Jugador.objects.get(id = id)
    jugadores.delete()
    return redirect('/jugadores')

def actualizarJugadores(request, id):
    jugadores = Jugador.objects.get(id = id)
    form = FormJugador(instance=jugadores)
    if request.method == 'POST':
        form = FormJugador(request.POST, instance=jugadores)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'seleccion/agregarJugadores.html', data)
