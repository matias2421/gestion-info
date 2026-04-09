"""
main.py – Punto de entrada del sistema de gestión de contactos.
Hito m4-menu: colores con colorama en el arranque.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import service
from menu import mostrar_menu
from colorama import init, Fore, Style

init(autoreset=True)


def main():
    print(Fore.GREEN + "✔ Sistema listo")
    service.inicializar()
    total = len(service.contactos)
    print(Fore.WHITE + f"  ({total} contacto(s) cargado(s) desde records.json)\n")
    service.listar()
    mostrar_menu()


if __name__ == "__main__":
    main()