lista_compras = [] # creamos una lista vacia dond el usuario va almacenar los items

# 2. Iniciar el bucle while
opcion = "" # se crea una variable vacia donde se guarda la opcion que escoja el usuario
while opcion != "4": # se inicia el bucle while y se repetira mientras el usuario no escoja el numero 4 en este caso que es la opcion salir
    print("\n1. Agregar ítem")
    print("2. Eliminar ítem")
    print("3. Ver lista")       # se imprime el menu 
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ") # se le pide al usuario, con imput para que escoja un opcion
    
    if opcion == "1":
        item = input("¿Qué deseas agregar?: ")
        lista_compras.append(item)               # aca si el usuaruio escoge el 1 con append() se agrega un item
        print("Agregado.")
        
    elif opcion == "2":
        item = input("¿Qué deseas eliminar?: ")
        lista_compras.remove(item)               # aca si el usuario escoge el 2 con remove() le decimos que diga cual item elimina
        print("Eliminado.")
        
    elif opcion == "3":
        print("\nTu lista actual:")
        print(lista_compras)                    # aca si escoge el 3 se imprime la lista par poder ver la lista completa
        
    elif opcion == "4":
        print("Saliendo...")                    # aca si escoge el 4 como mencionamos arriba se termina el bcle y se sale del menu 
        
    else:
        print("Opción no válida.")              # si escoge un numero diferente a los del menu o no hace nada se le muestra un mensaje 


        
        