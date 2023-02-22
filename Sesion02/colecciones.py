
# listas
numeros = [0,1,2,3,4,5,6,7,8,9]

print(numeros[0])
print(numeros[-1])

numeros.append(10)
print(numeros[0])
print(numeros[-1])

numeros[0] = 11
print(numeros[0])
print(numeros[-1])


numeros.sort(reverse=True)
print(numeros[0])
print(numeros[-1])

for elem in numeros:
    print(f"Es el elemento {elem}")

# cadenas
cadena = "Hola mundo"
print(f"Capitalize: {cadena.capitalize()}")    
print(f"Casefold: {cadena.casefold()}")    
print(f"Center: {cadena.center(100)}")    
print(f"Count: {cadena.count('o')}")    
print(f"Encode: {cadena.encode()}")    
print(f"Endswith: {cadena.endswith('a')}")    
print(f"Expandtabs: {cadena.expandtabs(4)}")    
print(f"Find: {cadena.find('a')}")    
print(f"Format: {cadena.format()}")    
print(f"Isalnum: {cadena.isalnum()}")    

cadena2 = "Primero, Segundo, Tercero, Cuarto, Quinto"
lista2 = cadena2.split(", ")
print(cadena2)
print(lista2)
cadena3 = "-".join(lista2)
print(cadena3)

# tuplas
variable = (1,2,3,4,5)
print(variable[0])


# cuestionario 2 pregunta 4 
var1 = 20
var2 = 30
var3 = 40
 
res1 = (not (var1 > 30))
res2 = not var2 > -30
res3 = ((var3 == 50 or var2 > 10) and var1 < 90)
 
resultado = ( (res1 != res2) and ( var1 > res2 + res1) )
print(resultado)


# cuestionario 2 pregunta 6
l = [10, 30, 50, 70]
l += l[-1:-3]
print(l[-1:-3])
print (l)