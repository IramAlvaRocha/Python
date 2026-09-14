print('*** Funciones lambda ***')

# Funcion para regresar un número elevado al cuadradon, sin usar lambda
def cuadrado(numero):
    return numero ** 2


print(f'El cuadrado de 5 es: {cuadrado(5)}')


# Funciones lambda (Anonimas)

cuadradoLambda = lambda num: num ** 2

print(f'El cuadrado de 7 es: {cuadradoLambda(7)}')