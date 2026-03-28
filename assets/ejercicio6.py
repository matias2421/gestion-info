"""
Ejercicio 6: Procesamiento de ventas refactorizado
"""

def calcular_descuento(cantidad: int, es_vip: bool) -> float:
    """Calcula descuento según cantidad y tipo de cliente."""
    descuento = 0.0
    if cantidad >= 10:
        descuento += 0.10
    if es_vip:
        descuento += 0.05
    return descuento


def calcular_total_venta(venta: dict) -> float:
    """Calcula total de una venta individual."""
    if venta.get("status") != "ok":
        return 0
    
    precio = venta["price"]
    cantidad = venta["qty"]
    es_vip = venta.get("customer") == "vip"
    
    descuento = calcular_descuento(cantidad, es_vip)
    subtotal = precio * cantidad
    
    return subtotal - (subtotal * descuento)


def calcular_total_general(ventas: list[dict]) -> float:
    """Calcula total sumando todas las ventas válidas."""
    total = 0
    for venta in ventas:
        total += calcular_total_venta(venta)
    return total


# Programa principal
if __name__ == "__main__":
    ventas = []
    
    print("=" * 50)
    print("PROCESAMIENTO DE VENTAS")
    print("=" * 50)
    
    n = int(input("¿Cuántas ventas desea registrar? "))
    
    for i in range(n):
        print(f"\n--- Venta {i+1} ---")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        cliente = input("Cliente (normal/vip): ").strip().lower()
        estado = input("Estado (ok/cancelado): ").strip().lower()
        
        venta = {
            "price": precio,
            "qty": cantidad,
            "customer": cliente,
            "status": estado
        }
        ventas.append(venta)
    
    total = calcular_total_general(ventas)
    
    print("\n" + "=" * 50)
    print(f"💰 TOTAL GENERAL: ${total:.2f}")
    print("=" * 50)