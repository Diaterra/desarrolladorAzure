def validar():
    codigo = input("INTRODUZCA UN CODIGO EAN (8 O 10 CARACTERES)")
    digitoDeControl = codigo[(len(codigo))-1]
    sumapares = 0
    sumaimpares = 0
    resultado=""
    suma = 0
    for i in codigo:
        if int(i) % 2 == 0:
            sumapares += int(i)
    for i in codigo:
        if int(i) % 2 != 0:
            sumaimpares += int(i)
    if len(codigo) == 8:
        sumaimpares = sumaimpares * 3
    else:
        sumapares = sumapares * 3
    suma = sumapares + sumaimpares
    resto = suma % 10
    if resto == digitoDeControl:
        resultado = "ES VALIDO"
    else:
        resultado = "NO VALIDO"
    return resultado

print(validar())