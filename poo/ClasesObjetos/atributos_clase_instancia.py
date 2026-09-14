class Persona:
    atributo_clase = 0
    
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia


# Programa principal

if __name__ == "__main__":
    print("=== Atributos de clase ===")
    print(f"Atributos de clase: {Persona.atributo_clase}")
    # Modificamos el atributo de clase
    Persona.atributo_clase = 10
    print(f"Atributo de clase modificado: {Persona.atributo_clase}")
    
    # Creamos objetos
    persona1 = Persona(15)
    print(f"Atributo de clase desde la instancia persona 1: {persona1.atributo_clase}")
    print(f"Atributo de instancia desde la instancia persona 1: {persona1.atributo_instancia}")
    
    # Creamos persona 2
    persona2 = Persona(30)
    print(f"Atributo de clase desde la instancia persona 2: {persona2.atributo_clase}")
    print(f"Atributo de instancia desde la instancia persona 2: {persona2.atributo_instancia}")
        
    
    