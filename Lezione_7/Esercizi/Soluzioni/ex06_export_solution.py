"""
TEMPLATE AVANZATO – Matplotlib (OO API)
---------------------------------------

Contenuti didattici:
- Uso della Object-Oriented API (fig, ax)
- Subplot multipli con fig.add_subplot() e plt.subplots()
- Gestione avanzata di stili e temi (plt.style.use)
- Figure complesse con layout ottimizzato (tight_layout, constrained_layout)
- Annotazioni, limiti assi, ticks personalizzati
- Esportazione professionale
"""

import os
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1) Utility: crea la cartella outputs/ se non esiste
# ------------------------------------------------------------
def ensure_output_dir():
    os.makedirs("outputs", exist_ok=True)


# ------------------------------------------------------------
# 2) Funzione principale
# ------------------------------------------------------------
def main():

    # --------------------------------------------------------
    # A) Imposta uno stile globale (tema)
    #    Puoi provare: 'ggplot', 'seaborn-v0_8', 'bmh', 'dark_background'
    # --------------------------------------------------------
    plt.style.use('seaborn-v0_8')

    # --------------------------------------------------------
    # B) Generazione dati
    # --------------------------------------------------------
    x = np.linspace(0, 2*np.pi, 400)
    sinx = np.sin(x)
    cosx = np.cos(x)
    tanx = np.tan(x)

    # Rumore per grafici più realistici
    noise = 0.1 * np.random.randn(len(x))
    sin_noisy = sinx + noise

    # --------------------------------------------------------
    # C) Creazione figura complessa con più subplot
    #    figsize controlla dimensioni in pollici
    #    constrained_layout ottimizza automaticamente gli spazi
    # --------------------------------------------------------
    fig = plt.figure(figsize=(14, 8), constrained_layout=True)

    # Subplot 1: sin e cos
    ax1 = fig.add_subplot(2, 2, 1)  # 2 righe, 2 colonne, posizione 1

    # Subplot 2: sin rumoroso
    ax2 = fig.add_subplot(2, 2, 2)

    # Subplot 3: tan con limiti
    ax3 = fig.add_subplot(2, 1, 2)  # 2 righe, 1 colonna, posizione 2 (più largo)

    # --------------------------------------------------------
    # D) Subplot 1 – sin e cos
    # --------------------------------------------------------
    ax1.plot(x, sinx, label='sin(x)', color='blue', linewidth=2)
    ax1.plot(x, cosx, label='cos(x)', color='red', linestyle='--')

    ax1.set_title("Seno e Coseno")
    ax1.set_xlabel("x (rad)")
    ax1.set_ylabel("valore")
    ax1.grid(True)
    ax1.legend()

    # Annotazione didattica
    ax1.annotate(
        "Intersezione",
        xy=(np.pi/4, np.sin(np.pi/4)),
        xytext=(1, 1),
        arrowprops=dict(arrowstyle="->", color="black")
    )

    # --------------------------------------------------------
    # E) Subplot 2 – sin rumoroso (scatter + linea)
    # --------------------------------------------------------
    ax2.scatter(x, sin_noisy, s=10, alpha=0.5, label="sin(x) + noise")
    ax2.plot(x, sinx, color='black', linewidth=2, label="sin(x)")

    ax2.set_title("Seno con rumore")
    ax2.set_xlabel("x (rad)")
    ax2.set_ylabel("valore")
    ax2.grid(True)
    ax2.legend()

    # --------------------------------------------------------
    # F) Subplot 3 – tan(x) con limiti e ticks personalizzati
    # --------------------------------------------------------
    ax3.plot(x, tanx, color='purple', linewidth=1)

    ax3.set_title("Tangente (con limiti)")
    ax3.set_xlabel("x (rad)")
    ax3.set_ylabel("valore")

    # Limiti verticali per evitare esplosioni della tangente
    ax3.set_ylim(-5, 5)

    # Ticks personalizzati
    ax3.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax3.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])

    ax3.grid(True)

    # --------------------------------------------------------
    # G) Esportazione professionale
    # --------------------------------------------------------
    ensure_output_dir()
    fig.savefig("outputs/advanced_subplot_template.png", dpi=200, bbox_inches='tight')
    print("✔ Grafico complesso salvato in outputs/advanced_subplot_template.png")

    # --------------------------------------------------------
    # H) Visualizzazione
    # --------------------------------------------------------
    plt.show()


# ------------------------------------------------------------
# Avvio programma
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
