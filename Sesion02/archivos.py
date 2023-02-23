f = open("archivo.txt","r")

for line in f:
    line = line.strip()
    line = line.split(',')
    print(line[2])

f = open("archivo.txt","a")
f.write("\nManzana,5,10")

f = open("archivo2.txt","w")
f.write("HOLA MUNDO")


# cuestionario 3 pregunta 2
def mostrarPixeles():
    file = open("pixeles.txt")
    pixeles = []
    for line in file:
        line = line.strip()
        line = line.split(",")
        pixeles.append(line[0])
    print(pixeles)
 
def procesarPixeles():
    file = open("pixeles.txt")
    pixeles = []
    for line in file:
        line = line.strip()
        line = line.split(",")
        pixeles.append(line[0])
    total = sum(pixeles)/len(pixeles)
    return total
 
def comprimirPixeles():
    file = open("pixeles.txt")
    pixeles = []
    for line in file:
        line = line.strip()
        line = line.split(",")
        pixeles.append(line[0])
    comprimido = rle(pixeles)
    return comprimido
 
def rle(pixeles):
    comprimido = []
    # ... procesamiento ...
    return comprimido