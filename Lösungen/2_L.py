taschengeld = 25
anzahl_kaugummies = input("Wie viele Kaugummies möchtest du kaufen?: ")
anzahl_kaugummies = int(anzahl_kaugummies)
kaugummie_preis = 1.5
kaugummie_kosten = anzahl_kaugummies * kaugummie_preis
taschengeld = taschengeld - kaugummie_kosten
print("Die " + str(anzahl_kaugummies) + " Kaugummies kosten: " + str(kaugummie_kosten) + " Euro")
print("Dein Guthaben beträgt noch " + str(taschengeld) + " Euro")