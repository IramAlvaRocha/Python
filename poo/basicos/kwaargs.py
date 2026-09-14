# Recibir n cantidad de parametros llave-valor con **kwargs

def detalle_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} - {valor}")
        
detalle_persona(nombre = "Iram", puesto = "Python dev", salario = "50,000.00 MXN")

