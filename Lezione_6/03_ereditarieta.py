"""
LEZIONE 3: Ereditarietà
Creare nuove classi basate su classi esistenti per riutilizzare il codice.
"""

# Classe Padre (Base Class)
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def info(self):
        return f"Veicolo: {self.marca} {self.modello}"

# Classe Figlia (Derived Class)
class Auto(Veicolo):
    def __init__(self, marca, modello, cavalli):
        # Chiamata al costruttore del padre con super()
        super().__init__(marca, modello)
        self.cavalli = cavalli

    # Override: sovrascriviamo il metodo del padre
    def info(self):
        base_info = super().info()
        return f"{base_info}, {self.cavalli} CV (Automobile)"

class Moto(Veicolo):
    def impenna(self):
        return f"La {self.marca} sta impennando!"

def main():
    auto = Auto("Fiat", "Panda", 69)
    moto = Moto("Ducati", "Monster")

    print(auto.info())    # Usa il metodo sovrascritto di Auto
    print(moto.info())    # Usa il metodo originale di Veicolo
    print(moto.impenna()) # Metodo specifico di Moto

if __name__ == "__main__":
    main()
