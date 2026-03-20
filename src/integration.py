"""
integration.py – Integraciones externas: faker, pandas, requests.
Contiene utilidades opcionales para generar datos de prueba,
exportar a CSV y consumir APIs externas.
"""

# ── Faker: datos de prueba ────────────────────────────────────────────────────

def generar_registros_falsos(cantidad: int = 5) -> list[dict]:
    """Genera una lista de registros ficticios usando Faker."""
    from faker import Faker

    fake = Faker("es_CO")
    return [
        {
            "id": i + 1,
            "nombre": fake.name(),
            "descripcion": fake.job(),
        }
        for i in range(cantidad)
    ]


# ── Pandas: exportar a CSV ────────────────────────────────────────────────────

def exportar_csv(registros: list[dict], ruta: str = "data/registros.csv") -> None:
    """Exporta la lista de registros a un archivo CSV usando pandas."""
    import pandas as pd

    df = pd.DataFrame(registros)
    df.to_csv(ruta, index=False, encoding="utf-8")
    print(f"Registros exportados a {ruta}")


# ── Requests: consumir una API pública de ejemplo ────────────────────────────

def obtener_usuarios_api(limite: int = 3) -> list[dict]:
    """
    Descarga usuarios de ejemplo desde JSONPlaceholder.
    Retorna una lista de dicts con 'id', 'nombre' y 'descripcion'.
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
            "descripcion": u.get("email", ""),
        }
        for u in usuarios
    ]
