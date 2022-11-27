from django.db import models

# Create your models here.

class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    posicion = models.CharField(max_length=50)
    goles = models.IntegerField()