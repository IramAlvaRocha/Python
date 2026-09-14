print("** Sistema de inventarios con funciones **")

# Inventario
inventario = [
    {
        "Id": 1,
        "Nombre": "Camisa azul",
        "Precio": 100,
        "Cantidad": 50
    },
    {
        "Id": 2,
        "Nombre": "Camisa roja",
        "Precio": 90,
        "Cantidad": 22
    }
]

def mostrar_inventario():
    print("")
    print("=== Inventario actual ===")
    for producto in inventario:
        print(f"""
              Id : {producto["Id"]}
              Nombre : {producto["Nombre"]}
              Precio : {producto["Precio"]}
              Cantidad : {producto["Cantidad"]}
              """)

def agregar_producto():
    
    id = input("Ingresa el id del producto: ")
    nombre = input("Ingresa el nombre del producto: ")
    precio = input("Ingresa el precio del producto: ")
    cantidad = input("Ingresa la cantidad del producto: ")
    
    inventario.append({
        "Id": id,
        "Nombre": nombre,
        "Precio": precio,
        "Cantidad": cantidad
    })


def buscar_producto_por_id():
    id = int(input("Ingresa el id del producto a buscar: "))
    for producto in inventario:
        if producto.get("Id") == id:
            print(producto.get("Id"))
            print(producto.get("Nombre"))
            print(producto.get("Precio"))
            print(producto.get("Cantidad"))

def detener():
    return False

if __name__ == "__main__":
    while True:
        print("""
            Menú:
            1. Mostrar inventario
            2. Agregar nuevo producto
            3. Buscar producto por ID
            4. Salir

            """)

        opcion = int(input("Proporciona una opción (1-4): "))
        
        if opcion == 1:
            mostrar_inventario()
        if opcion == 2:
            agregar_producto()
        if opcion == 3: 
            resultado = buscar_producto_por_id()
            print(resultado)
            
        if opcion == 4:
            break;
        