🎯 Lernziele

Werte in Variablen speichern.
Die grundlegenden Datentypen kennenlernen: int (ganze Zahlen), float (Dezimalzahlen) und str (Strings).
Typumwandlung (Casting) anwenden, insbesondere für die Verarbeitung von numerischen input()-Werten.

📝 Erklärung

Variablen sind Speicherplätze in unserem Programm. In Python definieren wir eine Variable, indem wir ihr einen Namen geben und ihr einen Wert zuweisen (z.B. alter = 30).

| Datentyp | Beschreibung  | Beispiel         |
|---------------------------------------------|
| int	   | Ganze Zahlen  | anzahl_autos = 5 |
| float	   | Dezimalzahlen | pi = 3.14159     |
| str	   | Text (String) | stadt = "Berlin" |

Achtung bei input(): Die input()-Funktion liefert immer einen String zurück. Willst du damit rechnen, musst du den String erst in eine Zahl umwandeln (casten) – z.B. mit int() oder float().

# Beispiel: Casten einer Variable
eingabe = input("Gib eine Zahl ein: ") # Eingabe ist ein String ("42")
zahl = int(eingabe) # Umwandlung in Integer (42)
ergebnis = zahl + 10 # Nun kann gerechnet werden

✍️ Aufgabe: Einfache Berechnung

Löse folgende Aufgabenstellung und nutze dafür die Datei 2_code.py:

Definiere die Variable basis_gehalt als int mit dem Wert 2500.
Nutze input(), um den Benutzer nach der Anzahl der Überstunden (als ganze Zahl) zu fragen.
Wandle die Überstunden-Eingabe in einen int-Wert um.
Definiere einen ueberstunden_satz als float (z.B. 15.50).
Berechne das gesamt_gehalt (basis_gehalt + (überstunden * überstunden_satz)).
Gib das gesamt_gehalt mit einer erklärenden Nachricht aus.