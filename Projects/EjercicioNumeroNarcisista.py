numero = input("Introduzca un numero: ")
exponente = len(numero)
suma = 0
for i in numero:
    suma += pow(int(i), exponente)
if suma == int(numero):
    print(f"{numero} es un numero narcisista")
else:
    print(f"{numero} no es un numero narcisista")
