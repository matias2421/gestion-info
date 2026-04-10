"""
integration.py – Integraciones externas: faker, pandas, requests.
Contiene utilidades opcionales para generar datos de prueba,
exportar a CSV y consumir APIs externas.

Hito m5-integracion: uso de *args y **kwargs en funciones genéricas.
"""

import os
from faker import Faker
import pandas as pd
import requests

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ── Helper genérico con *args y **kwargs ─────────────────────────────────────

def construir_contacto(*args, **kwargs) -> dict:
    """
    Construye un dict de contacto de forma flexible.

    Uso con *args (posicional):
        construir_contacto("Ana López", "ana@mail.com", "3001234567")

    Uso con **kwargs (nombrado):
        construir_contacto(nombre="Ana", email="ana@mail.com", telefono="300...")

    Uso mixto:
        construir_contacto("Ana López", email="ana@mail.com", descripcion="Dev")
    """
    campos = ["nombre", "email", "telefono", "descripcion"]

    # Primero asignamos los posicionales en orden
    contacto = {campos[i]: v for i, v in enumerate(args) if i < len(campos)}

    # Luego los nombrados (sobrescriben si hay conflicto)
    for clave, valor in kwargs.items():
        if clave in campos:
            contacto[clave] = valor

    # Valores por defecto para campos faltantes
    contacto.setdefault("nombre", "Sin nombre")
    contacto.setdefault("email", "")
    contacto.setdefault("telefono", "")
    contacto.setdefault("descripcion", "")

    return contacto


def _agregar_al_sistema(service, registros: list[dict]) -> int:
    """Agrega una lista de registros al sistema evitando duplicados. Retorna cantidad agregada."""
    from file import save_data

    agregados = 0
    for r in registros:
        if r["email"] in service.emails_registrados:
            continue
        nuevo_id = max(service.ids_registrados, default=0) + 1
        r["id"] = nuevo_id
        service.contactos.append(r)
        service.ids_registrados.add(nuevo_id)
        service.emails_registrados.add(r["email"])
        agregados += 1

    if agregados:
        save_data(service.contactos)
    return agregados


# ── Faker: datos de prueba ────────────────────────────────────────────────────

def generar_registros_falsos(cantidad: int = 5, **kwargs) -> list[dict]:
    """
    Genera registros ficticios usando Faker.

    **kwargs opcionales:
        locale (str) – idioma/region de Faker. Default: "es_CO"
    """
    locale = kwargs.get("locale", "es_CO")
    fake = Faker(locale)
    registros = []
    emails_usados = set()

    for _ in range(cantidad):
        email = fake.email()
        while email in emails_usados:
            email = fake.email()
        emails_usados.add(email)

        registro = construir_contacto(
            nombre=fake.name(),
            email=email,
            telefono=fake.numerify("3#########"),
            descripcion=fake.job(),
        )
        registros.append(registro)

    return registros


def cargar_registros_falsos(service) -> None:
    """Genera contactos falsos y los agrega al sistema."""
    try:
        cantidad = int(input("  Cuantos contactos falsos deseas generar? [5]: ").strip() or "5")
        if cantidad <= 0:
            print("  Ingresa un numero mayor a 0.")
            return
    except ValueError:
        print("  Valor invalido.")
        return

    registros = generar_registros_falsos(cantidad)
    agregados = _agregar_al_sistema(service, registros)
    print(f"  {agregados} contacto(s) falso(s) agregado(s) y guardado(s).")


# ── Pandas: exportar a CSV ────────────────────────────────────────────────────

def exportar_csv(registros: list[dict], *args, **kwargs) -> None:
    """
    Exporta registros a CSV usando pandas.

    *args:
        ruta (str) – ruta del archivo de salida (opcional)

    **kwargs opcionales:
        encoding  (str)  – codificacion del archivo. Default: "utf-8"
        separador (str)  – separador de columnas. Default: ","
        columnas  (list) – columnas a exportar. Default: todas
    """
    ruta      = args[0] if args else os.path.join(_BASE_DIR, "data", "registros.csv")
    encoding  = kwargs.get("encoding", "utf-8")
    separador = kwargs.get("separador", ",")
    columnas  = kwargs.get("columnas", None)

    if not registros:
        print("  No hay contactos para exportar.")
        return

    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    df = pd.DataFrame(registros)

    if columnas:
        df = df[[c for c in columnas if c in df.columns]]

    df.to_csv(ruta, index=False, encoding=encoding, sep=separador)
    print(f"  {len(registros)} contacto(s) exportado(s) a {ruta}")


# ── Requests: consumir una API publica de ejemplo ────────────────────────────

def obtener_usuarios_api(*args, **kwargs) -> list[dict]:
    """
    Descarga usuarios desde JSONPlaceholder.

    *args:
        limite (int) – cantidad de usuarios a traer. Default: 3

    **kwargs opcionales:
        url     (str) – endpoint alternativo
        timeout (int) – segundos de espera. Default: 5
    """
    limite  = args[0] if args else kwargs.get("limite", 3)
    url     = kwargs.get("url", "https://jsonplaceholder.typicode.com/users")
    timeout = kwargs.get("timeout", 5)

    response = requests.get(url, timeout=timeout)
    response.raise_for_status()

    usuarios = response.json()[:limite]
    return [
        construir_contacto(
            nombre=u["name"],
            email=u.get("email", "").lower(),
            telefono=u.get("phone", "000-000-0000")[:15],
            descripcion=u.get("company", {}).get("name", ""),
        )
        for u in usuarios
    ]


def cargar_usuarios_api(service) -> None:
    """Descarga usuarios de la API y los agrega al sistema."""
    try:
        limite = int(input("  Cuantos usuarios deseas importar desde la API? [3]: ").strip() or "3")
        if limite <= 0:
            print("  Ingresa un numero mayor a 0.")
            return
    except ValueError:
        print("  Valor invalido.")
        return

    print("  Conectando con la API...")
    try:
        usuarios = obtener_usuarios_api(limite)
    except Exception as e:
        print(f"  Error al conectar con la API: {e}")
        return

    agregados = _agregar_al_sistema(service, usuarios)
    print(f"  {agregados} usuario(s) importado(s) y guardado(s).")