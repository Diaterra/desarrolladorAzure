import cx_Oracle
import sys

connection=cx_Oracle.connect("system", "netoracle","localhost/XE")
cursor=connection.cursor()

try:
    dp=input("numero de departamento")
    nombre=input("nombre del departamento")
    localidad=input("localidad")
    cursor.callproc("PROC_INSERTDEPt",(dp,nombre,localidad))
    if cursor.rowcount>0:
        print("Registro insertado satisfactoriamente")
    else:
        print("Dato no encontrado")
except connection.Error as error:
    print("Error: ", error)

connection.close()