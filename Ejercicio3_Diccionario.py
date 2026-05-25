# 1. Crear el diccionario vacío
agenda = {}

# --- FUNCIÓN 1: Añadir contacto ---
def añadir_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"✅ Guardado: {nombre} -> {telefono}")

# --- FUNCIÓN 2: Buscar contacto ---
def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"🔍 Teléfono de {nombre}: {agenda[nombre]}")
    else:
        print(f"❌ '{nombre}' no está en la agenda.")

# --- FUNCIÓN 3: Mostrar todos ---
def mostrar_contactos():
    print("\n📖 Lista de contactos:")
    # Usamos el bucle for para recorrer el diccionario
    for nombre, telefono in agenda.items():
        print(f"- {nombre}: {telefono}")


# === PRUEBA DEL PROGRAMA ===

# Usamos input() para pedir datos (Requerimiento 1)
nom = input("Introduce un nombre: ")
tel = input("Introduce su teléfono: ")
añadir_contacto(nom, tel)

# Añadimos otro de forma directa para tener variedad
añadir_contacto("Carlos", "3112345678")

# Mostramos todo (Requerimiento 3)
mostrar_contactos()

# Buscamos uno (Requerimiento 2)
nombre_buscar = input("\n¿A quién quieres buscar?: ")
buscar_contacto(nombre_buscar)