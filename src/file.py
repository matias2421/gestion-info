"""
file.py – Persistencia: leer y guardar registros en data/records.json.
"""

import json
import os

# Ruta al archivo de datos relativa a este módulo
_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(_BASE_DIR, "data", "records.json")


def cargar_registros() -> list[dict]:
    """Lee y devuelve la lista de registros desde el archivo JSON."""
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def guardar_registros(registros: list[dict]) -> None:
    """Escribe la lista de registros en el archivo JSON."""
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)
