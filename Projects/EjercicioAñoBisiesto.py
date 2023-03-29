year=int(input("Introducer the year: "))
if year%4==0:
    if year%100==0 and year%400==0:
        print("year bisiesto")
    else:
        print("year bisiesto")
else:
    print("year no bisiesto")



