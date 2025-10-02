from random import randint

generiert = randint(0, 100)

while True:
    benutzer_zahl = int(input("Tippe eine Zahl: "))
    if benutzer_zahl == generiert:
        break
    elif benutzer_zahl < generiert:
        print("Die gesuchte Zahl ist größer")
    else:
        print("Die gesuchte Zahl ist kleiner")
print("Wunderbar, du hast die Zahl erraten!")