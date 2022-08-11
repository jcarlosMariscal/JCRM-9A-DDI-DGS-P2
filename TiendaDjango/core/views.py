Los accesos directos ayudan a simplificar Mi unidad … 
En las próximas semanas, los elementos que se encuentren en más de una carpeta se reemplazarán por accesos directos. El acceso a los archivos y las carpetas no cambiará.Más información
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

def form_producto(request):
    contexto = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_producto.html', contexto)