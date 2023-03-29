import sys

colores= dict()

colores = {
    "Amarillo": "Yellow",
    "Rosa": "Pink",
    "Azul": "Blue",
    "Blanco": "White",
    "Rojo": "Red",
}

def conseguirDato(key):
    try:
        dato=colores[key]
        print(dato)
    except KeyError:
       print("Dato no se encuentra, prueba con otro valor")
    except:
        print("Error: ", sys.exc_info())


conseguirDato("das")