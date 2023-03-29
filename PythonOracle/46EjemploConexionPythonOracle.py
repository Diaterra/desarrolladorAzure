import cx_Oracle

connection=cx_Oracle.connect("system", "netoracle","localhost/XE")

cursor=connection.cursor()

try:
    cursor.execute("SELECT EMP_NO,APELLIDO FROM EMP")
    print("Lista de empleados")
    print("----------------------------------------------")
    for numero,apellido in cursor:
        print("Numero de empleado: ",numero, "Apellido: ",apellido)
except connection.Error as error:
    print("Error: ",error)

connection.close()