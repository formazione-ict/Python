"""
LEZIONE 4: Polimorfismo e Metodi Magici (Dunder Methods)
Far comportare oggetti diversi in modo uniforme.
"""

class Libro:
    def __init__(self, titolo, pagine):
        self.titolo = titolo
        self.pagine = pagine

    # Rappresentazione stringa (per print())
    def __str__(self):
        return f"'{self.titolo}' ({self.pagine} pag.)"

    # Sovraccarico operatore + (addizione)
    def __add__(self, altro_libro):
        if isinstance(altro_libro, Libro):
            return self.pagine + altro_libro.pagine
        return NotImplemented

def main():
    libro1 = Libro("Python Crash Course", 400)
    libro2 = Libro("Clean Code", 350)

    # Grazie a __str__, print() funziona in modo leggibile
    print(libro1)  
    
    # Grazie a __add__, possiamo sommare due libri!
    totale_pagine = libro1 + libro2
    print(f"Totale pagine da leggere: {totale_pagine}")

if __name__ == "__main__":
    main()
