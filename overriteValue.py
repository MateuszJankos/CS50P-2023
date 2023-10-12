#pobieramy wartość Zwierze + strip Usuwa zbędne spacje z str + title Zamienia wszystkie pierwsze litery słów w Duże litery, naprawiąjąc tym rozmwiary liter
Zwierze = input("Podaj zwierzątko.   ").strip().title()

#Nadpisujemy Print aby nie przeskakiwało Entera, end równa się 1, sep równa się ??? jest to zamiast spacji
print("Zwierzątko to: " + Zwierze, end="1")
print("Zwierzątko to: " + Zwierze, sep="???")

#f oznacza specjalny string, gdzie {} oznaczają wartość 
print(f"Zwierzątko to: {Zwierze}")