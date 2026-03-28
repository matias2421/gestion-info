"""
Ejercicio 1: Calcular promedio de números separados por comas
"""

def calcular_promedio():
    """
    Lee una línea de números separados por comas, calcula el promedio
    y maneja errores de conversión.
    """
    print("\n" + "=" * 50)
    print("EJERCICIO 1 - CALCULAR PROMEDIO")
    print("=" * 50)
    
    entrada = input("Ingrese números separados por comas (ej: 10,20,30): ")
    
    # Dividir por comas y limpiar espacios
    partes = [p.strip() for p in entrada.split(",")]
    
    numeros = []
    errores = []
    
    # Convertir cada parte a número, capturando errores
    for i, parte in enumerate(partes):
        try:
            numero = float(parte)
            numeros.append(numero)
        except ValueError:
            errores.append(f"Posición {i+1}: '{parte}' no es un número válido")
    
    # Mostrar errores de conversión
    if errores:
        print("\n⚠️ Errores de conversión encontrados:")
        for error in errores:
            print(f"   • {error}")
    
    # Calcular promedio solo con números válidos
    if numeros:
        # Cálculo correcto del promedio: suma / cantidad
        promedio = sum(numeros) / len(numeros)
        print(f"\n✅ Números válidos: {numeros}")
        print(f"✅ Cantidad de números: {len(numeros)}")
        print(f"✅ Suma total: {sum(numeros)}")
        print(f"✅ Promedio: {promedio:.2f}")
    else:
        print("\n❌ No se ingresaron números válidos para calcular el promedio.")
    
    print("\n" + "-" * 50)


if __name__ == "__main__":
    calcular_promedio()