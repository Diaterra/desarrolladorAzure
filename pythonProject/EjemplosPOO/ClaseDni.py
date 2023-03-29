class Dni:
    numeroDni=0
    letrasDni=""
    resultadoLetra=""
    def __init__(self):
        self.letrasDni="TRWAGMYFPDXBNJZSQVHLCKET"
    def mostrarletra(self,numeroDni):
        self.numeroDni=numeroDni
        resultado=self.numeroDni%23
        self.resultadoLetra=self.letrasDni[resultado]
        #return self.resultadoLetra
    def __str__(self):
        return "numeroDni: " + str(self.numeroDni) + ", tu numero de letra es: " + str(self.resultadoLetra)


