
print("Hello world")
# comentario de linea

""""
comentario de bloque
"""
name = "Oscar"
lastName = "Galan"
edad = 28

print(name)
print(lastName)

print(name +' '+lastName)
print(f'{name} {lastName} y tengo {edad} años')
print(name*5)

num1 = 20
num2 = 5
result = num1 + num2
print(result)

list = ["Java", "Python","C#","JavaScript","PHP","Angular"]
print(list)
print(list[-1]) # ultimo lemento de la lista
list[1] = "Flutter"
print(list)
list.append("Bootstrap")
print(list)
list.insert(3, "CSS")  # añadir css en el tercer indice
print(list)



# Tupla (array que es inmutable, no se puede modificar)
# cuando la tupla tiene solo un dato, termina con ,
# tupla("Java", )   # tupla con un solo dato
tupla = ("Java", "Python","C#","JavaScript","PHP","Angular")
print(tupla)
print(tupla[1])



# Diccionarios
data = {'name': 'Oscar', 'lastName': 'Galan', 'edad':32}
print(data)
print(data['lastName'])
print(f'Mi nombre es: {data["name"]}')

data['city'] = 'EdoMex'
print(data)

del data['edad']   # palabra reservada para eliminar
print(data)

print(len(data))  # para saber cuantas claves tiene un diccionario (tamaño)
