"""
integration.py – Integraciones externas: faker, pandas, requests.
Contiene utilidades opcionales para generar datos de prueba,
exportar a CSV y consumir APIs externas.
"""

import os

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ── Faker: datos de prueba ────────────────────────────────────────────────────

def generar_registros_falsos(cantidad: int = 5) -> list[dict]:
    """Genera una lista de registros ficticios usando Faker."""
    from faker import Faker

    fake = Faker("es_CO")
    registros = []
    emails_usados = set()

    for i in range(cantidad):
        email = fake.email()
        while email in emails_usados:
            email = fake.email()
        emails_usados.add(email)

        registros.append(
            {
                "id": i + 1,
                "nombre": fake.name(),
                "email": email,
                "telefono": fake.numerify("3#########"),
                "descripcion": fake.job(),
            }
        )
    return registros


def cargar_registros_falsos(service) -> None:
    """Genera contactos falsos y los agrega al sistema."""
    try:
        cantidad = int(input("  ¿Cuántos contactos falsos deseas generar? [5]: ").strip() or "5")
        if cantidad <= 0:
            print("  ⚠ Ingresa un número mayor a 0.")
            return
    except ValueError:
        print("  ⚠ Valor inválido.")
        return

    registros = generar_registros_falsos(cantidad)
    agregados = 0

    for r in registros:
        if r["email"] in service.emails_registrados:
            continue  # saltar duplicados
        nuevo_id = max(service.ids_registrados, default=0) + 1
        r["id"] = nuevo_id
        service.contactos.append(r)
        service.ids_registrados.add(nuevo_id)
        service.emails_registrados.add(r["email"])
        agregados += 1

    from file import save_data
    save_data(service.contactos)
    print(f"  ✔ {agregados} contacto(s) falso(s) agregado(s) y guardado(s).")


# ── Pandas: exportar a CSV ────────────────────────────────────────────────────

def exportar_csv(registros: list[dict], ruta: str | None = None) -> None:
    """Exporta la lista de registros a un archivo CSV usando pandas."""
    import pandas as pd

    if ruta is None:
        ruta = os.path.join(_BASE_DIR, "data", "registros.csv")

    if not registros:
        print("  ⚠ No hay contactos para exportar.")
        return

    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    df = pd.DataFrame(registros)
    df.to_csv(ruta, index=False, encoding="utf-8")
    print(f"  ✔ {len(registros)} contacto(s) exportado(s) a {ruta}")


# ── Requests: consumir una API pública de ejemplo ────────────────────────────

def obtener_usuarios_api(limite: int = 3) -> list[dict]:
    """
    Descarga usuarios de ejemplo desde JSONPlaceholder.
    Retorna una lista de dicts con 'id', 'nombre', 'email', 'telefono', 'descripcion'.
    """
    import requests

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    usuarios = response.json()[:limite]
    return [
        {
            "id": u["id"],
            "nombre": u["name"],
            "email": u.get("email", "").lower(),
            "telefono": u.get("phone", "000-000-0000")[:15],
            "descripcion": u.get("company", {}).get("name", ""),
        }
        for u in usuarios
    ]


def cargar_usuarios_api(service) -> None:
    """Descarga usuarios de la API y los agrega al sistema."""
    try:
        limite = int(input("  ¿Cuántos usuarios deseas importar desde la API? [3]: ").strip() or "3")
        if limite <= 0:
            print("  ⚠ Ingresa un número mayor a 0.")
            return
    except ValueError:
        print("  ⚠ Valor inválido.")
        return

    print("  ⏳ Conectando con la API...")
    try:
        usuarios = obtener_usuarios_api(limite)
    except Exception as e:
        print(f"  ⚠ Error al conectar con la API: {e}")
        return

    agregados = 0
    for u in usuarios:
        if u["email"] in service.emails_registrados:
            print(f"  ↷ Email duplicado omitido: {u['email']}")
            continue
        nuevo_id = max(service.ids_registrados, default=0) + 1
        u["id"] = nuevo_id
        service.contactos.append(u)
        service.ids_registrados.add(nuevo_id)
        service.emails_registrados.add(u["email"])
        agregados += 1

    from file import save_data
    save_data(service.contactos)
    print(f"  ✔ {agregados} usuario(s) importado(s) y guardado(s).")
