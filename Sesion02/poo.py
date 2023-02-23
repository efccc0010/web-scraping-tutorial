class Casa:
    color: str
    consumo_luz: int
    consumo_agua: int

    def __init__(self, color):
        self.color = color
        self.consumo_luz = 0
        self.consumo_agua = 0


    def pintar(self,color):
        self.color = color

    def prender_luz(self):
        self.consumo_luz += 10

    def abrir_ducha(self):
        self.consumo_agua += 10

    def tocar_timbre(self):
        print("RIIIIIIIIIIN")
        self.consumo_luz += 2

class Mansion(Casa):
    def prender_luz(self):
        self.consumo_luz += 50

    def abrir_ducha(self):
        self.consumo_agua += 50
    
    def tocar_timbre(self):
        print("DING DONG")
        self.consumo_luz += 3

mi_casa = Casa("rojo")
print(mi_casa.color)
print(mi_casa.consumo_agua)
print(mi_casa.consumo_luz)
mi_casa.abrir_ducha()
mi_casa.prender_luz()
mi_casa.tocar_timbre()
print(mi_casa.consumo_agua)
print(mi_casa.consumo_luz)


mi_mansion = Mansion("Azul")
print(mi_mansion.color)
print(mi_mansion.consumo_agua)
print(mi_mansion.consumo_luz)
mi_mansion.abrir_ducha()
mi_mansion.prender_luz()
mi_mansion.tocar_timbre()
print(mi_mansion.consumo_agua)
print(mi_mansion.consumo_luz)