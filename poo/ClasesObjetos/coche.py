class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca      # Atributo público
        self._modelo = modelo   # Atributo protegido
        self._color = color    # Atributo privado
        
    def conducir(self):
        print(f'''Conduciendo el coche
              Marca: {self._marca}
              Modelo: {self._modelo}
              Color: {self._color}
        ''')
        
    def get_marca(self):
        return self._marca
    
    def set_marca(self, marca):
        self._marca = marca
    
    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, modelo):
        self._modelo = modelo
  
    def color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color
        
     
        
# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche("Toyota", "Yaris", "Negro")
    coche1.conducir()
    
    #No deberiamos acceder a los atributos que no sean públicos
    coche1.set_marca("Toyota 2")
    coche1.set_modelo("Corolla")
    coche1.set_color("Blanco")
    
    coche1.conducir()