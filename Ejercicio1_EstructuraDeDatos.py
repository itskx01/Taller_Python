def analizar_calificaciones(calificaciones):
    if not calificaciones:
        return (0.0, 0.0, 0.0)
    
    # 1. Calcular el promedio usando sum() y len()
    promedio = sum(calificaciones) / len(calificaciones)
    
    # 2. Encontrar la calificación más alta y más baja usando max() y min()
    nota_maxima = max(calificaciones)
    nota_minima = min(calificaciones)
    
    # 3. Retornar los resultados en una tupla (promedio, max, min)
    return (promedio, nota_maxima, nota_minima)

# Lista de ejemplo con el bucle 'for' para mostrar los datos individualmente
mis_calificaciones = [4.5, 3.2, 5.0, 2.8, 4.0, 3.7]

print("Calificaciones registradas:")
for nota in mis_calificaciones:
    print(f"- {nota}")

print("-" * 30)

# Llamada a la función y desempaquetado de la tupla resultante
promedio, maxima, minima = analizar_calificaciones(mis_calificaciones)


# Mostrar resultados 
print(f"Resultados del análisis:")
print("Resultados del análisis:")
print(f"• Promedio: {promedio:.2f}")
print(f"• Calificación más alta: {maxima}")
print(f"• Calificación más baja: {minima}")

