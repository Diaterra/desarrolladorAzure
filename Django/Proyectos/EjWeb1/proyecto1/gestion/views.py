from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Página de inicio")

# Create your views here.
