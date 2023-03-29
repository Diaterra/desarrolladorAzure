diaNac=int(input("Introduza su dia de Nacimiento: "))
mesNac=int(input("Introduza el mes de Nacimiento: "))
yearNac=int(input("Introduza el año de Nacimiento: "))
tabla=("Sabado","Domingo","Lunes","Martes","Miercoles","Jueves","Viernes")

if mesNac == 1:
    mesNac = 13
    yearNac -= 1
elif mesNac == 2:
    mesNac = 14
    yearNac -= 1


paso1=((mesNac+1)*3)/5
paso2=(yearNac//4)
paso3=(yearNac/100).__floor__()
paso4=(yearNac/400).__floor__()
paso5=(diaNac+(mesNac*2)+yearNac+paso1+paso2-paso3+paso4+2).__floor__()
paso6=(paso5/7).__floor__()
paso7=(paso5-(paso6*7)).__floor__()
diaSema=tabla[(paso7)]
print(f"Usted a nacido el dia: {diaSema}")