import sys

premios=[166116.06,133948.48,32353.38,1528.22,123.13,66.37,44.89,15.91]

def solicitarPremio():
    try:
        posicion=int(input("Introduzca el premio a mostrar"))-1
        print("premio obtenido: ", premios[posicion])
    except ValueError:
        print("Debe ingresar un numero")
    except IndexError:
        print("Dicha posicion del premio no se encuentra en la lista")
    except:
        print("error: ", sys.exc_info())

solicitarPremio()

