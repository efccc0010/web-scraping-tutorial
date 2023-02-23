import math
def potencia(x, y):
    resultado = math.pow(x, y)
    return resultado
 
x = 2
y = 5
# potencia()
# print (resultado)

try: 
    x = "Hola Mundo"
    print(x)
    # print(x, z)
except:
    print ("Ha ocurrido un error")
finally:
    print ("END")