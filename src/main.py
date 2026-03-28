"""
main.py – Punto de entrada del sistema de gestión de contactos.
Hito m2-files: los datos se guardan y cargan desde data/records.json.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import service
from menu import mostrar_menu


def main():
    print("Sistema listo")
    service.inicializar()
    total = len(service.contactos)
    print(f"  ({total} contacto(s) cargado(s) desde records.json)\n")
    service.listar()
    mostrar_menu()


if __name__ == "__main__":
    main()