"""
ESEMPIO 3: Funzioni
Blocchi di codice riutilizzabili per organizzare la logica del programma.
"""

# Funzione base con parametri e return
def calcola_area_rettangolo(base, altezza):
    area = base * altezza
    return area

# Funzione con parametri di default (opzionali)
def saluta(nome, messaggio="Benvenuto"):
    print(f"{messaggio}, {nome}!")

# Funzione con *args (numero variabile di argomenti)
def somma_tutto(*numeri):
    # 'numeri' diventa una tupla: (10, 20, 30...)
    totale = 0
    for n in numeri:
        totale += n
    return totale

def main():
    # Chiamata base
    risultato = calcola_area_rettangolo(5, 10)
    print(f"Area: {risultato}")

    # Uso dei default
    saluta("Marco")             # Usa "Benvenuto"
    saluta("Luca", "Ciao")      # Sovrascrive il default

    # Argomenti variabili
    s = somma_tutto(10, 20, 30, 5) 
    print(f"Somma totale: {s}")

if __name__ == "__main__":
    main()
