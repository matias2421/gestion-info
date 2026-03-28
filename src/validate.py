"""
validate.py – Validaciones y helpers para el sistema de contactos.
"""

import re


# ── Campos requeridos ─────────────────────────────────────────────────────────

def campo_requerido(mensaje: str) -> str:
    """Solicita un campo de texto no vacío al usuario."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  ⚠ Este campo es obligatorio.")


# ── Email ─────────────────────────────────────────────────────────────────────

def es_email_valido(email: str) -> bool:
    """Retorna True si el email tiene formato válido."""
    patron = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(patron, email))


def pedir_email(emails_registrados: set) -> str:
    """Pide un email válido y único (no duplicado en el set)."""
    while True:
        email = input("Email: ").strip().lower()
        if not es_email_valido(email):
            print("  ⚠ Formato de email inválido. Ejemplo: nombre@correo.com")
        elif email in emails_registrados:
            print("  ⚠ Ese email ya está registrado.")
        else:
            return email


# ── Teléfono ──────────────────────────────────────────────────────────────────

def es_telefono_valido(telefono: str) -> bool:
    """Acepta números con 7 a 15 dígitos, opcionalmente con +, espacios o guiones."""
    patron = r"^\+?[\d\s\-]{7,15}$"
    return bool(re.match(patron, telefono))


def pedir_telefono() -> str:
    """Pide un teléfono con formato válido."""
    while True:
        telefono = input("Teléfono: ").strip()
        if es_telefono_valido(telefono):
            return telefono
        print("  ⚠ Teléfono inválido. Ingresa entre 7 y 15 dígitos.")


# ── ID único ──────────────────────────────────────────────────────────────────

def id_unico(nuevo_id: int, ids_registrados: set) -> bool:
    """Verifica que el ID no exista en el set de IDs."""
    return nuevo_id not in ids_registrados