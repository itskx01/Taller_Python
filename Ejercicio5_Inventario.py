inventario = []
# Hacmeos un diccionario vaio
def agregar_producto():
    nombre = input("Nombre del producto: ").strip().lower()
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad inicial en stock: "))
    
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    inventario.append(nuevo_producto)
    print(f"✅ ¡Producto '{nombre}' agregado al inventario!")

"""
Creamos la variable agregar_productos dentro creamos las variables (nombre,precio,cantidad) que se pueda ingresar datos, hacemos un diccionario donde guardanmos tres campos fijos, para despues agregar a inventario el diccionario que creamos "nuevo_producto" y despues lo imprimimos para ver el resultado 
"""

def realizar_venta():
    nombre_buscar = input("¿Qué producto deseas vender?: ").strip().lower()
    
    for producto in inventario:
        if producto["nombre"] == nombre_buscar:
            cantidad_vender = int(input(f"¿Cuántas unidades de '{nombre_buscar}' vas a vender?: ")) #Creamos la funcion realizar_venta dentro de la funcion tenemos una variable llamada nombre_buscar donde ingresamos el nombre del producto que queremos buscar para despues hacer un for donde guardamos temporalmente en producto la informacion que estamos buscando en inventario el nombre que coincide
            
            if producto["cantidad"] >= cantidad_vender:
                producto["cantidad"] -= cantidad_vender  # Actualiza la cantidad
                total = cantidad_vender * producto["precio"]
                print(f"💰 Venta exitosa. Total a cobrar: ${total:.2f}")
                print(f"📉 Stock actualizado de {producto['nombre']}: {producto['cantidad']} unidades.")
                return  # Rompe la función ya que encontró el producto y procesó la venta
            else:
                print(f"❌ No hay suficiente stock. Solo quedan {producto['cantidad']} unidades.")
                return
                #despues veerifica la cantidad que hay en el inventario, cuando verifica que la cantidad pedida se pueden vender resta las unidades para mantener actualizado el inventario, multiplicando la cantidad con el precio monetario para mostrar el dinero a cobrar para finalizar con un return para evitar que sia buscando en el inventario
    print("❌ El producto no existe en el inventario.")


def mostrar_inventario(): #Creamos la funcion 
    if not inventario: #Comprueba que no tiene ningun elemento adentro
        print("📭 El inventario está vacío.")
        return #Si esta vacia avisa en la consola y detiene la ejecucion para evitar que imprima cosas innecesarias
    
    print("\n📦 --- INVENTARIO DE LA TIENDA ---")
    for producto in inventario:
        print(f"• Producto: {producto['nombre'].capitalize()[:15]:15}  | Precio: ${producto['precio']:10.2f} | Stock: {producto['cantidad']}")
    print("-----------------------------------")
    # El .capitalize toma el nombre y se asegura que la primera letra sea en mayuscula y las demas en minuscula 
    #El "[:15]" evita que objetos con caracteres muy largos mas de 15 caracteres corta el texto para que no dañe la tabla y el :15 rellena con espacios vaios a la derecha
    # El ":10" reserva un espacio de 10 caracteres para el precio y fuerza que se muestre siempre en decimales 


def menu(): # Creamos una funcion llamada menu
    while True: # Creamos un bucle while que no tenga fin para que cada vez que termine de agregar un producto vuelva a ejecutarse
        print("\n🏪 SYSTEMA DE GESTIÓN DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar inventario")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ").strip() # Compara el texto guardado en opcion para decidir que escoger
        #El .strip hace que borre los esspacios vaios que puede presionar el usuario 
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            realizar_venta()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Buen día!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
    # Aca le decimos que dependiendo lo que escoja le va a imprimir una opcion diferente si escribe una opcion que no existe le va a mostrar opcion no valida
if __name__ == "__main__":
    menu() #Es para reutilizar el codigo en otros archivos



    