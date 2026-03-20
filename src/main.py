"""
main.py – Punto de entrada del sistema de gestión de información.
"""

import sys
import os

# Permite importar módulos hermanos desde src/
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from menu import mostrar_menu


def main():
    print("Sistema listo")
    mostrar_menu()


if __name__ == "__main__":
    main()
