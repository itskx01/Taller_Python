# 1. Diccionario con los factores de conversión (la clave es el texto "origen_a_destino")
factores = {
    "metros_a_pies": 3.28084,
    "pies_a_metros": 0.3048,
    "kilometros_a_millas": 0.621371,
    "millas_a_kilometros": 1.60934
}

# 2. Función con múltiples parámetros y manejo de errores con 'if key in dict'
def convertir(cantidad, origen, destino):
    # Creamos el formato de la clave combinando el origen y el destino
    clave = f"{origen}_a_{destino}"
    
    # Manejo de errores básicos: Validamos si la combinación existe en el diccionario
    if clave in factores:
        factor = factores[clave]
        resultado = cantidad * factor
        return resultado
    else:
        # Si la unidad o la combinación no existe, retornamos None
        return None

# === PRUEBA DEL PROGRAMA ===

print("--- ⚖️ CONVERSOR DE UNIDADES ---")
# Captura de datos con input()
cant = float(input("Ingresa la cantidad a convertir: "))
origen_user = input("Unidad de origen (ej: metros, pies, kilometros): ").strip().lower()
destino_user = input("Unidad de destino (ej: metros, pies, millas): ").strip().lower()

# Llamada a la función pasándole los parámetros
resultado_conversion = convertir(cant, origen_user, destino_user)

# Verificación del retorno para manejar la respuesta al usuario
if resultado_conversion is not None:
    print(f"✅ {cant} {origen_user} equivalen a {resultado_conversion:.2f} {destino_user}.")
else:
    print("❌ Error: La conversión solicitada no está registrada en el sistema.")