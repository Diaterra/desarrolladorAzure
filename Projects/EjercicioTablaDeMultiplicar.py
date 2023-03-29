numero=int(input("Introduzca el numero que quiera multiplicar"))
calculo=""
for i in range(1,11):
    resultado=numero*i
    calculo+= str(numero)+"*"+str(i)+"="+str(resultado) + "\n"
print(f"{calculo}")