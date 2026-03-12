#Sistema De Inventario



# Solicitar al usuario que ingrese el nombre del producto, su precio y la cantidad disponible
nombre = input("Ingrese el nombre del producto: ")


while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break    
    except ValueError:
        print("Por favor, ingrese un número válido para el precio.")



while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break    
    except ValueError:
        print("Por favor, ingrese un número válido para la cantidad.")

# Calcular el costo total del producto multiplicando el precio por la cantidad
costo_total = precio * cantidad 

# Mostrar el resumen del inventario al usuario
print("\n===== RESUMEN DEL INVENTARIO =====")
print(f"\nProducto: {nombre}")
print(f"Precio unitario: ${precio:.0f}")
print(f"Costo total: ${costo_total:.0f}")










    







