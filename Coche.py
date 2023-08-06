class Coche:
     # pass es para inicializar una clase vacia, cuando ya tenga datos, 
     # borrar pass
    #pass
    marca = ""
    color = ""
    __encendido = True  # __ para encapsular la varibale "private"
    velocidad = 0


    def get_encnedido(self): # se debe hacer un emtodo ge tp obtener el valor
        return self.__encendido
    

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        
    #funcion para encender el coche
    def encender(self):
        
        if self.get_encnedido == True:
            print(f"El coche esta encendido y va ha una velocidad de {coche1.velocidad} km/h")
        else:
            print("El coche esta apagado")
    
    def set_velocidad(self, velocidad):
        self.velocidad = velocidad


# HERENCIA poner () la clase padre               Herencia Multiple
class CocheDeportivo(Coche):  # class CocheDeportivo(Coche, Coche4x4):
   # caballosF = 60
    
    def __init__(self, marca, color, caballosF):
        self.marca = marca
        self.color = color
        self.caballosF = caballosF