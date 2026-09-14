def factorial(numero):
    # Caso base 
    if numero == 0 or numero == 1:
        print(f"Resultado factorial parcial de {numero} es: 1")
        return 1
    else:
        factorial_parcial = numero * factorial(numero - 1)
        print(f"Resultado del factorial parcial {numero} : {factorial_parcial}")
        return factorial_parcial;
    
resultado = factorial(5)

print(f"El resultado es factorial final es: {resultado}")