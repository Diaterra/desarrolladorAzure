import cx_Oracle

connection=cx_Oracle.connect("system", "netoracle","localhost/XE")

cursor=connection.cursor()

try:
    miOficio=input("Introduce Oficio del empleado: ")
    consulta=("SELECT APELLIDO, OFICIO, SALARIO FROM EMP WHERE UPPER(OFICIO)=UPPER(:p1)")

    cursor.execute(consulta,(miOficio,))
    for ape,ofi,sal in cursor:
        print("Apellido: ", ape)
        print("Oficio: ", ofi)
        print("Salario: ", sal)
except connection.Error as Error:
    print("Error: ",error)

connection.close()