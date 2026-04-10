"""
tests/test_validate.py – Pruebas para el módulo de validaciones.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from validate import es_email_valido, es_telefono_valido, id_unico


# ── Email ─────────────────────────────────────────────────────────────────────

class TestEsEmailValido:

    def test_email_valido(self):
        assert es_email_valido("juan@correo.com") is True

    def test_email_con_punto_en_usuario(self):
        assert es_email_valido("juan.perez@correo.com") is True

    def test_email_sin_arroba(self):
        assert es_email_valido("juancorreo.com") is False

    def test_email_sin_dominio(self):
        assert es_email_valido("juan@") is False

    def test_email_vacio(self):
        assert es_email_valido("") is False

    def test_email_con_espacios(self):
        assert es_email_valido("juan @correo.com") is False

    def test_email_dominio_corto(self):
        assert es_email_valido("juan@correo.c") is False


# ── Teléfono ──────────────────────────────────────────────────────────────────

class TestEsTelefonoValido:

    def test_telefono_valido_10_digitos(self):
        assert es_telefono_valido("3001234567") is True

    def test_telefono_valido_con_prefijo(self):
        assert es_telefono_valido("+573001234567") is True

    def test_telefono_valido_con_guiones(self):
        assert es_telefono_valido("300-123-4567") is True

    def test_telefono_muy_corto(self):
        assert es_telefono_valido("123") is False

    def test_telefono_con_letras(self):
        assert es_telefono_valido("300abc4567") is False

    def test_telefono_vacio(self):
        assert es_telefono_valido("") is False


# ── ID único ──────────────────────────────────────────────────────────────────

class TestIdUnico:

    def test_id_no_existe(self):
        assert id_unico(5, {1, 2, 3}) is True

    def test_id_ya_existe(self):
        assert id_unico(2, {1, 2, 3}) is False

    def test_set_vacio(self):
        assert id_unico(1, set()) is True