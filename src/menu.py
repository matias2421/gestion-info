"""
menu.py – Interfaz de consola (UI).
Presenta opciones al usuario y delega acciones al servicio.
Hito m4-menu: colores con colorama y manejo de errores en la selección.
"""

import service
from service import crear, listar, actualizar, eliminar
from integration import cargar_registros_falsos, exportar_csv, cargar_usuarios_api
from colorama import init, Fore, Style

init(autoreset=True)


def _encabezado():
    print(Fore.CYAN + "\n╔══════════════════════════════════╗")
    print(Fore.CYAN + "║     GESTIÓN DE CONTACTOS         ║")
    print(Fore.CYAN + "╚══════════════════════════════════╝")


def _mostrar_opciones():
    print(Fore.YELLOW + "\n  ── CRUD ──")
    print(Fore.WHITE + "  1. Crear registro")
    print(Fore.WHITE + "  2. Listar registros")
    print(Fore.WHITE + "  3. Actualizar registro")
    print(Fore.WHITE + "  4. Eliminar registro")
    print(Fore.YELLOW + "\n  ── Integraciones ──")
    print(Fore.WHITE + "  6. Generar contactos falsos (Faker)")
    print(Fore.WHITE + "  7. Exportar contactos a CSV (Pandas)")
    print(Fore.WHITE + "  8. Importar usuarios desde API (Requests)")
    print(Fore.RED + "\n  5. Salir")


def mostrar_menu():
    _encabezado()

    while True:
        _mostrar_opciones()

        try:
            seleccion = input(Fore.CYAN + "\nElige una opción: " + Style.RESET_ALL).strip()

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
                print(Fore.GREEN + "\n¡Hasta luego! 👋")
                break
            else:
                print(Fore.RED + "  ⚠ Opción no válida. Ingresa un número del menú.")

        except KeyboardInterrupt:
            print(Fore.GREEN + "\n\n¡Hasta luego! 👋")
            break
        except Exception as e:
            print(Fore.RED + f"  ⚠ Error inesperado: {e}")