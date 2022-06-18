# from curses.ascii import HT
from django.shortcuts import render, HttpResponse

# Create your views here.

# MVC - Modelo Vista Controlador -> Acciones (métodos) 
# MVT - Modelo Vista Template (solo en django) -> Acciones (métodos)

def hola_django(request):
    return HttpResponse("""
        <center>
        <h1>Universidad Tecnológica de Tehuacán</h1>
        <h2>Django - Python - Web</h2>
        <h3>DDI - 9A</h3>
        </center>
    """)