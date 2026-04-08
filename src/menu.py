"""
menu.py – Interfaz de consola (UI).
Presenta opciones al usuario y delega acciones al servicio.
"""

import service
from service import crear, listar, actualizar, eliminar
from integration import cargar_registros_falsos, exportar_csv, cargar_usuarios_api


def mostrar_menu():
    while True:
        print("\n=== Menú principal ===")
        print("  1. Crear registro")
        print("  2. Listar registros")
        print("  3. Actualizar registro")
        print("  4. Eliminar registro")
        print("  ── Módulo 3: Integraciones ──")
        print("  6. Generar contactos falsos (Faker)")
        print("  7. Exportar contactos a CSV (Pandas)")
        print("  8. Importar usuarios desde API (Requests)")
        print("  5. Salir")

        seleccion = input("Elige una opción: ").strip()

        if seleccion == "1":
            crear()
        elif seleccion == "2":
            listar()
        elif seleccion == "3":
            actualizar()
        elif seleccion == "4":
            eliminar()
        elif seleccion == "6":
            cargar_registros_falsos(service)
        elif seleccion == "7":
            exportar_csv(service.contactos)
        elif seleccion == "8":
            cargar_usuarios_api(service)
        elif seleccion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
