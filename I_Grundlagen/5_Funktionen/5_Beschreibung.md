🎯 Lernziele

Funktionen definieren (def) und aufrufen.
Argumente an eine Funktion übergeben.
Werte mit return aus einer Funktion zurückgeben.
Den Vorteil von Funktionen zur Wiederverwendbarkeit verstehen.

📝 Erklärung

Funktionen helfen, den Code zu strukturieren und wiederverwendbar zu machen. Anstatt denselben Code mehrmals zu schreiben, definierst du ihn einmal und rufst ihn bei Bedarf auf.

def addiere(zahl1, zahl2): # Funktion mit zwei Argumenten definieren
    ergebnis = zahl1 + zahl2
    return ergebnis # Ergebnis zurückgeben

# Funktion aufrufen und Ergebnis speichern
summe = addiere(5, 3)
print(summe) # Ausgabe: 8

Die Funktion return beendet die Funktion und sendet den Wert an die aufrufende Stelle zurück. Ohne return gibt eine Funktion standardmäßig den Wert None zurück.

✍️ Aufgabe: Primzahl

Löse folgende Aufgabenstellung und nutze dafür die Datei 5_code.py:

Definiere eine Funktion namens ist_primzahl, die ein Argument (zahl) entgegennimmt.

Die Funktion soll überprüfen, ob die übergebene Zahl eine Primzahl ist und das Ergebnis zurückgeben.

Nutze input() (mit Typumwandlung!), um den Benutzer nach einer Zahl zu fragen.

Rufe deine Funktion mit den Benutzereingaben auf.

Gib das zurückgegebene Ergebnis mit einer erklärenden Nachricht aus.

Tipp: Eine Zahl ist eine Primzahl, wenn sie nur durch 1 und sich selbst teilbar ist. Beispiele sind 2, 3 und 5