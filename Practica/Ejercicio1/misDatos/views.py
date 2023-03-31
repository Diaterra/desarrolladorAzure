
from django.shortcuts import render

def index(request):
    dato1='Diana'
    dato2='Terragno'
    dato3=40
    lista={
        "nombre": dato1,
        "apellido": dato2,
        "edad": dato3,

    }
    return render(request,"webs/datos.html",lista)


# Create your views here.
