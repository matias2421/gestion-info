"""
menu.py – Interfaz de consola (UI).
Presenta opciones al usuario y delega acciones al servicio.
"""

from service import crear, listar, actualizar, eliminar


def mostrar_menu():
    opciones = {
        "1": ("Crear registro",    crear),
        "2": ("Listar registros",  listar),
        "3": ("Actualizar registro", actualizar),
        "4": ("Eliminar registro", eliminar),
        "5": ("Salir",             None),
    }

    while True:
        print("\n=== Menú principal ===")
        for clave, (descripcion, _) in opciones.items():
            print(f"  {clave}. {descripcion}")

        seleccion = input("Elige una opción: ").strip()

        if seleccion == "5":
            print("¡Hasta luego!")
            break
        elif seleccion in opciones:
            _, accion = opciones[seleccion]
            accion()
        else:
            print("Opción no válida. Intenta de nuevo.")
