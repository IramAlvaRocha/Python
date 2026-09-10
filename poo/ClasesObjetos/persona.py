# Definición de una clase

class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
           
    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        ''')
        
# Creación de objetos
if __name__ == '__main__':
    #Creación de un primer objeto
    person1 = Persona("Iram", "Rocha"); #Se crea un objeto vacío en memoria
    person1.mostrar_persona();
    
    # Creamos un segundo objeto
    person2 = Persona("Felipe", "Herrera")
    person2.mostrar_persona()    
    
    
    