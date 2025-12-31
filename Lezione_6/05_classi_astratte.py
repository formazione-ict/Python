"""
LEZIONE 5: Classi Astratte
Definire un'interfaccia che le sottoclassi DEVONO implementare.
"""
from abc import ABC, abstractmethod

# Classe Astratta: non può essere istanziata
class FormaGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Rettangolo(FormaGeometrica):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    # Se non implementassi area() e perimetro(), Python darebbe errore!
    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)

def main():
    # f = FormaGeometrica() # ERRORE: Non si può istanziare una classe astratta
    
    r = Rettangolo(10, 5)
    print(f"Area rettangolo: {r.area()}")

if __name__ == "__main__":
    main()
