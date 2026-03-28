"""
file.py – Persistencia: cargar y guardar contactos en data/records.json.
"""

import json
import os

# Ruta al archivo de datos
_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(_BASE_DIR, "data", "records.json")


def load_data() -> list[dict]:
    """
    Carga los contactos desde el archivo JSON.
    - Si el archivo no existe, retorna lista vacía.
    - Si el archivo está dañado, muestra mensaje y retorna lista vacía.
    """
    if not os.path.exists(DATA_PATH):
        return []

    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            datos = json.load(f)
            if isinstance(datos, list):
                return datos
            print("  ⚠ El archivo tiene un formato inesperado. Arrancando con lista vacía.")
            return []
    except json.JSONDecodeError:
        print("  ⚠ El archivo está dañado. Arrancando con lista vacía.")
        return []
    except OSError as e:
        print(f"  ⚠ Error al leer el archivo: {e}")
        return []


def save_data(data: list[dict]) -> None:
    """
    Guarda la lista de contactos en el archivo JSON.
    - Crea la carpeta data/ si no existe.
    - Muestra mensaje si no se puede escribir.
    """
    try:
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"  ⚠ Error al guardar el archivo: {e}")