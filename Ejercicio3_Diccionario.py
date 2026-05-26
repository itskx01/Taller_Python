# Creamos un diccionario vacio
agenda = {}

# --- FUNCIÓN 1: Añadir contacto ---
def añadir_contacto(nombre, telefono): 
    agenda[nombre] = telefono
    print(f"✅ Guardado: {nombre} -> {telefono}")
"""
Creamos una funcion llamada "añadir_contacto" que tiene 2 variables (nombre,telefono), despues hacemos que agenda asocie el telefono con el nombre registrado
"""

# --- FUNCIÓN 2: Buscar contacto ---
def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"🔍 Teléfono de {nombre}: {agenda[nombre]}")
    else:
        print(f"❌ '{nombre}' no está en la agenda.")
"""
Creamos una funcion llamada "buscar_contacto" que tiene 1 variable (nombre), si el nombre se encuentra en la agenda va a devolver un tru si no esta va a ser false 
"""

# --- FUNCIÓN 3: Mostrar todos ---
def mostrar_contactos():
    print("\n📖 Lista de contactos:")
    # Usamos el bucle for para recorrer el diccionario
    for nombre, telefono in agenda.items():
        print(f"- {nombre}: {telefono}")
"""
Creamos una funcion llamada "mostrar_contacto" se imprime para despues hacer un bucle for para buscar en el diccionario, el agenda.item hace que entregue en parejas los datos y el for cada que se repite guarda la informacion de las variables 
"""

nom = input("Introduce un nombre: ")
tel = input("Introduce su teléfono: ")
# Aca estamos llamando las funciones ya creadas
añadir_contacto(nom, tel)
añadir_contacto("Carlos", "3112345678")
mostrar_contactos()

# Y aca estamos pidiendo que escriba el nombre para encontrarlo en el diccionario
nombre_buscar = input("\n¿A quién quieres buscar?: ")
buscar_contacto(nombre_buscar)

