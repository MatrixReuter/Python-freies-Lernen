🎯 Lernziele

Werte in Variablen speichern.
Die grundlegenden Datentypen kennenlernen: int (ganze Zahlen), float (Dezimalzahlen), str (Strings) und bool.
Typumwandlung (Casting) anwenden, insbesondere für die Verarbeitung von numerischen input()-Werten.

📝 Erklärung

Variablen sind Speicherplätze in unserem Programm. In Python definieren wir eine Variable, indem wir ihr einen Namen geben und ihr einen Wert zuweisen (z.B. alter = 30).

| Datentyp | Beschreibung  | Beispiel         |
|---------------------------------------------|
| int	   | Ganze Zahlen  | anzahl_autos = 5 |
| float	   | Dezimalzahlen | pi = 3.14159     |
| str	   | Text (String) | stadt = "Berlin" |
| bool	   | Wahrheitswert | bestanden = True |

Achtung bei input(): Die input()-Funktion liefert immer einen String zurück. Willst du damit rechnen, musst du den String erst in eine Zahl umwandeln (casten) – z.B. mit int() oder float().

# Beispiel: Casten einer Variable
eingabe = input("Gib eine Zahl ein: ") # Eingabe ist ein String ("42")
zahl = int(eingabe) # Umwandlung in Integer (42)
ergebnis = zahl + 10 # Nun kann gerechnet werden

Das Casten kann auch gemeinsam mit der input Funktion aufegrufen werden:
zahl = int(input("Gib eine Zahl ein: "))

✍️ Aufgabe: Einfache Berechnung

Löse folgende Aufgabenstellung und nutze dafür die Datei 2_code.py:

Definiere die Variable Taschengeld als int mit dem Wert 25.
Nutze input(), um den Benutzer zu Fragen, wie viele Kaugummies er kaufen möchte (als ganze Zahl) zu fragen.
Wandle die Kaugummie-Eingabe in einen int-Wert um.
Definiere einen Preis für die Kaugummies als float (z.B. 1.50).
Berechne wie viel Geld der Benutzer bezahlen muss und wie viel Geld er nach dem Kauf noch hat.Gib den Gesamtpreis für die Kaugummies und das Restgeld des Benutzers aus.

Tipp: Zum Addieren verwende ein "+", zum Subtrahieren ein "-", zum Multiplizieren ein "*" und zum Dividieren ein "/" 