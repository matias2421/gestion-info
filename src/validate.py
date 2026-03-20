"""
validate.py – Validaciones y helpers reutilizables.
"""


def campo_requerido(mensaje: str) -> str:
    """Solicita un campo de texto no vacío al usuario."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo es obligatorio. Por favor, ingresa un valor.")


def id_unico(nuevo_id: int, registros: list[dict]) -> bool:
    """Verifica que el ID no exista ya en la lista de registros."""
    return all(r["id"] != nuevo_id for r in registros)


def es_entero_positivo(valor: str) -> bool:
    """Retorna True si la cadena representa un entero positivo."""
    try:
        return int(valor) > 0
    except ValueError:
        return False
