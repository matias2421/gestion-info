"""
tests/test_service.py – Pruebas para la logica de negocio (service.py).
Usa monkeypatch para evitar leer/escribir archivos reales.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
import service


@pytest.fixture(autouse=True)
def reset_service(monkeypatch):
    """Resetea el estado en memoria antes de cada prueba."""
    monkeypatch.setattr(service, "contactos", [])
    monkeypatch.setattr(service, "ids_registrados", set())
    monkeypatch.setattr(service, "emails_registrados", set())


@pytest.fixture
def contacto_base():
    return {
        "id": 1,
        "nombre": "Ana Lopez",
        "email": "ana@correo.com",
        "telefono": "3001234567",
        "descripcion": "Desarrolladora",
    }


# ── _siguiente_id ─────────────────────────────────────────────────────────────

class TestSiguienteId:

    def test_primer_id_es_1(self):
        assert service._siguiente_id() == 1

    def test_siguiente_id_con_registros(self):
        service.ids_registrados.add(3)
        service.ids_registrados.add(1)
        assert service._siguiente_id() == 4


# ── listar ────────────────────────────────────────────────────────────────────

class TestListar:

    def test_listar_sin_contactos(self, capsys):
        service.listar()
        salida = capsys.readouterr().out
        assert "No hay contactos" in salida

    def test_listar_con_contactos(self, capsys, contacto_base):
        service.contactos.append(contacto_base)
        service.listar()
        salida = capsys.readouterr().out
        assert "Ana Lopez" in salida
        assert "ana@correo.com" in salida


# ── eliminar ──────────────────────────────────────────────────────────────────

class TestEliminar:

    def test_eliminar_contacto_existente(self, monkeypatch, contacto_base):
        service.contactos.append(contacto_base)
        service.ids_registrados.add(1)
        service.emails_registrados.add("ana@correo.com")

        monkeypatch.setattr("service.save_data", lambda x: None)
        monkeypatch.setattr("builtins.input", lambda _: "1")

        service.eliminar()
        assert len(service.contactos) == 0
        assert 1 not in service.ids_registrados

    def test_eliminar_id_inexistente(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "99")
        service.eliminar()
        salida = capsys.readouterr().out
        assert "No se encontró" in salida

    def test_eliminar_id_invalido(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "abc")
        service.eliminar()
        salida = capsys.readouterr().out
        assert "inválido" in salida


# ── integration: construir_contacto ──────────────────────────────────────────

class TestConstruirContacto:

    def test_args_posicionales(self):
        from integration import construir_contacto
        c = construir_contacto("Pedro", "pedro@mail.com", "3009876543")
        assert c["nombre"] == "Pedro"
        assert c["email"] == "pedro@mail.com"
        assert c["telefono"] == "3009876543"

    def test_kwargs_nombrados(self):
        from integration import construir_contacto
        c = construir_contacto(nombre="Luis", email="luis@mail.com")
        assert c["nombre"] == "Luis"
        assert c["descripcion"] == ""

    def test_defaults_vacios(self):
        from integration import construir_contacto
        c = construir_contacto()
        assert c["nombre"] == "Sin nombre"
        assert c["email"] == ""