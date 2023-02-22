f = open("archivo.txt","r")

for line in f:
    line = line.strip()
    line = line.split(',')
    print(line[2])

f = open("archivo.txt","a")
f.write("\nManzana,5,10")

f = open("archivo2.txt","w")
f.write("HOLA MUNDO")
