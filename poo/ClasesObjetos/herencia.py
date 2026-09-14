class Animal:
    def comer(self):
        print("Como muchas veces al día")
        
    def dormir(self):
        print('Duermo muchas horas')
        
class Perro(Animal):
    
    def hacer_sonido(self):
        print("Puedo ladrar")
    
    def dormir(self):
        print("Duermo 10 horas al día")
    
# Programa principal

print("Ejemplo de herencia en Python")

print('Clase padre, soy un Animal')

animal1 = Animal()

animal1.comer()
animal1.dormir()


print("\n Clase hija, soy un Perro")
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()