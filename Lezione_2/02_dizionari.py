"""
ESEMPIO 2: Dizionari
Strutture dati che associano una chiave univoca a un valore.
Simili ai JSON o alle HashMap in altri linguaggi.
"""

def main():
    # 1. Creazione
    studente = {
        "nome": "Alice",
        "eta": 22,
        "corsi": ["Python", "Database"], # Il valore può essere una lista
        "media": 29.5
    }

    # 2. Accesso ai dati
    print(f"Nome: {studente['nome']}")
    
    # Metodo .get() è più sicuro: non crasha se la chiave non esiste
    indirizzo = studente.get("indirizzo", "Non specificato")
    print(f"Indirizzo: {indirizzo}")

    # 3. Modifica e Aggiunta
    studente["eta"] = 23           # Modifica
    studente["laureato"] = False   # Nuova chiave
    
    # 4. Iterazione (Chiavi e Valori)
    print("\n--- Dettagli Studente ---")
    for chiave, valore in studente.items():
        print(f"{chiave}: {valore}")

    # 5. Dizionari Annidati (Dizionario dentro Dizionario)
    database = {
        "id_01": {"nome": "Mario", "ruolo": "Admin"},
        "id_02": {"nome": "Luigi", "ruolo": "User"}
    }
    
    print(f"\nRuolo di Mario: {database['id_01']['ruolo']}")

if __name__ == "__main__":
    main()
