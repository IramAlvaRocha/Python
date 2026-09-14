from sistema_empleados.empleado import Empleado
from sistema_empleados.empresa import Empresa


print("==== Sistema de Empleados ====")

# Creamos una instancia de una empresa

empresa1 = Empresa('Global Mentoring')

# Contratar algunos empleados 

empresa1.contratar_empleado("Iram", "Desarrollo")
empresa1.contratar_empleado("Fer", "Analisis")
empresa1.contratar_empleado("Karely", "Analisis")
empresa1.contratar_empleado("Felipe", "Desarrollo")
empresa1.contratar_empleado("Diego", "Desarrollo")


# Obtener el total de objetos empleados

print(f"Total de empleados: {Empleado.obtener_total_empleador()}")
