# La diferencia entre las listas y las tuplas, es que las tuplas son
# inmutables

my_tuple = (1,2,3,4,5,6, "Hola", True, False, 3, 2, 2, 5, "Adiós")

print(my_tuple)

# Cuenta la cantidad de veces que esta en la tupla
print(my_tuple.count(2))

# Muestra el indice de donde se encuentra el valor pasado como argumento,
# si ese valor aparece más de una vez, se regresa el primero que encuentra
print(my_tuple.index(3))


#  Marcará un error debido a que no se pueden mutar
# my_tuple[2] = 5
print(my_tuple)

week = ("Lunes", "Martes")

print(week)