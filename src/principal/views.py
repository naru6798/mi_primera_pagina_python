from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    return HttpResponse("Hola desde Django!")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Hola desde Django con etiquetas!</h1>")

def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"Hola {nombre} {apellido} desde Django con parámetros!")
# Va a ocurrir que cuando se abra el servidor va a dar un error porque faltan parametros. En el mismo link del servidor se agregan los valores para los parametros de la funcion. Por ejemplo http://127.0.0.1:8000/saludar3/Naren/Mirabel. Ademas hay que aclarar en la puerta de entrada, es decir en urls.py que debe tomar strings en el link

def index(request):
    from datetime import datetime
    año_actual = datetime.now().year
    contexto = {'año': año_actual}
    return render(request, 'principal/index.html', contexto)

def tirar_dado(request):
    from datetime import datetime
    from random import randit

    tiro_de_dado = randit(1, 6)

    if tiro_de_dado == 6:
        mensaje = f'Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😀 ✨ Ganaste ✨'
    else:
        mensaje = f'Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😢 Sigue intentando. Presiona F5 para volver a tirar.'

    datos = {
        'title': 'Tiro de Dados',
        'message': mensaje,
        'fecha': datetime.now().strftime('%H:%M:%S.%f'),
    }

    return render(request, 'principal/tirar-dado.html', context = datos)

