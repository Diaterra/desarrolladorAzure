print("--------------CONJETURA DE COLLATZ------------")


numero=int(input("Introduzca un número:"))
resultado=""
while numero != 1:
    resultado += "\n"
    if (numero % 2 == 0):
        numero = numero / 2
    else:
        numero = (numero * 3) + 1
    resultado +=  str(numero)
    resultado += "\n"

print(f"Resultado Conjetura {resultado} ")
