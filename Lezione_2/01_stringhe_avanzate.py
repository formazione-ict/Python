"""
ESEMPIO 1: Manipolazione Stringhe
Le stringhe in Python sono immutabili ma offrono metodi potenti per l'elaborazione del testo.
"""

def main():
    # 1. F-Strings (Formattazione moderna)
    nome = "Mario"
    voto = 28.5
    # Inseriamo variabili direttamente nella stringa
    print(f"Studente: {nome}, Voto: {voto}") 

    # 2. Metodi di pulizia e ricerca
    testo_sporco = "   Python è Fantastico   "
    pulito = testo_sporco.strip().lower() # Rimuove spazi e converte in minuscolo
    print(f"Testo pulito: '{pulito}'")
    
    # 3. Split e Join (Fondamentali per parsare dati)
    csv_data = "mario,luigi,peach,toad"
    lista_nomi = csv_data.split(",")  # Da Stringa a Lista
    print(f"Lista: {lista_nomi}")
    
    nuova_stringa = " - ".join(lista_nomi) # Da Lista a Stringa
    print(f"Join: {nuova_stringa}")

    # 4. Slicing sulle stringhe
    codice = "PROD-12345-IT"
    categoria = codice[:4]    # Primi 4 caratteri
    id_num = codice[5:10]     # Caratteri centrali
    nazione = codice[-2:]     # Ultimi 2
    
    print(f"Cat: {categoria}, ID: {id_num}, Naz: {nazione}")

if __name__ == "__main__":
    main()
