"""
ESEMPIO PRATICO: Gestore Voti Studenti
Questo script combina i concetti appresi: creazione, append, loop, funzioni built-in.
"""

def main():
    # Lista vuota per i voti
    voti = []
    
    print("--- GESTORE VOTI ---")
    print("Inserisci i voti (scrivi -1 per terminare):")

    while True:
        try:
            input_utente = float(input("Inserisci voto (1-10): "))
            
            if input_utente == -1:
                break
                
            if 1 <= input_utente <= 10:
                voti.append(input_utente)
            else:
                print("Errore: Il voto deve essere tra 1 e 10.")
                
        except ValueError:
            print("Errore: Inserisci un numero valido.")

    # Se la lista non è vuota, procediamo con le statistiche
    if voti:
        print("\n--- RIEPILOGO STATISTICO ---")
        print(f"Tutti i voti: {voti}")
        
        # Funzioni built-in per le liste numeriche
        totale_voti = len(voti)
        voto_max = max(voti)
        voto_min = min(voti)
        media = sum(voti) / totale_voti
        
        # List comprehension per filtrare i voti sufficienti
        sufficienti = [v for v in voti if v >= 6]

        print(f"Numero di prove: {totale_voti}")
        print(f"Voto più alto: {voto_max}")
        print(f"Voto più basso: {voto_min}")
        print(f"Media della classe: {media:.2f}")
        print(f"Voti sufficienti: {sufficienti} ({len(sufficienti)} studenti)")
        
    else:
        print("Nessun voto inserito.")

if __name__ == "__main__":
    main()
