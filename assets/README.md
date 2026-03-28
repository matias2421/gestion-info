# Ejercicios Prácticos de Python

Seis ejercicios interactivos para practicar manejo de errores, archivos, refactorización y validaciones en Python.

---

## 🚀 Cómo ejecutar

```bash
# Ir a la carpeta del proyecto
cd gestion-info

# Ejecutar el menú principal
python assets/menu.py
📋 Lista de ejercicios
Ejercicio 1: Promedio de números
Calcula el promedio de números ingresados separados por comas.

Reglas:

Ingresar números separados por comas (ej: 10,20,30,40)

Maneja errores de conversión (si se ingresa texto)

Calcula promedio solo con números válidos

Ejemplo:


Ingrese números: 10,20,30,40
Promedio: 25.00
Ejercicio 2: Contar líneas de un archivo
Abre un archivo, cuenta sus líneas y muestra las primeras 5.

Reglas:

Solicita nombre del archivo

Maneja archivo no encontrado

Cierra el archivo correctamente con finally

Ejemplo:


Ingrese nombre del archivo: datos.txt
El archivo tiene 10 líneas

Primeras líneas:
1: Línea 1
2: Línea 2
3: Línea 3
Ejercicio 3: Menú con manejo de errores
Menú interactivo con opciones que capturan diferentes excepciones.

Opciones:

Dividir números - Captura ValueError y ZeroDivisionError

Mostrar primera línea de archivo - Captura FileNotFoundError

Salir

Reglas:

Cada opción maneja su propio tipo de error

Captura genérica Exception para errores no previstos

Ejercicio 4: Calculadora refactorizada
Calculadora con operaciones básicas usando diccionario y lambdas.

Operaciones:

suma o s - Suma dos números

resta o r - Resta dos números

multi o m - Multiplica dos números

divi o d - Divide dos números (maneja división por cero)

Características:

Usa diccionario para mapear operaciones

Retorna mensaje claro en lugar de mezclar tipos

Maneja operaciones inválidas

Ejemplo:


Operación: suma
Primer número: 10
Segundo número: 5
✅ Resultado: 15
Ejercicio 5: Validador de contraseñas
Valida contraseñas según reglas de seguridad.

Reglas:

✅ Mínimo 8 caracteres

✅ Sin espacios

✅ Al menos 1 número

✅ Al menos 1 mayúscula

Ejemplo:


Contraseña: Abcdefg1
✅ VÁLIDA

Contraseña: abcdefg1
❌ INVÁLIDA (falta mayúscula)
Ejercicio 6: Procesamiento de ventas
Sistema que calcula total de ventas con descuentos.

Reglas de descuento:

10% de descuento si cantidad ≥ 10 unidades

5% adicional si el cliente es VIP

Flujo:

Ingresar cantidad de ventas

Por cada venta: precio, cantidad, tipo cliente, estado

Calcula total con descuentos aplicados

Ignora ventas con estado diferente a "ok"

Ejemplo:


Venta 1: precio=100, cantidad=5, cliente=normal → $500
Venta 2: precio=50, cantidad=10, cliente=normal → $450 (10% desc)
Venta 3: precio=200, cantidad=2, cliente=vip → $380 (5% desc)
Total: $1330
🧪 Pruebas rápidas
Ejercicio	Prueba	Resultado esperado
1	10,20,30	Promedio: 20.00
2	Archivo inexistente	Error: archivo no existe
3	Dividir 10 / 0	Error: división por cero
4	divi 10 / 0	Error: división por cero
5	Abcdefg1	Válida
5	abcdefg1	Inválida (sin mayúscula)
6	Cantidad=10, normal	10% descuento
📁 Estructura de archivos

gestion-info/
└── assets/
    ├── ejercicio1.py      # Promedio de números
    ├── ejercicio2.py      # Contar líneas de archivo
    ├── ejercicio3.py      # Menú con manejo de errores
    ├── ejercicio4.py      # Calculadora refactorizada
    ├── ejercicio5.py      # Validador de contraseñas
    ├── ejercicio6.py      # Procesamiento de ventas
    └── menu.py            # Menú principal
⚙️ Requisitos
Python 3.8 o superior

No requiere librerías externas (solo librerías estándar)

❓ Solución de problemas
Problema	Solución
python no reconocido	Usar py en lugar de python
Archivo no encontrado	Verificar que el archivo existe en la carpeta actual
Error en ejercicio 2	Crear un archivo de prueba con echo "texto" > prueba.txt
👋 Salir del menú
Seleccione la opción 0 desde el menú principal.

📝 Notas
Cada ejercicio es independiente

Todos incluyen manejo de errores con try-except

El menú permite ejecutar cualquier ejercicio sin modificar código

