class Persona: 
    # Atributo de clase
    contador_personas = 0
    
    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar_persona(self):
        print(f'Persona: {self.id}, { self.nombre}, { self.apellido}')
        
    @staticmethod
    def contador_personas_estatico():
        print("Método Estatico")
        return Persona.contador_personas
    
    @classmethod
    def get_contador_personas_clases(cls):
        return cls.contador_personas
    
if __name__ == '__main__':
    persona = Persona("Iram", "Rocha")
    persona.mostrar_persona()
    
    persona2 = Persona("Felipe", "Acosta")
    persona2.mostrar_persona()
    
    # Imprimir el valor de contador de objetos de personas
    print(f"Contador objetos personas: {Persona.contador_personas}")
    print(f"Contador de objetos persona (static): {Persona.contador_personas_estatico()}")
    print(f"Contador de objetos persona (cls): {Persona.get_contador_personas_clases()}")