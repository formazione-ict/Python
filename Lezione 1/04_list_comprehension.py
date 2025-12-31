"""
ESEMPIO 4: List Comprehension (Opzionale/Avanzato)
Un modo conciso e potente per creare nuove liste basate su liste esistenti.
"""

def main():
    numeri = [1, 2, 3, 4, 5]
    
    # APPROCCIO CLASSICO (Ciclo For)
    quadrati_classico = []
    for n in numeri:
        quadrati_classico.append(n ** 2)
    print(f"Quadrati (loop): {quadrati_classico}")

    # APPROCCIO PYTHONIC (List Comprehension)
    # Sintassi: [espressione for elemento in lista]
    quadrati_comp = [n ** 2 for n in numeri]
    print(f"Quadrati (comprehension): {quadrati_comp}")

    # Comprehension con filtro (IF condition)
    # Solo numeri pari
    pari = [n for n in numeri if n % 2 == 0]
    print(f"Solo pari: {pari}")

if __name__ == "__main__":
    main()
