class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    # Sobreescribir el metodo __str__
    def __str__(self):
        return f''' 
        nombre = {self.nombre}
        apellido = {self.apellido}
        dir. memoria = {super.__str__(self)}
        '''
        
        
persona1 = Persona('Iram', 'Rocha')
print(persona1)