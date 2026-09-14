class Monitor:
    
    contador_monitores = 0
    
    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.id = Monitor.contador_monitores
        self.marca = marca
        self.tamanio = tamanio
        
    def __str__(self):
        return f'''
            Id = {self.id}
            Marca = {self.marca}
            Tamaño = {self.tamanio}
        '''
if __name__ == '__main__':
    monitor1 = Monitor('HP', '24"')
    print(monitor1)