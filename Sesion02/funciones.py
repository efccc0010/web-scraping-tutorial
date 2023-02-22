def suma(lista: list) -> float:
    x = 0
    for elem in lista:
        x += elem
    return x

lista = [1,2,3,4,5,6,7,8,9,10]

print(suma(lista=lista))
print(sum(lista))