# AND
age = 11
licensed = True
if age >= 18 and licensed:
    print("Puedes manejar un carro")
else:
    print("No puedes manejar un carro")
    
    
# OR
is_student = False
membership = True

if is_student or membership:
    print("Bienvenido!")
    
# NOT
is_admin = False

if not is_admin:
    print("Acceso denegado")    
    
# Short Circuit
name = "False"
print(name and name.upper())