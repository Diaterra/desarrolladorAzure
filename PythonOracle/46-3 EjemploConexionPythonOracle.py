import cx_Oracle

connection=cx_Oracle.connect("system", "netoracle","localhost/XE")

cursor=connection.cursor()

try:
    inputfuncion=input('Introduce la funcion')
    consulta=("select plantilla.apellido, plantilla.salario, hospital.nombre from plantilla join hospital on plantilla.hospital_cod=hospital.hospital_cod where upper(funcion)=upper(:p1)")
    cursor.execute(consulta,(inputfuncion,))
    for ape,sal,hosp in cursor:
        print(ape,sal,hosp)
except connection.Error as error:
    print("Error: ", error)
connection.close()