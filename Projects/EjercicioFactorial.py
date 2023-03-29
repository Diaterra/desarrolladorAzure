numero=int(input("introduzca un numero"))
if numero==0:
    print(f"el factorial de {numero} es: 0")
else:
    i=0
    factorial=1
    while i<numero:
         factorial = factorial * (numero - i)
         i += 1
    print(f"el factorial de {numero} es: {factorial}")