"""
Menú interactivo para ejecutar los ejercicios del taller
"""

import os
import sys

# Agregar la ruta base para poder importar módulos si es necesario
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)


def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\nPresione Enter para continuar...")


def ejecutar_ejercicio(ruta: str):
    """Ejecuta un archivo Python."""
    try:
        # Ejecutar el archivo
        with open(ruta, "r", encoding="utf-8") as archivo:
            codigo = archivo.read()
            exec(codigo)
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {ruta}")
    except Exception as e:
        print(f"❌ Error al ejecutar: {e}")
    
    pausar()


def mostrar_menu():
    """Muestra el menú principal."""
    while True:
        limpiar_pantalla()
        
        print("=" * 60)
        print("   TALLER DE PYTHON - EJERCICIOS PRÁCTICOS")
        print("=" * 60)
        print()
        print("   EJERCICIOS DE MANEJO DE ERRORES Y ARCHIVOS:")
        print("   " + "-" * 50)
        print("   1. Promedio de números separados por comas")
        print("   2. Contar líneas de un archivo")
        print("   3. Menú interactivo con manejo de errores")
        print("   4. Calculadora refactorizada")
        print("   5. Validador de contraseñas")
        print("   6. Procesamiento de ventas")
        print()
        print("   " + "-" * 50)
        print("   0. Salir")
        print("=" * 60)
        
        opcion = input("\nSeleccione un ejercicio (0-6): ").strip()
        
        # Mapeo de opciones a archivos
        ejercicios = {
            "1": "ejercicio1.py",
            "2": "ejercicio2.py",
            "3": "ejercicio3.py",
            "4": "ejercicio4.py",
            "5": "ejercicio5.py",
            "6": "ejercicio6.py",
        }
        
        if opcion == "0":
            print("\n👋 ¡Hasta luego!")
            break
        
        elif opcion in ejercicios:
            ruta = os.path.join(BASE_DIR, "assets", ejercicios[opcion])
            ejecutar_ejercicio(ruta)
        
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")
            pausar()


if __name__ == "__main__":
    mostrar_menu()