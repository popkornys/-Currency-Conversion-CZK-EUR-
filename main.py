from tkinter import *

# okno
window = Tk()
window.title("Převod měn")
window.minsize(width=200, height=200)
window.resizable(False, False)
window.config(bg="#061856")



# Akce vyvolaná zmáčknutím tlačítka
def calculate():
    try:
        float(user_input.get())
    except ValueError:
        warning_label = Label(text="Neplatný vstup", font=("Cambria", 10, "bold"), bg="#061856", foreground="red")
        warning_label.grid(row=3, column=0, padx=10, pady=1)
    else:
        result = float(user_input.get()) / 22.05
        calculated_value["text"] = round(result, 2)
        user_input.delete(0, END)
        # user_input.delete(0, END)  # Vymazání obsahu vstupu uživatele
        warning_label = Label(text="", font=("Cambria", 10, "bold"), bg="#061856", foreground="red")
        warning_label.grid(row=3, column=0, columnspan=3, padx=10, pady=1, sticky=W + E)


# Vstup uživatele
user_input = Entry(width=10, font=("Cambria", 10))
user_input.focus()  # Nastavení kurzoru na vstup uživatele
user_input.grid(row=0, column=0, padx=10, pady=1)

# Výpis výsledku
calculated_value = Label(text="0", font=("Cambria", 15), bg="#061856", foreground="white")
calculated_value.grid(row=1, column=0, padx=10, pady=10)

euro_label = Label(text="EUR", font=("Cambria", 10), bg="#061856", foreground="white")
euro_label.grid(row=1, column=1, padx=10, pady=10)

# label
currency = Label(text="CZK", font=("Cambria", 10), bg="#061856", foreground="white")
# currency.pack(pady=50)  # Přidání do okna, expand si zabaere veškeré moné místo
# currency.place(x=250, y=100)  # Velmi specifické přidní pomocí souřadnic
currency.grid(row=0, column=1, padx=10, pady=1)

# Tlačítko
Calculate_Btn = Button(text="Calculate", font=("Cambria", 10, "bold"), command=calculate)
# Calculate_Btn.pack()
Calculate_Btn.grid(row=0, column=3, padx=10, pady=10)

# hlavní cyklus
window.mainloop()
