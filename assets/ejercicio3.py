"""
Ejercicio 3: Menú interactivo con manejo de diferentes excepciones
"""

import os

def dividir_numeros():
    """Divide dos números ingresados por el usuario."""
    print("\n--- DIVIDIR NÚMEROS ---")
    
    try:
        num1 = float(input("Ingrese el dividendo (numerador): "))
        num2 = float(input("Ingrese el divisor (denominador): "))
        
        resultado = num1 / num2
        print(f"✅ Resultado: {num1} ÷ {num2} = {resultado}")
        
    except ValueError:
        print("❌ Error: Debe ingresar números válidos.")
        
    except ZeroDivisionError:
        print("❌ Error: No se puede dividir por cero.")
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def mostrar_primera_linea():
    """Muestra la primera línea de un archivo."""
    print("\n--- MOSTRAR PRIMERA LÍNEA ---")
    
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            primera_linea = archivo.readline()
            
            if primera_linea:
                print(f"✅ Primera línea: {primera_linea.strip()}")
            else:
                print("⚠️ El archivo está vacío.")
                
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")
        
    except PermissionError:
        print(f"❌ Error: No tiene permisos para leer el archivo.")
        
    except UnicodeDecodeError:
        print(f"❌ Error: El archivo tiene una codificación no soportada.")
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_principal():
    """Menú principal del ejercicio."""
    
    while True:
        limpiar_pantalla()
        print("\n" + "=" * 50)
        print("EJERCICIO 3 - MENÚ CON MANEJO DE ERRORES")
        print("=" * 50)
        print("1. Dividir números")
        print("2. Mostrar primera línea de archivo")
        print("3. Salir")
        print("=" * 50)
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            dividir_numeros()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "2":
            mostrar_primera_linea()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "3":
            print("\n👋 ¡Hasta luego!")
            break
            
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    menu_principal()