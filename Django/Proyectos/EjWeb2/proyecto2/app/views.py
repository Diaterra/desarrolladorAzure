from django.shortcuts import render

def index(request):
    return render(request,"app/inicio.html")


def equipo(request):
    nombre='Real Madrid'
    dato=nombre.upper()
    lista={
        "equipo1":dato
    }
    return render(request, "app/equipoPreferido.html",lista)
# Create your views here.
