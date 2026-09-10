list_numbers = [1,2,3,4,5]
list_strings = ['a', 'b']
list_mix = [2, 'z', 4, 'hola']

shopping_cart = ["Laptop", "Monitor"]

print(type(list_mix))

print(list_numbers)
list_numbers.append(77)
list_numbers.append(66)
list_numbers.append(55)

print(list_numbers)


list_numbers.remove(55)
print(list_numbers)

print("Count ayuda a saber cuantos elementos de x hay", list_numbers.count(2))
