"""
LEZIONE 1: Basi delle Liste
Questo script illustra come creare liste e accedere ai loro elementi.
"""

def main():
    # 1. Creazione di liste
    # Le liste sono ordinate e mutabili. Possono contenere tipi misti.
    lista_vuota = []
    numeri = [1, 2, 3, 4, 5]
    mista = [1, "Python", 3.14, True]
    
    print(f"Lista numeri: {numeri}")
    print(f"Lista mista: {mista}")

    # 2. Accedere agli elementi (Indicizzazione)
    # Gli indici partono da 0
    linguaggi = ["Python", "Java", "C++", "JavaScript"]
    
    print(f"\nPrimo elemento (indice 0): {linguaggi[0]}")
    print(f"Terzo elemento (indice 2): {linguaggi[2]}")

    # 3. Indicizzazione Negativa
    # Python permette di contare dalla fine: -1 è l'ultimo elemento
    print(f"Ultimo elemento (indice -1): {linguaggi[-1]}")
    print(f"Penultimo elemento (indice -2): {linguaggi[-2]}")

    # 4. Modifica di un elemento (Mutabilità)
    print(f"\nLista originale: {linguaggi}")
    linguaggi[1] = "C#"  # Sostituisce 'Java' con 'C#'
    print(f"Lista modificata: {linguaggi}")

if __name__ == "__main__":
    main()
