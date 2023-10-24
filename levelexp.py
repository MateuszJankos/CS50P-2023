lvl = 1
xp = 0
Gold = 500

print("lvl = ", lvl)
print("xp =  ", xp)
print("Gold = ", Gold)


print("Wybierz akcje:")
print("1. Zabij Miniona")
print("2. Zabij gracza")
print("3. Zniszcz Towera")
print("4. Dive Towera")
choice = input("Wybierz swoją akcje wpisując od 1 do 4: ")

if choice == "1":
    Gold = Gold + 25
    xp = xp + 30 
elif choice == "2":
    Gold = Gold + 300
    xp = xp + 50  
elif choice == "3":
    Gold = Gold + 125 
elif choice == "4":
    print("You have died")
else:
    print("Nieprawidłowa liczba. Jestes AFK")