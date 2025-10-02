try:
    zaehler = int(input("Gib einen Zähler ein: "))
    nenner = int(input("Gib einen Nenner ein: "))

    print("Der Wert des Division lautet: " + str(zaehler/nenner))
except ValueError:
    print("Es können nur Zahlen eingegeben werden")
except ZeroDivisionError:
    print("Der Nenner darf nicht 0 sein")

