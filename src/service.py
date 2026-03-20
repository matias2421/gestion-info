"""
service.py – Lógica de negocio (CRUD).
Coordina validaciones, persistencia y respuestas al menú.
"""

from file import cargar_registros, guardar_registros
from validate import campo_requerido, id_unico


# ── Crear ────────────────────────────────────────────────────────────────────

def crear():
    registros = cargar_registros()

    nombre = campo_requerido("Nombre: ")
    descripcion = input("Descripción: ").strip()

    nuevo_id = (max((r["id"] for r in registros), default=0)) + 1
    if not id_unico(nuevo_id, registros):
        print("Error: ID duplicado.")
        return

    registro = {"id": nuevo_id, "nombre": nombre, "descripcion": descripcion}
    registros.append(registro)
    guardar_registros(registros)
    print(f"Registro #{nuevo_id} creado correctamente.")


# ── Listar ───────────────────────────────────────────────────────────────────

def listar():
    registros = cargar_registros()
    if not registros:
        print("No hay registros todavía.")
        return
    print(f"\n{'ID':<6} {'Nombre':<25} {'Descripción'}")
    print("-" * 60)
    for r in registros:
        print(f"{r['id']:<6} {r['nombre']:<25} {r.get('descripcion', '')}")


# ── Actualizar ───────────────────────────────────────────────────────────────

def actualizar():
    registros = cargar_registros()
    try:
        registro_id = int(input("ID del registro a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    for r in registros:
        if r["id"] == registro_id:
            nuevo_nombre = campo_requerido(f"Nuevo nombre [{r['nombre']}]: ") or r["nombre"]
            nueva_desc = input(f"Nueva descripción [{r.get('descripcion', '')}]: ").strip()
            r["nombre"] = nuevo_nombre
            r["descripcion"] = nueva_desc or r.get("descripcion", "")
            guardar_registros(registros)
            print("Registro actualizado.")
            return

    print(f"No se encontró ningún registro con ID {registro_id}.")


# ── Eliminar ─────────────────────────────────────────────────────────────────

def eliminar():
    registros = cargar_registros()
    try:
        registro_id = int(input("ID del registro a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return

    nuevos = [r for r in registros if r["id"] != registro_id]
    if len(nuevos) == len(registros):
        print(f"No se encontró ningún registro con ID {registro_id}.")
        return

    guardar_registros(nuevos)
    print(f"Registro #{registro_id} eliminado.")
