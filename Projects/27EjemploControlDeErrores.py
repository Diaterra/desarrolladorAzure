def controlErrores():
    try:
        numero= int(input("Introduce numero: "))
        print("Numero: ", numero)
    except ValueError:
        print("Error, debe introducir un numero: ")
        controlErrores()



########################################################

controlErrores()
