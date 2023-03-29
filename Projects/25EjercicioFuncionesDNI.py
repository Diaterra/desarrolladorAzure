def dni(ndni):
    resultado1 = ndni % 23
    letrasDni = "TRWAGMYFPDXBNJZSQVHLCKET"
    return letrasDni[resultado1]

letra= dni(53256987)
print(letra)


letra2=dni(55256999)
print(letra2)
