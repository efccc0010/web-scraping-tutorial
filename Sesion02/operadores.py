import random

x = 4
y = 5
z = random.randint(1,10)

print (x != y)
print (x == y)
print (x > y)
print (x < y)
print (x <= y)
print (x >= y)

if z == 1:
    print(f"Numero {z}")
elif z == 2: 
    print(f"Numero {z}")
else:
    print(f"Numero {z}")

x = 0
for i in range(10):
     x += random.randint(1,100)
     print(f"{i} -> {x}")
