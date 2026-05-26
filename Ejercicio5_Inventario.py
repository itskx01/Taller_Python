inventario = []
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


def realizar_venta():
    nombre_buscar = input("¿Qué producto deseas vender?: ").strip().lower()
    
    for producto in inventario:
        if producto["nombre"] == nombre_buscar:
            cantidad_vender = int(input(f"¿Cuántas unidades de '{nombre_buscar}' vas a vender?: "))
            
            if producto["cantidad"] >= cantidad_vender:
                producto["cantidad"] -= cantidad_vender  # Actualiza la cantidad
                total = cantidad_vender * producto["precio"]
                print(f"💰 Venta exitosa. Total a cobrar: ${total:.2f}")
                print(f"📉 Stock actualizado de {producto['nombre']}: {producto['cantidad']} unidades.")
                return  # Rompe la función ya que encontró el producto y procesó la venta
            else:
                print(f"❌ No hay suficiente stock. Solo quedan {producto['cantidad']} unidades.")
                return
                
    print("❌ El producto no existe en el inventario.")


def mostrar_inventario():
    if not inventario:
        print("📭 El inventario está vacío.")
        return
    
    print("\n📦 --- INVENTARIO DE LA TIENDA ---")
    for producto in inventario:
        print(f"• Producto: {producto['nombre'].capitalize()[:15]:15} | Precio: ${producto['precio']:10.2f} | Stock: {producto['cantidad']}")
    print("-----------------------------------")


def menu():
    while True:
        print("\n🏪 SYSTEMA DE GESTIÓN DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar inventario")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ").strip()
        
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

if __name__ == "__main__":
    menu()


    