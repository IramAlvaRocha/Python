number = 1

while number <= 10:
    print(number)
    number+=1
else:
    print("Termina while")
 
 
 
response = ''

while response.lower() != 'bye':
    response = input("Escribe 'bye' para salir")
else: 
    print("Terminamos")