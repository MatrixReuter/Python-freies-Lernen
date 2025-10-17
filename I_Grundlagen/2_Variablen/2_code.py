basis_gehalt = 2500
ueberstunden = int(input("Wie viele Überstunden hast du?: "))
ueberstunden_satz = 15.5
gesamt_gehalt = basis_gehalt + ueberstunden_satz * ueberstunden
print("Gesamtgehalt: " + str(gesamt_gehalt))