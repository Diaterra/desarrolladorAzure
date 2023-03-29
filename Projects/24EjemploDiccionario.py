provincia=dict()

provincia= {
    924: "Badajoz",
    956: "Cadiz",
    958: "Granada",
    959: "Huelva",
    91: "Madrid",
    95: "Málaga",
    968: "Murcia",
    923: "Salamanca",
    95: "Sevilla",
    922: "Sta. Cruz de Tenerife",
    975: "Soria",
    96: "Valencia",
    976: "Zaragoza"

}

print(provincia)
dato=(provincia.get(91))
print(dato)
for clave,valor in provincia.items():
    print("prefijo: ", clave, "Provincias: ", valor)
print(provincia.items())
print("---------------------------------------------")
print(len(provincia))

print("---------------------------------------------")
provincia.setdefault(925,"Toledo")
for clave,valor in provincia.items():
    print("prefijo: ", clave, "Provincias: ", valor)

provincia.setdefault(925,"Toledo")
for clave,valor in provincia.items():
    print("prefijo: ", clave, "Provincias: ", valor)

