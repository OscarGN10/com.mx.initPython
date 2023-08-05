edad = int(input("Introduce tu edad: "))


if edad >= 18:
    print('eres mayor de edad')
else:
    print('eres menor de edad')    


if not edad < 50:  #   se puede usar if not 'o' !=
    print('eres viejo xD')


edad2 = int(input("Intorduce la otra edad: "))
mes = int(input("Introduce el numero de mes en que naciste: "))
if edad >= 18:
    print("Eres mayor de EDAD")
    if mes == 1:
        print("naciste en enero")
    elif mes == 2:
        print("naciste en febrero")
else:
    print("Eres menor de EDAD")
    if mes == 3:
        print("naciste en marzo")
    elif mes == 4:
        print("naciste en abril")