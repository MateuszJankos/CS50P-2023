import tkinter as tk
from tkinter import messagebox

# Funkcja do obsługi przycisku "Zapisz profil"
def zapisz_profil():
    imie = entry_imie.get()
    wiek = entry_wiek.get()
    zainteresowania = entry_zainteresowania.get("1.0", "end-1c")

    if imie and wiek and zainteresowania:
        messagebox.showinfo("Sukces", "Profil został zapisany!")
    else:
        messagebox.showerror("Błąd", "Wszystkie pola są wymagane!")

# Tworzenie okna głównego
root = tk.Tk()
root.title("Profil Randkowy")

# Tworzenie etykiet i pól do wprowadzania danych
label_imie = tk.Label(root, text="Imię:")
label_wiek = tk.Label(root, text="Wiek:")
label_zainteresowania = tk.Label(root, text="Zainteresowania:")

entry_imie = tk.Entry(root)
entry_wiek = tk.Entry(root)
entry_zainteresowania = tk.Text(root, height=5, width=30)

# Tworzenie przycisku do zapisywania profilu
button_zapisz = tk.Button(root, text="Zapisz profil", command=zapisz_profil)

# Rozmieszczenie elementów w oknie
label_imie.grid(row=0, column=0)
label_wiek.grid(row=1, column=0)
label_zainteresowania.grid(row=2, column=0)

entry_imie.grid(row=0, column=1)
entry_wiek.grid(row=1, column=1)
entry_zainteresowania.grid(row=2, column=1)

button_zapisz.grid(row=3, columnspan=2)

# Uruchomienie głównej pętli programu
root.mainloop()