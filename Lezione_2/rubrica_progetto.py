"""
PROGETTO FINALE: Rubrica Digitale
Unisce: Funzioni, Dizionari, Stringhe, Gestione File (JSON) e Error Handling.
"""
import json
import os

FILE_RUBRICA = "rubrica.json"

def carica_dati():
    """Carica la rubrica da file JSON. Se non esiste, ritorna dizionario vuoto."""
    if not os.path.exists(FILE_RUBRICA):
        return {}
    
    try:
        with open(FILE_RUBRICA, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Errore nel file dati. Inizializzo rubrica vuota.")
        return {}

def salva_dati(rubrica):
    """Salva la rubrica su file JSON."""
    with open(FILE_RUBRICA, "w") as f:
        json.dump(rubrica, f, indent=4)
    print("💾 Dati salvati correttamente.")

def aggiungi_contatto(rubrica):
    nome = input("Nome contatto: ").strip().title()
    if nome in rubrica:
        print("❌ Contatto già esistente!")
        return

    telefono = input("Numero di telefono: ").strip()
    email = input("Email (opzionale): ").strip()

    # Dizionario annidato
    rubrica[nome] = {
        "telefono": telefono,
        "email": email
    }
    print(f"✅ {nome} aggiunto.")

def cerca_contatto(rubrica):
    ricerca = input("Inserisci nome da cercare: ").strip().title()
    # Uso .get() per evitare errori
    contatto = rubrica.get(ricerca)
    
    if contatto:
        print(f"\n--- {ricerca} ---")
        print(f"📞 Tel: {contatto['telefono']}")
        print(f"📧 Email: {contatto['email']}")
    else:
        print("❌ Contatto non trovato.")

def main():
    rubrica = carica_dati()
    
    while True:
        print("\n--- MENU RUBRICA 2.0 ---")
        print("1. Aggiungi Contatto")
        print("2. Cerca Contatto")
        print("3. Visualizza Tutti")
        print("4. Esci (Salva)")
        
        scelta = input("Scegli (1-4): ")

        if scelta == "1":
            aggiungi_contatto(rubrica)
        elif scelta == "2":
            cerca_contatto(rubrica)
        elif scelta == "3":
            print(f"\nHai {len(rubrica)} contatti:")
            for nome in rubrica:
                print(f"- {nome}")
        elif scelta == "4":
            salva_dati(rubrica)
            print("Arrivederci! 👋")
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
