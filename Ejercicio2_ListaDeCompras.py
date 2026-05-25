# 1. Crear la lista vacía
lista_compras = []

# 2. Iniciar el bucle while
opcion = ""
while opcion != "4":
    print("\n1. Agregar ítem")
    print("2. Eliminar ítem")
    print("3. Ver lista")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    # 3. Estructura condicional if/elif/else
    if opcion == "1":
        item = input("¿Qué deseas agregar?: ")
        lista_compras.append(item)
        print("Agregado.")
        
    elif opcion == "2":
        item = input("¿Qué deseas eliminar?: ")
        lista_compras.remove(item)
        print("Eliminado.")
        
    elif opcion == "3":
        print("\nTu lista actual:")
        print(lista_compras)
        
    elif opcion == "4":
        print("Saliendo...")
        
    else:
        print("Opción no válida.")