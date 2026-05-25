factores = {
    "metros_a_pies": 3.28084,
    "pies_a_metros": 0.3048,
    "kilometros_a_millas": 0.621371,
    "millas_a_kilometros": 1.60934
}

def convertir(cantidad, origen, destino):
    clave = f"{origen}_a_{destino}"
    
    if clave in factores:
        factor = factores[clave]
        resultado = cantidad * factor
        return resultado
    else:
        return None

print("--- ⚖️ CONVERSOR DE UNIDADES ---")
cant = float(input("Ingresa la cantidad a convertir: "))
origen_user = input("Unidad de origen (ej: metros, pies, kilometros): ").strip().lower()
destino_user = input("Unidad de destino (ej: metros, pies, millas): ").strip().lower()

resultado_conversion = convertir(cant, origen_user, destino_user)

if resultado_conversion is not None:
    print(f"✅ {cant} {origen_user} equivalen a {resultado_conversion:.2f} {destino_user}.")
else:
    print("❌ Error: La conversión solicitada no está registrada en el sistema.")