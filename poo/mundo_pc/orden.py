from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Orden:
    contador_ordenes = 0
    
    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self.computadoras = computadoras
        
    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)
        
    def __str__(self):
        computadoras_str = ''
        for compu in self.computadoras:
            computadoras_str += '\n' + compu.__str__()
            
        return f'''
        Orden: {self.id_orden}
        Computadoras: {computadoras_str}
        '''

if __name__ == '__main__':
    lista_computadoras = []
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', '24"')
    
    computadora1 = Computadora('Gamer', monitor1, teclado1, raton1)
    
    lista_computadoras.append(computadora1)
    
    orden1 = Orden(lista_computadoras)
    
    print(orden1)