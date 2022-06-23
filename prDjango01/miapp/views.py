# from curses.ascii import HT
from django.shortcuts import render, HttpResponse

# Create your views here.

# MVC - Modelo Vista Controlador -> Acciones (métodos) 
# MVT - Modelo Vista Template (solo en django) -> Acciones (métodos)

def index(request):
    html = """
        <h1>Bienvenido a la página de inicio</h1>
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
    
    return HttpResponse(html)

def hola_django(request):
    return HttpResponse(
        """
            <center>
            <h1>Universidad Tecnológica de Tehuacán</h1>
            <h2>Django - Python - Web</h2>
            <h3>DDI - 9A</h3>
            </center>
        """
    )

def pagina(request):
    return HttpResponse(
        """
            <h1>Página Web</h1>
            <h3>Materia DDI - Python - Django - Web</h3>
        """
    )