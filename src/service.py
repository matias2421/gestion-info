"""
service.py – Lógica de negocio (CRUD) en memoria para contactos.

Estructuras de datos:
    contactos        : list[dict]  – lista principal de registros
    ids_registrados  : set         – IDs únicos (evita duplicados)
    emails_registrados: set        – emails únicos (evita duplicados)
"""

from validate import campo_requerido, pedir_email, pedir_telefono, id_unico

# ── Estado en memoria ─────────────────────────────────────────────────────────
contactos: list[dict] = []
ids_registrados: set = set()
emails_registrados: set = set()


def _siguiente_id() -> int:
    return max(ids_registrados, default=0) + 1


# ── Crear ─────────────────────────────────────────────────────────────────────

def crear():
    print("\n── Nuevo contacto ──")
    nuevo_id = _siguiente_id()

    if not id_unico(nuevo_id, ids_registrados):
        print("Error interno: ID duplicado.")
        return

    nombre      = campo_requerido("Nombre: ")
    email       = pedir_email(emails_registrados)
    telefono    = pedir_telefono()
    descripcion = input("Descripción (opcional): ").strip()

    contacto = {
        "id":          nuevo_id,
        "nombre":      nombre,
        "email":       email,
        "telefono":    telefono,
        "descripcion": descripcion,
    }

    contactos.append(contacto)
    ids_registrados.add(nuevo_id)
    emails_registrados.add(email)

    print(f"  ✔ Contacto #{nuevo_id} creado correctamente.")


# ── Listar ────────────────────────────────────────────────────────────────────

def listar():
    if not contactos:
        print("\n  (No hay contactos registrados)")
        return

    print(f"\n{'ID':<5} {'Nombre':<20} {'Email':<25} {'Teléfono':<15} {'Descripción'}")
    print("─" * 80)
    for c in contactos:
        print(f"{c['id']:<5} {c['nombre']:<20} {c['email']:<25} {c['telefono']:<15} {c.get('descripcion','')}")


# ── Actualizar ────────────────────────────────────────────────────────────────

def actualizar():
    listar()
    try:
        cid = int(input("\nID del contacto a actualizar: "))
    except ValueError:
        print("  ⚠ ID inválido.")
        return

    for c in contactos:
        if c["id"] == cid:
            print("  (Deja en blanco para conservar el valor actual)")
            nombre = input(f"Nombre [{c['nombre']}]: ").strip() or c["nombre"]

            # Email: solo cambia si ingresa uno distinto
            nuevo_email = input(f"Email [{c['email']}]: ").strip().lower()
            if nuevo_email and nuevo_email != c["email"]:
                from validate import es_email_valido
                if not es_email_valido(nuevo_email):
                    print("  ⚠ Email inválido, se conserva el anterior.")
                    nuevo_email = c["email"]
                elif nuevo_email in emails_registrados:
                    print("  ⚠ Email duplicado, se conserva el anterior.")
                    nuevo_email = c["email"]
                else:
                    emails_registrados.discard(c["email"])
                    emails_registrados.add(nuevo_email)
            else:
                nuevo_email = c["email"]

            telefono    = input(f"Teléfono [{c['telefono']}]: ").strip() or c["telefono"]
            descripcion = input(f"Descripción [{c.get('descripcion','')}]: ").strip() or c.get("descripcion","")

            c.update({"nombre": nombre, "email": nuevo_email,
                      "telefono": telefono, "descripcion": descripcion})
            print("  ✔ Contacto actualizado.")
            return

    print(f"  ⚠ No se encontró ningún contacto con ID {cid}.")


# ── Eliminar ──────────────────────────────────────────────────────────────────

def eliminar():
    listar()
    try:
        cid = int(input("\nID del contacto a eliminar: "))
    except ValueError:
        print("  ⚠ ID inválido.")
        return

    for c in contactos:
        if c["id"] == cid:
            contactos.remove(c)
            ids_registrados.discard(cid)
            emails_registrados.discard(c["email"])
            print(f"  ✔ Contacto #{cid} eliminado.")
            return

    print(f"  ⚠ No se encontró ningún contacto con ID {cid}.")