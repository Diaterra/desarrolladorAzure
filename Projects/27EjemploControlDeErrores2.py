import sys


def controlDeErrores():
    try:
        dividendo = int(input("Introduce dividendo:"))
        divisor = int(input("Introduce divisor:"))
        resultado = dividendo / divisor
        print(f"Resultado división: {resultado}")
    except ValueError:
        print("Debe introducir un numero")
    #except ZeroDivisionError:
       # print("El divisor no puede ser cero")
    except:
        print(f"Error general: {sys.exc_info()}")
    finally:
        print("Entra")


controlDeErrores()
