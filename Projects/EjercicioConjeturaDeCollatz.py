number=int(input("Introduzce un numero: "))
if number==1:
    print(f"{number}")
else:
    while number!=1:
        if number%2==0:
            number=number/2
            print(f"{number}")
        else:
            number=(number*3)+1
            print(f"{number}")

