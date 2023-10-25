# Definicja trzech różnych bohaterów
bohaterowie = {
    1: {"nazwa": "Bohater 1", "zdrowie": 100, "pancerz": 30},
    2: {"nazwa": "Bohater 2", "zdrowie": 80, "pancerz": 20},
    3: {"nazwa": "Bohater 3", "zdrowie": 120, "pancerz": 40}
}

# Wybór bohatera przez użytkownika
print("Wybierz bohatera:")
for numer, bohater in bohaterowie.items():
    print(f"{numer}: {bohater['nazwa']}")
wybor = int(input("Wprowadź numer bohatera (1, 2 lub 3): "))

if wybor in bohaterowie:
    wybrany_bohater = bohaterowie[wybor]
    zdrowie_bohatera = wybrany_bohater["zdrowie"]
    pancerz_bohatera = wybrany_bohater["pancerz"]
    
    # Zapytaj użytkownika o ilość obrażeń
    obrazenia = int(input("Ile obrażeń otrzymać ma bohater? "))
    
    # Przelicz obrażenia z uwzględnieniem pancerza
    obrazenia_po_pancerzu = obrazenia * (1 - pancerz_bohatera / 100)
    
    # Sprawdź, czy bohater przeżył
    if zdrowie_bohatera > obrazenia_po_pancerzu:
        zdrowie_po_obrazeniach = zdrowie_bohatera - obrazenia_po_pancerzu
        print(f"Gratulacje, bohater przeżył! Pozostałe zdrowie: {zdrowie_po_obrazeniach}")
    else:
        print("Bohater umarł.")
else:
    print("Nieprawidłowy numer bohatera. Proszę wybrać 1, 2 lub 3.")
