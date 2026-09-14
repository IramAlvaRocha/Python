#   POLIMORFISMO SIGNIFICA QUE SE VA A COMPORTAR DE MULTIPLES MANERAS DEPENDIENDO DEL TIPO DE DATO EN EL QUE ESTAMOS TRABAJANDO
#  Y SI ES QUE EXISTE ALGUNA SOBREESCRITURA DEL MÉTODO DE LA CLASE PADRE


class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')
        
        
class Perro(Animal):
    
    # OVERRIDE DEL MÉTODO
    def hacer_sonido(self):
        print('Puedo ladrar')
        
        
class Gato(Animal):
    def hacer_sonido(self):
        print("Puedo maullar")
        
        
# Función polimorfica
def hacer_sonido_animal(animal):
    animal.hacer_sonido()
        
print("Ejemplo de Polimorfismo")
print("Clase Padre Animal:")
animal1 = Animal()
hacer_sonido_animal(animal1)

print('Clase hija Perro:')
perro1 = Perro()
hacer_sonido_animal(perro1)

print('Clase hija Gato:')
gato1 = Gato()
hacer_sonido_animal(gato1)