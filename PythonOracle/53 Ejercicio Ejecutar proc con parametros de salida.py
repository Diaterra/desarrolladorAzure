import cx_Oracle

connection=cx_Oracle.connect("system", "netoracle","localhost/XE")
cursor=connection.cursor()

try:
    dp = input("Número de departamento:")
    loc = cursor.var(cx_Oracle.STRING)

    args = (dp, loc)
    cursor.callproc('DEVOLVER_LOC', args)
    print(loc.getvalue())

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()