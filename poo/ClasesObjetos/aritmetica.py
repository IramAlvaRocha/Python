class Aritmetica:
    # Python solamente toma en cuenta el último constructor
    def __init__(self, operando1):
        self.operando1 = operando1
    
    def __init__(self, operando1 = None, operando2 = None):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def sumar(self):
        return f"Suma: { self.operando1 + self.operando2 }"
    
    def restar(self):
        return f"Resta: {self.operando1 - self.operando2}"

    def dividir(self):
        return f"Division: {self.operando1 / self.operando2}"
    
    def multuplicar(self):
        return f"Multiplicación: {self.operando1 * self.operando2}"

aritmetica = Aritmetica(5, 2)

print(aritmetica.sumar())
print(aritmetica.restar())
print(aritmetica.dividir())
print(aritmetica.multuplicar())

artimetica2 = Aritmetica(4);
artimetica2.operando2 = 2;
artimetica2.sumar()