from dataclasses import field
from django import forms
from .models import Servicios

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ('clave', 'nombreCliente', 'TipServ', 'costo', 'FechaSer')
    