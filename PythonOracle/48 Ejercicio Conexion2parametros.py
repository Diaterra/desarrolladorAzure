import cx_Oracle

connection = cx_Oracle.connect("system", "netoracle","localhost/XE")
cursor = connection.cursor()

try:
    salarMin=int(input("Introducir el salario minimo"))
    salarMax=int(input("Introducir el salario maximo"))
    consulta=("select apellido, oficio,salario from emp where salario between :sMin and :sMax")
    cursor.execute(consulta,(salarMin,salarMax))
    for ape,ofi,sal in cursor:
        print(ape,ofi,sal)
except connection.Error as error:
    print("Error: ", error)

connection.close()