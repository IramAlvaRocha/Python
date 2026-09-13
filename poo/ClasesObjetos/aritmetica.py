class Aritmetica:
  
    def __init__(self, operando1 = None, operando2 = None):
        self._operando1 = operando1
        self._operando2 = operando2
    
    @property
    def operador1(self):
        return self._operando1
    
    @operador1.setter
    def operador1(self, operador1):
        self._operando1 = operador1
        
    @property
    def operador2(self):
        return self._operando2
    
    @operador2.setter
    def operador2(self, operador2):
        self._operando2 = operador2
    
    def sumar(self):
        return f"Suma: { self._operando1 + self._operando2 }"
    
    def restar(self):
        return f"Resta: {self._operando1 - self._operando2}"

    def dividir(self):
        return f"Division: {self._operando1 / self._operando2}"
    
    def multuplicar(self):
        return f"Multiplicación: {self._operando1 * self._operando2}"

aritmetica = Aritmetica();
aritmetica.operador1 = 2
aritmetica.operador2 = 2

print ( f''' 
{aritmetica.sumar()}
{aritmetica.restar()}
{aritmetica.multuplicar()}
{aritmetica.dividir()}
       ''')