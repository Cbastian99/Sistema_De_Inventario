# Sistema De Inventario


# Lista donde se almacenarán los productos
inventario = []

# Funcion para agregar producto
def agregar_producto():
    while True:
            nombre = input("Ingrese el nombre del producto: ")
            if nombre == "":
                print("Debe ingresar un nombre")
            else:
                break

    precio = float(input("Ingrese el precio: $"))
    cantidad = int(input("Ingrese la cantidad: "))

    producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

    inventario.append(producto)

    print("Producto agregado correctamente.".upper())



# Funcion para Mostrar inventario
def mostrar_inventario():
    print("\n--- INVENTARIO ---") 
        
    for producto in inventario:
        print(
            "Producto:", producto["nombre"],
            "| Precio:", producto["precio"],
            "| Cantidad:", producto["cantidad"]
        )


# Funcion para calcular estadisticas
def calcular_estadisticas():
    total_productos = len(inventario)
    total_unidades = 0
    valor_total = 0
    
    for producto in inventario:
         total_unidades += producto["cantidad"]
         valor_total += producto["precio"] * producto["cantidad"]

    print("\--- RESUMEN INVENTARIO---")
    print("Total productos:", total_productos)
    print("Total unidades:", total_unidades)
    print("Valor total:$", valor_total)







# MENU PRINCIPAL
while True:
        
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        
        opcion = input("Seleccione una opción: ")
      
        if opcion == "1":
            agregar_producto()
        elif opcion == "":
            print("Ingrese una opcion valida")

        elif opcion == "2":

            if len(inventario) == 0:
                print("El inventario esta vacio.")
            
            else:
                mostrar_inventario()
                
        elif opcion == "3":
            calcular_estadisticas()
            
        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Ingrese una opcion valida.")


# Resumen de la semana
# Se creo un sistema de inventario usando python donde se aplicaron
# listas, diccionarios, condicionales, bucles y funciones para registrar
# productos, mostrar inventario, y calcular estadisticas basicas
        
    















    







