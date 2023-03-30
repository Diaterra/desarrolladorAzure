import cx_Oracle

connection=cx_Oracle.connect("system", "netoracle","localhost/XE")
cursor=connection.cursor()

try:
    ape=cursor.var(cx_Oracle.STRING)
    sex=cursor.var(cx_Oracle.STRING)
    nss=input("Introducir el numero de NSS")
    args=(nss,ape,sex)
    cursor.callproc('DEVOL_ENF', args)
    print(ape.getvalue(), sex.getvalue())

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()