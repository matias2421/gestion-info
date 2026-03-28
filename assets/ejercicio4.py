"""
Ejercicio 4: Calculadora refactorizada (versión compacta)
"""

def calc(a, b, op):
    """Calculadora con diccionario de operaciones."""
    ops = {
        "suma": lambda x, y: x + y,
        "resta": lambda x, y: x - y,
        "multi": lambda x, y: x * y,
        "divi": lambda x, y: "Error: división por cero" if y == 0 else x / y
    }
    
    func = ops.get(op)
    return func(a, b) if func else None


def main():
    print("\nOperaciones: suma, resta, multi, divi")
    
    try:
        op = input("Operación: ").strip().lower()
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        
        result = calc(a, b, op)
        
        if result is None:
            print(f"❌ Operación '{op}' no válida")
        elif isinstance(result, str):
            print(f"❌ {result}")
        else:
            # Mostrar sin decimales si es entero
            if result == int(result):
                result = int(result)
            print(f"✅ Resultado: {result}")
    
    except ValueError:
        print("❌ Error: Ingrese números válidos")


if __name__ == "__main__":
    main()