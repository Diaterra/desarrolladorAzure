from django.shortcuts import render


def index(request):
    return render(request, "gestion/Inicio.html")

"""def index(request):
    return HttpResponse("Página de inicio")
# Create your views here."""

def equipo(request):
    nombre='Real Madrid'
    dato=nombre.upper()
    lista={
        "equipo1":dato
    }
    return render(request, "gestion/equipoPreferido.html",lista)

def jugadores(request):
    listajugadores=[
        {
            "Nombre":"Sergio Ramos",
            "Demarcacion":"Defensa",
            "Numero":5
        },
        {
            "Nombre": "Eden Hazard",
            "Demarcacion": "Delantero",
            "Numero":7
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero":9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero":8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]
    contexto = {
        'listado_jugadores': listajugadores
    }
    return render(request, "gestion/Jugadores.html",contexto)

def data(request):
    amigos=[
        {
            "Nombre":"Ana",
        },
        {
            "Nombre": "Andrea",
        },
        {
            "Nombre": "Adrian",
       },
        {
            "Nombre": "Maria",
        },
        {
            "Nombre": "Lucia",
        },
        {
            "Nombre": "Alex",
        },
        {
            "Nombre": "Benito",
        },
        {
            "Nombre": "Carlos",
        },
        {
            "Nombre": "Javier",
        },
        {
            "Nombre": "Antonio",
        },
        {
            "Nombre": "Maite",
        },
    ]
    contexto = {
        'Mis_amigos': amigos
    }
    return render(request, "gestion/DataList.html",contexto)

def peli(request):
    return render(request, "gestion/Peli.html")