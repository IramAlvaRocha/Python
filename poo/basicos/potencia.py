# Calcular la potencia de un número base A a la potencia B

# Definimos la funcion
# def calcular_potencia(base, potencia):
#     total = base * potencia
#     if potencia == 0:
#         print(f"El resultado parcial de {base} elevado a {potencia} es: {total}")

#     else: 
#         calcular_potencia(base, potencia-1)
#         print(f"El resultado parcial de {base} elevado a {potencia} es: {total}")        
#     return total

def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    else: 
        return base * calcular_potencia(base, exponente - 1)        
        
print(calcular_potencia(2,3))
print(calcular_potencia(10,0))
print(calcular_potencia(2,4))