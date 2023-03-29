import sys

isbn=input("Introduzca ISBN")
if len(isbn)!=10:
    print("Debe introducir 10 digitos")
    sys.exit()
resultado = 0
for i in range(1,11):
    digito=int(isbn[i-1])
    resultado+=digito*i
if resultado%11==0:
    print(f"{isbn} es correcto")
else:
    print(f"{isbn} es incorrecto")
