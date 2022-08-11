""" from dataclasses import fields """
from django import forms
from django.forms import ModelForm
from .models import Producto

""" SE CREA AL NIVEL DE core/ """

class ProductoForm(ModelForm):
    class Meta: 
        model = Producto
        fields = ['idProducto','nombreProducto', 'valorProducto', 'categoria']