from datetime import date
# Conjuntos
lista = [1,5,9]

conjunto = set(lista)
print(conjunto)

conjunto.add(10)
print(conjunto)

conjunto.remove(9)
print(conjunto)

# busqueda en Conjuntos o Set -> O(1)
# busqueda en Lista o List -> O(n)

# Diccionarios

d = {
    "edad": 19,
    "nombre": "Marco",
    "apellido": "Lopez",
    "promedio": 17.44,
}

print(d)

d["fecha_nacimiento"] = date(2000,10,10)
print(d)

for k,v in list(d.items()):
    print(f"{k} -> {v}")

d["padres"] = {
    "madre": "Maria",
    "padre": "Juan",
}
print(d)
print(d["padres"]["madre"])