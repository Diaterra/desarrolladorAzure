import sys


def narcisista(numero):
    exponente = len(str(numero))
    suma = 0
    for i in str(numero):
        suma += pow(int(i), exponente)
    if suma == int(numero):
        resultado= str(numero) + " es un numero narcisista"
    else:
        resultado= str(numero) + " no es un numero narcisista"
    return resultado

def conjetura(number):
    if number == 1:
        return number
    else:
        while number != 1:
            if number % 2 == 0:
                number = number / 2
            else:
                number = (number * 3) + 1
        return number


""""----------------------------------"""
opcion=0
while True:
    opcion = int(input(("\n" + "---PULSA EN LA OPCION---" + "\n"
                 "\n" + "1. Comprobar numero Narcisista" + "\n"
                 "\n" + "2. Comprobar conjetura" + "\n"
                 "\n" + "3. Salir" + "\n"
                "\n")))
    if opcion==1:
       numero=int(input("introduzca un numero para comprobar si es Narcisista"))
       print(narcisista(numero))
    elif opcion==2:
       number = int(input("introduzca un numero para conjetura de collatz"))
       print(conjetura(number))
    else:
       sys.exit()

"""resultadoNarcisista=narcisista(371)

print(resultadoNarcisista)

resultadoConjetura=conjetura(5)
print(resultadoConjetura)"""