import coche


# import + nombre clase(constructor)
# con import traemos todo el fichero y las clases que contenga
# por eso s epueen utilizar aqui coche y cocheDeportivo
coche1 = coche.Coche("SEAT","Negro")
print(f'Marca: {coche1.marca}, Color: {coche1.color}')

coche_lujo = coche.CocheDeportivo("Volkswagen","Rojo", 240)
print(f'CocheDeportivo Marca: {coche_lujo.marca}, Color: {coche_lujo.color}, caballos: {coche_lujo.caballosF}')
