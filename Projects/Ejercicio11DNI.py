dni = int(input("introduzca su num de dni: "))
resultado1 = round(dni / 23)
resultado2 = resultado1 * 23
resultado3 = dni - resultado2

if resultado3==4:
    print("G")
elif resultado3==5:
    print("M")



letrasDni="TRWAFMYFPDXBNJZSQVHLCKET"
print(letrasDni[resultado3])