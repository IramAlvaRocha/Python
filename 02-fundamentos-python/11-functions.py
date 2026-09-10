# Parametros
def hello(name = "Felipe"):
    print(f"Hola, {name}")

# Argumentos
hello("Iram")
hello("Fernando")
hello()



def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return 0
    
print(big_function(1,2,3,4,5,6,7, num1 = 1, num2=2))