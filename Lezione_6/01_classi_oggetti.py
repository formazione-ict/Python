"""
LEZIONE 1: Classi e Oggetti
Una classe è un "progetto" (blueprint), un oggetto è la realizzazione concreta.
"""

class Cane:
    # Attributo di CLASSE (condiviso da tutti i cani)
    specie = "Canis Lupus Familiaris"

    def __init__(self, nome, eta):
        # Attributi di ISTANZA (specifici per ogni cane)
        self.nome = nome
        self.eta = eta

    def abbaia(self):
        # Metodo di istanza
        return f"{self.nome} dice: Woof!"

    def descrivi(self):
        return f"{self.nome} ha {self.eta} anni."

def main():
    # Creazione oggetti (Istanziazione)
    cane1 = Cane("Rex", 5)
    cane2 = Cane("Fido", 3)

    print(cane1.descrivi())  # Rex ha 5 anni.
    print(cane2.abbaia())    # Fido dice: Woof!
    
    # Accesso attributo di classe
    print(f"Specie: {cane1.specie}")

if __name__ == "__main__":
    main()
