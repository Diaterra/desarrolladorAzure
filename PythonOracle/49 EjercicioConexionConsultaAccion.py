import cx_Oracle

connection=cx_Oracle.connect("system", "netoracle","localhost/XE")
cursor=connection.cursor()
cursor2 = connection.cursor()
try:
    accion=("INSERT INTO DEPT VALUES(:P1,:P2,:P3)")
    dept_no=int(input("Introducir el numero de depto"))
    dnombre=input("Introducir el nombre")
    loc=input("Introducir una localidad")
    cursor.execute(accion,(dept_no,dnombre,loc))
    consulta=("select * from dept")
    connection.commit()
    cursor2.execute(consulta)

    for dpto,nomb,loc in cursor2:
        print(dpto,nomb,loc)

except connection.Error as error:
    print("Error: ",error)

connection.close()