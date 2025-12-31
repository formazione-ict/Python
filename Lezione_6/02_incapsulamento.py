"""
LEZIONE 2: Incapsulamento
Proteggere i dati interni e controllarne l'accesso.
"""

class Persona:
    def __init__(self, nome, eta_iniziale):
        self.nome = nome
        # Attributo "privato" (convenzione Python: __var)
        self.__eta = eta_iniziale

    # Getter tramite decoratore @property
    @property
    def eta(self):
        return self.__eta

    # Setter per validare i dati in input
    @eta.setter
    def eta(self, nuova_eta):
        if nuova_eta > 0:
            self.__eta = nuova_eta
        else:
            print("Errore: L'età deve essere positiva!")

def main():
    p = Persona("Mario", 30)
    
    # Accesso in lettura (usa il getter)
    print(f"Età attuale: {p.eta}")

    # Accesso in scrittura (usa il setter)
    p.eta = 31
    print(f"Nuova età: {p.eta}")

    # Tentativo non valido
    p.eta = -5  # Stampa errore e non modifica

    # Nota: p.__eta genererebbe un errore AttributeError se chiamato direttamente
    # print(p.__eta) # ERRORE!

if __name__ == "__main__":
    main()
