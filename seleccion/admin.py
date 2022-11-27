from django.contrib import admin
from seleccion.models import Jugador

class JugadorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'nacionalidad', 'club', 'posicion', 'goles']

admin.site.register(Jugador, JugadorAdmin)
