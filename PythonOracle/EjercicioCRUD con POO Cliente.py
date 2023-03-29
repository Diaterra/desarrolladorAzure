from classCRUD import crud

myCrud = crud()
while True:
    opcion = int(input(("\n" + "---PULSA EN LA OPCION---" + "\n"
                 "\n" + "1. Alta doctor" + "\n"
                 "\n" + "2. Baja doctor" + "\n"
                 "\n" + "3. Modificacion doctor" + "\n"
                 "\n" + "4. Consultar datos" + "\n"
                 "\n" + "5. Salir" + "\n"
                "\n")))

    if opcion==1:
        hospt_cod = int(input("Introduzca el Hospital_cod: "))
        doc_no = int(input("Introduzca el doc_no: "))
        ape = input("Introduzca el apellido: ")
        esp = input("Introduzca la especialidad: ")
        sal = int(input("Introduzca el salario: "))
        myCrud.altaEmpleado(hospt_cod,doc_no,ape,esp,sal)
    elif opcion==2:
        doc_no2 = int(input("Introduzca el doc_no a borrar: "))
        print(myCrud.bajaEmpleado(doc_no2))
    elif opcion==3:
        doctor_no = int(input("Introduzca el doc_no a modificar: "))
        espec = input("Introduzca la nueva especialidad")
        print(myCrud.modificarEmpleado(espec,doctor_no))
    elif opcion==4:
        print(myCrud.consultaDatos())
    else:
        myCrud.salir()
