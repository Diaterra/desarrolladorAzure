import cx_Oracle
import sys

class crud:
    hospt_cod = 0
    doc_no = 0
    ape = ""
    esp = ""
    sal = 0
    cursor=""
    connection=""
    def __init__(self):
        self.connection=cx_Oracle.connect("system", "netoracle","localhost/XE")
        self.cursor=self.connection.cursor()
    def altaEmpleado(self, hospt_cod,doc_no,ape,esp,sal):
        try:
            consulta1 = ("insert into doctor values(:p1,:p2,:p3,:p4,:p5)")
            self.cursor.execute(consulta1, (hospt_cod, doc_no, ape, esp, sal))
            self.connection.commit()
        except self.connection.Error as error:
            return "Error: ", error
    def bajaEmpleado(self,doc_no):
        try:
            consulta2 = ("delete from doctor where doctor_no=:p1")
            self.cursor.execute(consulta2, (doc_no,))
            self.connection.commit()
            if self.cursor.rowcount > 0:
                return "Registro borrado correctamente"
            else:
                return "Dato no encontrado"
        except self.connection.Error as error:
            return "Error: ", error
    def modificarEmpleado(self,espec, doctor_no):
       try:
            consulta3 = ("update doctor set especialidad=:p1 where doctor_no=:p2")
            self.cursor.execute(consulta3, (espec, doctor_no))
            self.connection.commit()
            if self.cursor.rowcount > 0:
                return "Registro actualizado correctamente"
            else:
                return"Dato no encontrado"
       except self.connection.Error as error:
             return "Error: ", error

    def consultaDatos(self):
        try:
            consulta4=("select * from doctor")
            self.cursor.execute(consulta4)
            for hosp,doct,ape,esp,sal in self.cursor:
                print(hosp,doct,ape,esp,sal)
        except self.connection.Error as error:
            return "Error: ", error
    def salir(self):
        self.connection.close()
        sys.exit()