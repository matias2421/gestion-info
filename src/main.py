"""
main.py – Punto de entrada del sistema de gestión de contactos.
Hito m1-data: crea contactos en memoria y los lista.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import service
from menu import mostrar_menu


def _cargar_datos_demo():
    """Inserta dos contactos de ejemplo directamente en memoria."""
    service.contactos.extend([
        {"id": 1, "nombre": "Ana García",   "email": "ana@example.com",
         "telefono": "3001234567", "descripcion": "Cliente VIP"},
        {"id": 2, "nombre": "Luis Pérez",   "email": "luis@example.com",
         "telefono": "3119876543", "descripcion": "Proveedor"},
    ])
    service.ids_registrados.update({1, 2})
    service.emails_registrados.update({"ana@example.com", "luis@example.com"})


def main():
    print("Sistema listo")
    _cargar_datos_demo()
    print("  (2 contactos de demo cargados en memoria)\n")
    service.listar()
    mostrar_menu()


if __name__ == "__main__":
    main()