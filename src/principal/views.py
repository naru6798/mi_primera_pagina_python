from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    return HttpResponse("Hola desde Django!")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Hola desde Django con etiquetas!</h1>")

# Create your views here.
