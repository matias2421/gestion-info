# Gestión de Información

Sistema de gestión de registros por consola desarrollado en Python.

## Requisitos

- Python 3.8 o superior
- pip

## Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/<tu-usuario>/gestion-info.git
cd gestion-info

# 2. (Opcional) Crea un entorno virtual
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Instala las dependencias
pip install -r requirements.txt
```

## Cómo correr el programa

```bash
python src/main.py
```

Deberías ver en consola:

```
Sistema listo
```

## Estructura del proyecto

```
gestion-info/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ data/
│  └─ records.json        # almacenamiento de registros
└─ src/
   ├─ main.py             # punto de entrada
   ├─ menu.py             # interfaz de consola (UI)
   ├─ service.py          # lógica de negocio (CRUD)
   ├─ file.py             # persistencia (leer/guardar JSON)
   ├─ validate.py         # validaciones y helpers
   └─ integration.py      # integraciones: faker, pandas, requests
```

## Tag de versión

`m0-setup` — configuración inicial del proyecto.
