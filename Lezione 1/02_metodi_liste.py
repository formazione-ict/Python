"""
LEZIONE 2: Metodi delle Liste
Panoramica delle operazioni principali per manipolare le liste.
"""

def main():
    frutta = ["mela", "banana", "ciliegia"]
    print(f"Lista iniziale: {frutta}")

    # --- AGGIUNGERE ELEMENTI ---
    
    # 1. append(): Aggiunge alla fine
    frutta.append("dattero")
    print(f"Dopo append('dattero'): {frutta}")

    # 2. insert(): Aggiunge in una posizione specifica
    frutta.insert(1, "arancia") # Inserisce all'indice 1
    print(f"Dopo insert(1, 'arancia'): {frutta}")

    # 3. extend(): Unisce un'altra lista
    frutta_esotica = ["mango", "papaya"]
    frutta.extend(frutta_esotica)
    print(f"Dopo extend: {frutta}")

    # --- RIMUOVERE ELEMENTI ---

    # 4. remove(): Rimuove la PRIMA occorrenza di un valore
    frutta.remove("banana")
    print(f"Dopo remove('banana'): {frutta}")

    # 5. pop(): Rimuove e RESTITUISCE l'elemento a un indice (default: ultimo)
    rimosso = frutta.pop() # Rimuove l'ultimo
    print(f"Elemento rimosso con pop(): {rimosso}")
    print(f"Lista attuale: {frutta}")

    # --- ORDINAMENTO ---
    
    numeri = [45, 10, 88, 2]
    
    # sort() ordina la lista "in-place" (modifica l'originale)
    numeri.sort()
    print(f"\nNumeri ordinati (sort): {numeri}")
    
    # reverse() inverte l'ordine attuale
    numeri.reverse()
    print(f"Numeri invertiti (reverse): {numeri}")

if __name__ == "__main__":
    main()
