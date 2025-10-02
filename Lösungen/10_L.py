while True:
    berechnung = input("Gib die vollständige Rechnung ein oder schreibe 'ende', wenn du das Programm beenden möchtest: ")
    if berechnung == "ende":
        break
    try:
        print(eval(berechnung))
    except Exception:
        print("Ungültige Gleichung. Bitte korrigiere die Eingabe.")
        