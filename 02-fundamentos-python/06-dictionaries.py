user = {
    "name": "Iram Remigio",
    "age": 29,
    "email": "iram@gmail.com",
    "active": True,
    (19.2, -88.93) : "Cancun, México"
}

user["name"] = "Remigio"
user["age"] = 27

print(user["name"])

print(user[(19.2, -88.93)])

# items, values, keys
print(user.items())
print(user.values())
print(user.keys())

# Agregar cosas al diccionario

user["country"] = "Mexico"
print(user["country"])