Armor = 30
MagicRes = 30

lvl = float(input("Enter your champion level:  "))

while lvl in range(1,19):
    Armor = 30 + 5 * lvl
    MagicRes = 30 + 4 * lvl
    print("Armor:    ",Armor)
    print("MagicRes: ",MagicRes)
    break
else:
    print("Wrong Champion level")