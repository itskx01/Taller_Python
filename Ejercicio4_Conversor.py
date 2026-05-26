
conversiones = {
    "metros_pies": 3.28,
    "pies_metros": 0.30,            # creamos un diccionario con las conversiones 
    "kilometros_millas": 0.62,
    "millas_kilometros": 1.60
}

# Función para convertir
def convertir(cantidad, origen, destino):
    
    # Crear la clave
    clave = origen + "_" + destino # esto solo es para unir los textos

    # Verificar si existe
    if clave in conversiones:
                                        # si existe la conversion en el diccioanrio se hace se hace la conversion
        # Hacer la conversión
        resultado = cantidad * conversiones[clave]
        
        return resultado    # retornar el resultado
    
    else:
        return "❌Conversión no disponible❌"       # si escribe una que no esxista en el diccionario envia este mensaje 



print("=== CONVERSOR DE UNIDADES ===")

cantidad = float(input("Ingresa una cantidad: "))

origen = input("Unidad de origen: ")            # aca le pedimos los datos al usuario para poder hacer la conversion
destino = input("Unidad de destino: ")

# Llamar la función
resultado = convertir(cantidad, origen, destino)        # aca en esta variable llamammos la funcion que cremos(convertir)

# Mostrar resultado
print(f"{resultado}✅")        # imprimimos el resultado de la conversion 



