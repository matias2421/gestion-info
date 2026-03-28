"""
Ejercicio 5: Validador de contraseñas
"""

def is_valid_password(password: str) -> bool:
    """Valida que la contraseña cumpla con las reglas."""
    # Regla 1: longitud mínima 8
    if len(password) < 8:
        return False
    
    # Regla 2: sin espacios
    if " " in password:
        return False
    
    # Regla 3: al menos un dígito
    if not any(c.isdigit() for c in password):
        return False
    
    # Regla 4: al menos una mayúscula
    if not any(c.isupper() for c in password):
        return False
    
    return True


# Programa principal con entrada de datos
if __name__ == "__main__":
    print("=" * 50)
    print("VALIDADOR DE CONTRASEÑAS")
    print("=" * 50)
    print("Reglas:")
    print("  - Mínimo 8 caracteres")
    print("  - Sin espacios")
    print("  - Al menos 1 número")
    print("  - Al menos 1 mayúscula")
    print("=" * 50)
    
    while True:
        password = input("\nIngrese una contraseña (o 'salir' para terminar): ")
        
        if password.lower() == "salir":
            print("👋 ¡Hasta luego!")
            break
        
        if is_valid_password(password):
            print("✅ CONTRASEÑA VÁLIDA")
        else:
            print("❌ CONTRASEÑA INVÁLIDA")
            print("   Debe cumplir con todas las reglas:")
            if len(password) < 8:
                print("   - Mínimo 8 caracteres")
            if " " in password:
                print("   - No puede contener espacios")
            if not any(c.isdigit() for c in password):
                print("   - Debe tener al menos un número")
            if not any(c.isupper() for c in password):
                print("   - Debe tener al menos una mayúscula")