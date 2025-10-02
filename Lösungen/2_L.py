basis_gehalt = 2500
ueberstunden = input("Wie viele Überstunden hast du?: ")
ueberstunden = int(ueberstunden)
ueberstunden_satz = 15.5
gesamt_gehalt = basis_gehalt + ueberstunden * ueberstunden_satz
print("Dein Gehalt beträgt: " + str(gesamt_gehalt))