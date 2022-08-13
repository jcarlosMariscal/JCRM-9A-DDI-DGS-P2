from django.shortcuts import render

# from TiendaDjango.core.forms import ProductoForm
from .forms import ProductoForm
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

def form_mod_producto(request, id):
  producto = Producto.objects.get(idProducto = id)
  contexto = {
    'form': ProductoForm(instance=producto)
  }
  if request.method == 'POST':
    formulario = ProductoForm(data=request.POST, instance=producto)
    if formulario.is_valid:
      formulario.save()
      contexto['mensaje'] = "Se modificaron los datos correctamente"
  return render(request, 'core/form_mod_producto.html', contexto)
