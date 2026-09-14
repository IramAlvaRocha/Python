from functools import reduce

print('*** Funciones lambda ***')

# Funcion para regresar un número elevado al cuadradon, sin usar lambda
def cuadrado(numero):
    return numero ** 2


print(f'El cuadrado de 5 es: {cuadrado(5)}')


# Funciones lambda (Anonimas)

cuadradoLambda = lambda num: num ** 2

print(f'El cuadrado de 7 es: {cuadradoLambda(7)}')

# Con map y lambda
# Creamos una lista de números

numeros = [1,2,3,4,5]

# Aplicar una función lambda para obtener el cuadrado de cada número

cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)


# Trabajando con filter  y lambda

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)

# Reduce y Map

suma_iterativa = reduce(lambda x, y: x + y, numeros)
print(suma_iterativa)