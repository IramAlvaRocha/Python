print("Imprimir del 1 al 5 de forma recursiva")

# Definir la función recursiva

def function_recursiva(numero):
    # Caso base
    if numero == 1 :
        print(numero, end=" ") # Numeros del 1 al 5
    else:
        # Caso recursivo
        function_recursiva(numero - 1)
        print(numero, end=" ")
        
        
function_recursiva(5)