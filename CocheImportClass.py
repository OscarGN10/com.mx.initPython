from coche import Coche, CocheDeportivo
# from Clases.coche import Coche, CocheDeportivo
# por si el fichero esta en una carpeta (paquetes)

# del fichero coche, importame unicamente las clases coche y deportivo
# con esto traemos unicamente las clases que queramos
coche1 = Coche("SEAT","Negro")
print(f'Marca: {coche1.marca}, Color: {coche1.color}')

coche_lujo = CocheDeportivo("Volkswagen","Rojo", 240)
print(f'CocheDeportivo Marca: {coche_lujo.marca}, Color: {coche_lujo.color}, caballos: {coche_lujo.caballosF}')
