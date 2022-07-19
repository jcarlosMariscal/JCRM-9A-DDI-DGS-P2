from django.shortcuts import render
from .models import Producto

"""class Producto:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
        super().__init__()"""

# Create your views here.
"""def home(request):
    disco = Producto("Black Sabbath", 195.00)
    lista = ["Iron Man", "Capitán América", "Spider Man"]
    contexto = {"nombre":"UT Tehuacán", "personajes": lista, "disco": disco}
    return render(request, 'core/home.html', contexto)"""

def home(request):
    productos = Producto.objects.all()
    contexto = {
        "productos": productos
    }
    return render(request, 'core/home.html', contexto)
