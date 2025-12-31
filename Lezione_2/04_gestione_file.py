"""
LEZIONE 4: Gestione File e JSON
Come leggere e scrivere dati in modo persistente.
"""
import json  # Modulo standard per gestire file .json

def main():
    # --- SCRITTURA FILE TESTO ---
    testo = "Prima riga\nSeconda riga\nTerza riga"
    
    # 'w' = write (sovrascrive), 'with' chiude il file automaticamente
    with open("note.txt", "w", encoding="utf-8") as f:
        f.write(testo)
    print("File note.txt creato.")

    # --- LETTURA FILE TESTO ---
    with open("note.txt", "r", encoding="utf-8") as f:
        contenuto = f.read() # Legge tutto in una stringa
        print(f"\nContenuto letto:\n{contenuto}")

    # --- GESTIONE JSON (Fondamentale per i Dizionari) ---
    configurazione = {
        "tema": "dark",
        "volume": 80,
        "utenti_recenti": ["admin", "guest"]
    }

    # Salvare un dizionario su file (Dump)
    with open("config.json", "w") as f:
        json.dump(configurazione, f, indent=4) # indent=4 rende il file leggibile
    print("\nFile config.json salvato.")

    # Caricare un dizionario da file (Load)
    with open("config.json", "r") as f:
        dati_caricati = json.load(f)
        print(f"Tema caricato: {dati_caricati['tema']}")

if __name__ == "__main__":
    main()
