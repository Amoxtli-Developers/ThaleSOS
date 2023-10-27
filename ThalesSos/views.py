from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def mi_vista(request):
    contexto = {
        'nombre_del_sitio': 'Mi Sitio Web',
        'fecha_actual': '27 de octubre de 2023'
    }
    return render(request, 'mi_template.html', contexto)