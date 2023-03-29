import cx_Oracle

connetion=cx_Oracle.connect("system", "netoracle","localhost/XE")

cursor=connetion.cursor()
try:
    consultabaja= ("delete from emp where emp_no=:p1")
    numeroEmpleado=int(input("Numero de empleado a eliminar: "))
    cursor.execute(consultabaja,(numeroEmpleado,))
    if cursor.rowcount>0:
        print("Registro eliminado satisfactoriamente")
    else:
        print("Dato no encontrado")

    connetion.commit()
except connetion.Error as error:
    print ("Error:" , error)
cursor.close()
connetion.close()