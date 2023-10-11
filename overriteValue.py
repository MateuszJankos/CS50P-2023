#pobieramy wartość Zwierze
Zwierze = input("Podaj zwierzątko.   ")

#Nadpisujemy Print aby nie przeskakiwało Entera, end równa się 1, sep równa się ??? jest to zamiast spacji
print("Zwierzątko to: " + Zwierze, end="1")
print("Zwierzątko to: " + Zwierze, sep="???")

#f oznacza specjalny string, gdzie {} oznaczają wartość 
print(f"Zwierzątko to: {Zwierze}")
