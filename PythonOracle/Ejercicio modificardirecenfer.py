import cx_Oracle

connection=cx_Oracle.connect("system", "netoracle","localhost/XE")
cursor=connection.cursor()

try:
    insc=input("Introducir el numero de inscripcion")
    dire=input("Introducir la nueva direccion")
    cursor.callproc('MODIDIRECENF',(insc,dire))


except connection.Error as error:
    print("Error: ", error)

connection.close()
