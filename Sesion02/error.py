cadena = "Hola"

try:
    x = int(cadena)
except Exception as err:
    print(f"Error: {err}")