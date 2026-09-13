class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca      # Atributo protegido
        self._modelo = modelo   # Atributo protegido
        self._color = color    # Atributo protegido
        
    def conducir(self):
        print(f'''Conduciendo el coche
              Marca: {self._marca}
              Modelo: {self._modelo}
              Color: {self._color}
        ''')
    
    @property # Definir el metodo get de manera mas pythonica
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
        
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
        
     
        
# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche("Toyota", "Yaris", "Negro")
    coche1.conducir()
    
    #No deberiamos acceder a los atributos que no sean públicos
    coche1.marca = ("Toyota 2")
    coche1.modelo = ("Corolla")
    coche1.color = ("Blanco")
    
    coche1.conducir()
    
    # Atributo de marca coche 1
    print(f"Atributo de marca coche 1: {coche1.marca}")
    coche1.marca = "BYD"
    print(f"{coche1.marca}")
    
    
    # Intentar agregar un nuevo atributo (De manera dinamica)
    setattr(coche1,"nuevo_atributo", "valor")
    coche1.otro = "Otro valors"
    
    print(coche1.nuevo_atributo)
    print(coche1.otro)