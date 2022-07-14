# from curses.ascii import HT
from django.shortcuts import render, HttpResponse, redirect
# import layoutparser as layout

# Create your views here.

# MVC - Modelo Vista Controlador -> Acciones (métodos) 
# MVT - Modelo Vista Template (solo en django) -> Acciones (métodos)

layout = """
    <h1>Bienvenido a la página de Inicio</h1>
    <hr>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-django">Hola Django</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Página de pruebas</a>
        </li>
        <li>
            <a href="/contacto">Contacto</a>
        </li>
    </ul>
    <hr>
"""

def index(request):
    html = """
        <br><br>
        <h3>Años hasta el 2050</h3>
        <ul>
    """
    year = 2022
    while year <= 2060:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"
    
    nombre = 'Carlos Mariscal'
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C', 'JS']
    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
    })

def hola_django(request):
    return render(request, 'hola_django.html')

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('contacto', nombre="Victor", apellidos="Arismendi")
        # return redirect('/contacto/Sandra/Mora')
    return render(request, 'pagina.html')

def contacto(request, nombre ="", apellidos=""):
    html = ""
    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos}</h3>"
    return HttpResponse(layout + f"<h2>Contacto {nombre} {apellidos}</h2>" + html)