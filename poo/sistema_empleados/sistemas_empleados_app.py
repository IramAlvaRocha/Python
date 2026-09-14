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


# Obtener el numero de empleados por departamento
print("Empleados en el departamento de ventas:"
      f"{empresa1.obtener_numero_empleados_por_departamento("Ventas")}")

# Mostrar todos los empleados de la empresa

print(f'La empresa tiene: {empresa1.obtener_total_empleados()}')