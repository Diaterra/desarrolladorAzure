import sys

import cx_Oracle

connection = cx_Oracle.connect("system", "netoracle", "localhost/XE")

cursor = connection.cursor()

while True:
    opcion = int(input(("\n" + "---PULSA EN LA OPCION---" + "\n"
             "\n" + "1. Alta enfermo" + "\n"
             "\n" + "2. Baja enfermo" + "\n"                                                                                  
             "\n" + "3. Modificacion enfermo" + "\n"
             "\n" + "4. Salir" + "\n"
             "\n")))
    if opcion == 1:
        try:
            enf=input("Introducir numero de enfermo")
            ape=input("Introducir el apellido")
            dir=input("Introducir direccion")
            fecha=input("Introducir la fecha de nac")
            sex=input("Introducir el sexo")
            nss=input("Introducir el numero de nss")
            p_afe=cursor.var(cx_Oracle.NUMBER)
            args=(enf,ape,dir,fecha,sex,nss,p_afe)
            cursor.callproc('GESTIONENFERMO.ALTAENF', args)
            if p_afe.getvalue() >= 1:
                print("dato insertado")
            else:
                print("Error a insertar registro")
        except ValueError:
            print("Debe introducir un numero")
        except connection.Error as error:
            print("Error: ", error)

    elif opcion == 2:
        try:
            enf = input("Introducir numero de enfermo a borrar")
            p_afe = cursor.var(cx_Oracle.NUMBER)
            cursor.callproc('GESTIONENFERMO.BAJAENF', (enf,p_afe))
            if p_afe.getvalue() >= 1:
                print("dato borrado")
            else:
                print("Error al borrar el registro")
        except connection.Error as error:
            print("Error: ", error)
    elif opcion == 3:
        try:
            enf = input("Introducir numero de enfermo a modificar")
            dir = input("Introducir la nueva direccion")
            p_afe = cursor.var(cx_Oracle.NUMBER)
            args=(enf,dir,p_afe)
            cursor.callproc('GESTIONENFERMO.UPDATEENF', args)
            if p_afe.getvalue() >= 1:
                print("dato actualizado")
            else:
                print("Error al actualizar el registro")
        except connection.Error as error:
            print("Error: ", error)
    else:
        connection.close()
        sys.exit()