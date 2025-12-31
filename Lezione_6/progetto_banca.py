from abc import ABC, abstractmethod
from datetime import datetime

# --- CLASSE ASTRATTA (Base) ---
class ContoBancario(ABC):
    def __init__(self, titolare, saldo_iniziale=0):
        self.titolare = titolare
        self._saldo = saldo_iniziale  # _saldo è protetto
        self._movimenti = [] # Storico operazioni

    @property
    def saldo(self):
        return self._saldo

    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo
            self._registra_movimento(f"Deposito: +{importo}€")
            print(f"Depositati {importo}€. Nuovo saldo: {self._saldo}€")
        else:
            print("Importo non valido.")

    # Metodo astratto: ogni tipo di conto deve implementare le sue regole di prelievo
    @abstractmethod
    def preleva(self, importo):
        pass

    def _registra_movimento(self, descrizione):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._movimenti.append(f"[{data}] {descrizione}")

    def stampa_estratto_conto(self):
        print(f"\n--- Estratto Conto di {self.titolare} ---")
        for mov in self._movimenti:
            print(mov)
        print(f"Saldo Finale: {self.saldo}€\n")


# --- SOTTOCLASSE 1: Conto Corrente (con fido) ---
class ContoCorrente(ContoBancario):
    def __init__(self, titolare, saldo_iniziale=0, fido=1000):
        super().__init__(titolare, saldo_iniziale)
        self.fido = fido

    def preleva(self, importo):
        # Può andare in rosso fino al limite del fido
        if self.saldo + self.fido >= importo:
            self._saldo -= importo
            self._registra_movimento(f"Prelievo: -{importo}€")
            print(f"Prelevati {importo}€. Nuovo saldo: {self.saldo}€")
        else:
            print("Fondi insufficienti (superato limite fido).")


# --- SOTTOCLASSE 2: Conto Risparmio (con interessi e vincoli) ---
class ContoRisparmio(ContoBancario):
    def __init__(self, titolare, saldo_iniziale=0, tasso_interesse=0.02):
        super().__init__(titolare, saldo_iniziale)
        self.tasso = tasso_interesse
        self.prelievi_rimanenti = 3  # Max 3 prelievi gratuiti

    def preleva(self, importo):
        if self.saldo >= importo:
            if self.prelievi_rimanenti > 0:
                self._saldo -= importo
                self.prelievi_rimanenti -= 1
                self._registra_movimento(f"Prelievo: -{importo}€ (Gratis)")
            else:
                penale = 2.0
                self._saldo -= (importo + penale)
                self._registra_movimento(f"Prelievo: -{importo}€ (Penale -{penale}€)")
            print(f"Prelevati {importo}€. Nuovo saldo: {self.saldo}€")
        else:
            print("Fondi insufficienti.")

    def applica_interessi(self):
        interessi = self.saldo * self.tasso
        self.deposita(interessi)
        self._registra_movimento(f"Interessi maturati: +{interessi}€")


# --- ESECUZIONE ---
if __name__ == "__main__":
    # Polimorfismo: Trattiamo oggetti diversi allo stesso modo
    cc = ContoCorrente("Mario Rossi", 500)
    cr = ContoRisparmio("Luigi Verdi", 2000)

    # Operazioni
    cc.deposita(200)
    cc.preleva(1000) # Va in rosso (ok per fido)
    
    cr.preleva(500)
    cr.applica_interessi()

    # Stampa report
    for conto in [cc, cr]:
        conto.stampa_estratto_conto()
