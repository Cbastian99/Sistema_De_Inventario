#Sistema De Inventario

# Lista donde se almacenarán los productos
inventario = []

while True:

    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Ingrese el nombre del producto: ")

        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))

        productos = {
            "nombres": nombre,
            "precios": precio,
            "cantidades": cantidad
        }

        inventario.append(productos)

        print("Producto agregado correctamente.")

    elif opcion == "2":

        if len(inventario) == 0:
            print("El inventario esta vacio.")
        
        else:
            print("\n--- INVENTARIO ---") 
        
            for producto in inventario:
                print(
                    "Producto:", productos["nombre"],
                    "| Precio:", productos["precio"],
                    "| Cantidad:", cantidad["cantidad"]
                )

    elif opcion == "3":
        print("Calcular estadísticas seleccionado")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
        
    















    







