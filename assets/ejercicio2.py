"""
Ejercicio 2: Contar líneas de un archivo con manejo de errores
"""

def contar_lineas_archivo():
    """
    Abre un archivo, cuenta sus líneas y maneja errores de apertura.
    Usa try-except-else-finally.
    """
    print("\n" + "=" * 50)
    print("EJERCICIO 2 - CONTAR LÍNEAS DE ARCHIVO")
    print("=" * 50)
    
    nombre_archivo = input("Ingrese el nombre del archivo (ej: datos.txt): ")
    
    archivo = None
    try:
        # Intentar abrir el archivo
        archivo = open(nombre_archivo, "r", encoding="utf-8")
        
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")
        return
        
    except PermissionError:
        print(f"❌ Error: No tiene permisos para leer el archivo '{nombre_archivo}'.")
        return
        
    except Exception as e:
        print(f"❌ Error inesperado al abrir el archivo: {e}")
        return
        
    else:
        # Solo se ejecuta si no hubo errores al abrir
        try:
            lineas = archivo.readlines()
            cantidad = len(lineas)
            print(f"✅ El archivo '{nombre_archivo}' tiene {cantidad} líneas.")
            
            # Mostrar primeras 5 líneas si el archivo no es muy grande
            if cantidad > 0:
                print("\n📄 Primeras líneas:")
                for i, linea in enumerate(lineas[:5]):
                    print(f"   {i+1}: {linea.rstrip()}")
                if cantidad > 5:
                    print(f"   ... y {cantidad - 5} líneas más")
                    
        except Exception as e:
            print(f"❌ Error al leer el contenido: {e}")
            
    finally:
        # Siempre se ejecuta, asegurando que el archivo se cierra
        if archivo:
            archivo.close()
            print("\n🔒 Archivo cerrado correctamente.")
    
    print("\n" + "=" * 50)
    print("🏁 Fin del procesamiento del archivo")
    print("=" * 50)


if __name__ == "__main__":
    contar_lineas_archivo()