from django import forms
from seleccion.models import Jugador
class FormJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'


    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nacionalidad = forms.CharField(max_length=50)
    club = forms.CharField(max_length=50)
    posicion = forms.CharField(max_length=50)
    goles = forms.IntegerField()