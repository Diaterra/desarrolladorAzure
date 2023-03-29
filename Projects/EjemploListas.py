print("Creando listas")
edades=[20,35,40]

print("Edad 1", edades[0])

nombres= ["Luis","Juan","Pedro"]

print("nombre2", nombres[1])

nombres.append("Esteban")
print(nombres)

nombres.insert(2,"Marcos")
print(nombres)

nombres.remove("Luis")
print(nombres)

del nombres[1]
print(nombres)

nombres.append("Diana")
print(nombres)

del nombres[0:3]
print(nombres)

nombres=["Diana","Ger","Gon","Giovi","Aki"]
print(nombres)

longitudNombres=len(nombres)
print(longitudNombres)

"""es el for each"""
for i in nombres:
    print(i)

print("------------------------")

"""es el for comùn"""

for dato in range(len(nombres)):
    print(nombres[dato])

print("------------------------")

print("Diana" in nombres)

print("------------------------")

notas=[1,10,1,0,8,7,3,35]
notas.sort()
print("nota mas baja",notas[0])
print("------------------------")
print(notas)

print("------------------------")
notas.sort(reverse=True)
print("nota mas alta", notas[0])
print(notas)


print("--------CREANDO TUPLAS----------------")

diasDeLaSemana=("Lunes","Martes","Miercoles","Jueves","Viernes")