class CodigoEAN:
    codigo=""
    digitoDeControl=""
    NumeroDeControl=""
    resultado=""
    def validar(self):
        self.codigo=input("INTRODUZCA UN CODIGO EAN (8 O 10 CARACTERES)")
        self.digitoDeControl=self.codigo[(len(self.codigo))-1]
        sumapares=0
        sumaimpares=0
        suma=0
        for i in self.codigo:
            if int(i)%2==0:
                sumapares += int(i)
        for i in self.codigo:
            if int(i) % 2 != 0:
                sumaimpares += int(i)
        if len(self.codigo)==8:
            sumaimpares= sumaimpares*3
        else:
            sumapares=sumapares*3
        suma=sumapares+sumaimpares
        resto=suma%10
        if resto==self.digitoDeControl:
            self.resultado="ES VALIDO"
        else:
            self.resultado="NO VALIDO"
        return self.resultado
    def __str__(self):
        return "Codigo EAN: " + str(self.codigo) + str(self.resultado)

