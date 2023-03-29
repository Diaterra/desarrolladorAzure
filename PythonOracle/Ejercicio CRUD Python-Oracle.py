import cx_Oracle
import sys

connection=cx_Oracle.connect("system", "netoracle","localhost/XE")
cursor=connection.cursor()

while True:
    opcion = int(input(("\n" + "---PULSA EN LA OPCION---" + "\n"
                 "\n" + "1. Alta doctor" + "\n"
                 "\n" + "2. Baja doctor" + "\n"
                 "\n" + "3. Modificacion doctor" + "\n"
                 "\n" + "4. Consultar datos" + "\n"
                 "\n" + "5. Salir" + "\n"
                "\n")))
    if opcion==1:
        try:
            hospt_cod = int(input("Introduzca el Hospital_cod: "))
            doc_no= int(input("Introduzca el doc_no: "))
            ape= input("Introduzca el apellido: ")
            esp= input("Introduzca la especialidad: ")
            sal= int(input("Introduzca el salario: "))
            consulta1=("insert into doctor values(:p1,:p2,:p3,:p4,:p5)")
            cursor.execute(consulta1,(hospt_cod,doc_no,ape,esp,sal))
            connection.commit()
        except connection.Error as error:
            print("Error: ",error)

    elif opcion==2:
        try:
            doc_no2 = int(input("Introduzca el doc_no a borrar: "))
            consulta2=("delete from doctor where doctor_no=:p1")
            cursor.execute(consulta2,(doc_no2,))
            connection.commit()
            if cursor.rowcount>0:
                print("Registro borrado correctamente")
            else:
                print("Dato no encontrado")
        except connection.Error as error:
            print("Error: ", error)

    elif opcion==3:
        try:
            doc_no3=int(input("Introduzca el doc_no a modificar: "))
            espec=input("Introduzca la nueva especialidad")
            consulta3=("update doctor set especialidad=:p1 where doctor_no=:p2")
            cursor.execute(consulta3,(espec,doc_no3))
            connection.commit()
            if cursor.rowcount > 0:
                print("Registro actualizado correctamente")
            else:
                print("Dato no encontrado")
        except connection.Error as error:
            print("Error: ", error)

    elif opcion==4:
        try:
            consulta4=("select * from doctor")
            cursor.execute(consulta4)
            for hosp,doct,ape,esp,sal in cursor:
                print(hosp,doct,ape,esp,sal)
        except connection.Error as error:
            print("Error: ", error)

    else:
       connection.close()
       sys.exit()