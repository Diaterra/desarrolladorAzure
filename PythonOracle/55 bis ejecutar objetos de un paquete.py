import cx_Oracle

connection = cx_Oracle.connect("system", "netoracle", "localhost/XE")

cursor = connection.cursor()

try:
    nEm=input("Introducir numero de empleado a cambiar el salario")
    nSal = input("Introducir el nuevo salario")
    cursor.callproc('tablaemp.cambiarsalario', (nEm,nSal))
    print(nEm,nSal)
except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()