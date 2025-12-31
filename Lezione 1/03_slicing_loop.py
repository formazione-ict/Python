"""
ESEMPIO 3: Slicing e Iterazione
Come estrarre sotto-liste e ciclare attraverso i dati.
"""

def main():
    numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Lista completa: {numeri}")

    # --- SLICING ---
    # Sintassi: lista[inizio : fine(escluso) : passo]

    print(f"Primi 3 elementi [0:3]: {numeri[0:3]}")
    print(f"Dal quarto alla fine [3:]: {numeri[3:]}")
    print(f"Elementi pari (passo 2) [::2]: {numeri[::2]}")
    print(f"Lista invertita [::-1]: {numeri[::-1]}")

    # --- ITERAZIONE (LOOPS) ---
    
    studenti = ["Mario", "Luigi", "Peach", "Toad"]

    print("\n--- Ciclo For Semplice ---")
    for studente in studenti:
        print(f"Nome studente: {studente}")

    print("\n--- Ciclo con Indice (enumerate) ---")
    # enumerate restituisce sia l'indice che il valore
    # start=1 fa partire il conteggio da 1 per l'output visivo
    for i, studente in enumerate(studenti, start=1):
        print(f"{i}. {studente}")

if __name__ == "__main__":
    main()
