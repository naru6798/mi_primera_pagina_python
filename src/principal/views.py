from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.urls import reverse_lazy

class MiLoginView(LoginView):
    template_name = 'principal/login.html'
    authentication_form = LoginForm
    next_page = reverse_lazy('principal:index')


# from .models import Cliente

def index(request):
    return render(request, 'principal/index.html')

def about(request):
    return render(request, 'principal/about.html')

# def saludar(request):
#     return HttpResponse("Hola desde Django!")

# def saludar_con_etiqueta(request):
#     return HttpResponse("<h1>Hola desde Django con etiquetas!</h1>")

# def saludar_con_parametros(request, nombre: str, apellido: str):
#     nombre = nombre.capitalize()
#     apellido = apellido.capitalize()
#     return HttpResponse(f"Hola {nombre} {apellido} desde Django con parámetros!")
# # Va a ocurrir que cuando se abra el servidor va a dar un error porque faltan parametros. En el mismo link del servidor se agregan los valores para los parametros de la funcion. Por ejemplo http://127.0.0.1:8000/saludar3/Naren/Mirabel. Ademas hay que aclarar en la puerta de entrada, es decir en urls.py que debe tomar strings en el link


# def tirar_dado(request):
#     from datetime import datetime
#     from random import randint

#     tiro_de_dado = randint(1, 6)

#     if tiro_de_dado == 6:
#         mensaje = f'Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😀 ✨ Ganaste ✨'
#     else:
#         mensaje = f'Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😢 Sigue intentando. Presiona F5 para volver a tirar.'

#     datos = {
#         'title': 'Tiro de Dados',
#         'message': mensaje,
#         'fecha': datetime.now().strftime('%H:%M:%S.%f'),
#     }

#     return render(request, 'principal/dados.html', context = datos)


# def ejercicio1(request):
#     nombre = "Naren"
#     apellido = "Mirabel"

#     datos = {
#         'nombre': nombre,
#         'apellido': apellido,
#     }

#     return render(request, 'principal/ejercicio1.html', context = datos)

# def ver_notas(request):
#     from random import randint
#     lista_notas = []
#     while len(lista_notas) < 26:
#         lista_notas.append(randint(1, 10))

#     return render (request, 'principal/notas.html', {'notas': lista_notas})

# def ejercicio_2(request):
#     usuarios = [
#         {'nombre': 'Naren', 'email': 'narenmirabel@gmail.com'},
#         {'nombre': 'Juan', 'email': 'juan@gmail.com'},
#         {'nombre': 'Pedro', 'email': 'pedro@gmail.com'},
#     ]
#     return render(request, 'principal/ejercicio2.html', {'usuarios': usuarios})

# def clientes_list(request):
#     clientes = Cliente.objects.all()
#     return render(request, 'principal/clientes_list.html', {'clientes': clientes})
