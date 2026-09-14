# La función zip() en Python sirve para combinar dos o más iterables elemento por elemento.

nombre = ['Iram', 'Fernando', 'Felipe']
edad = [27,48,49]
ciudad = ['Monterrey', 'San José', 'Cuba']

# Combinar los elementos correspondientes usando la función zip

personas = zip(nombre, edad, ciudad)

for persona in personas:
    print(persona)