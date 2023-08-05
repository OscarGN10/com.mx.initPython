name = input("introduce tu nombre: ")
last_Name = input("introduce tu apellido: ")
edad = input("introduce tu edad: ")

print(f'Mi nombre es {name} {last_Name} y mi edad es {edad} ')
#print("Mi nombre es: "+name+" "+last_Name+" y mi edad es: "+edad)
#print(name)

# num1 = int(input("Primer numero: "))
num1 = input("Primer numero: ") 
num2 = input("Segundo numero: ")
# todo lo ingresado llega en string, hay que convertirlo a numerico
print(int(num1)+int(num2))  

#str() = string
#bool() = boolean
#int()
#float()

num3 = int(input("introduce numero: "))

"""" SI el usuario ingresa un numero mayor a 0 devovlera true
"""
print(bool(num3))
