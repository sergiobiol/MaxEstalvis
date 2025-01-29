import tkinter as tk
from tkinter import ttk, font, messagebox

def mostrar_error():
    messagebox.showerror("Error", "Si us plau, introdueix un número vàlid per Diners totals i Salari.")

def ajustar_percentatges(combobox_actualitzat):
    total_seleccionat = sum(int(combo.get().strip('%')) for combo in totes_les_combobox)
    restant = 100 - total_seleccionat

    for combo in totes_les_combobox:
        if combo != combobox_actualitzat:
            valor_actual = int(combo.get().strip('%'))
            nou_valor = max(0, min(valor_actual, restant))
            combo.set(f"{nou_valor}%")

def calcular():
    try:
        total = float(entry_diners_totals.get())
        salari = float(entry_salari.get())

        percentatges = {}
        for categoria, combo in comboboxes.items():
            percentatges[categoria] = int(combo.get().strip('%')) / 100

        for categoria, percentatge in percentatges.items():
            resultats_total[categoria].config(text=f"{total * percentatge:.2f} €")
            resultats_salari[categoria].config(text=f"{salari * percentatge:.2f} €")

    except ValueError:
        mostrar_error()

finestra = tk.Tk()
finestra.title("MaxEstalvis")
finestra.geometry("950x450")
finestra.configure(bg="#BFD7ED")

style = ttk.Style()
style.configure("TLabel", background="#BFD7ED", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10, "bold"), padding=5)
style.configure("TCombobox", padding=5)

font_titol = font.Font(size=16, weight="bold")
ttk.Label(finestra, text="Max Estalvis", font=font_titol, background="#BFD7ED").grid(row=0, column=0, columnspan=6, pady=10)

ttk.Label(finestra, text="Diners totals:").grid(row=1, column=0, sticky="e")
entry_diners_totals = ttk.Entry(finestra)
entry_diners_totals.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(finestra, text="Salari:").grid(row=2, column=0, sticky="e")
entry_salari = ttk.Entry(finestra)
entry_salari.grid(row=2, column=1, padx=10, pady=5)

ttk.Separator(finestra, orient="horizontal").grid(row=3, column=0, columnspan=6, sticky="ew", pady=10)

opcions_percentatges = ["0%", "5%", "10%", "15%", "20%", "25%", "30%", "35%", "40%", "50%", "100%"]

categories = ["Casa", "Ahorrar", "Cotxe", "Capritxos", "Ús diari"]
comboboxes = {}

for i, categoria in enumerate(categories):
    fila = i + 5
    ttk.Label(finestra, text=categoria).grid(row=fila, column=0, sticky="e", padx=10)
    combobox = ttk.Combobox(finestra, values=opcions_percentatges, state="readonly", width=5)
    combobox.grid(row=fila, column=1, padx=10, pady=3)
    combobox.set("10%" if categoria != "Casa" else "40%")
    combobox.bind("<<ComboboxSelected>>", lambda e, c=combobox: ajustar_percentatges(c))
    comboboxes[categoria] = combobox

totes_les_combobox = list(comboboxes.values())

ttk.Button(finestra, text="Calcular", command=calcular).grid(row=10, column=0, columnspan=2, pady=10)

ttk.Separator(finestra, orient="horizontal").grid(row=11, column=0, columnspan=6, sticky="ew", pady=10)
ttk.Label(finestra, text="Diners Totals", font=("Arial", 10, "bold")).grid(row=4, column=3, padx=40)
ttk.Label(finestra, text="Salari", font=("Arial", 10, "bold")).grid(row=4, column=5, padx=40)


resultats_total = {}
resultats_salari = {}

for i, categoria in enumerate(categories):
    fila = i + 5

    ttk.Label(finestra, text=categoria).grid(row=fila, column=2, sticky="e", padx=20)
    resultat_total = ttk.Label(finestra, text="0.00 €", anchor="center", width=10)
    resultat_total.grid(row=fila, column=3, padx=40)
    resultats_total[categoria] = resultat_total

    ttk.Label(finestra, text=categoria).grid(row=fila, column=4, sticky="e", padx=20)
    resultat_salari = ttk.Label(finestra, text="0.00 €", anchor="center", width=10)
    resultat_salari.grid(row=fila, column=5, padx=40)
    resultats_salari[categoria] = resultat_salari

finestra.mainloop()
