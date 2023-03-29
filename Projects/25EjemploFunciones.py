def calcularIva():
    importe = int(input("Precio del producto"))
    total = importe*1.21
    print (f"Iva incluido(21%: {total}")

"""Esta funcion no retorna nada, solo demuestra el calculo de un iva, no mostraria nada por consola ni por pantalla,
no lo devuelve por patanlla"""

calcularIva()

print("---funciones con parametros-----")

def calcularIva2(importe):
    total = importe*1.21
    print(f"Iva incluido(21%: {total}")

calcularIva2(100)

"""Esta funcion si retorna """

def calcularIva3(importe):
    total=importe*1.21
    return total

resultado=calcularIva3(125)

print("resultado",resultado)

