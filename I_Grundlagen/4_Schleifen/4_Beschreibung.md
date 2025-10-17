🎯 Lernziele

Den Code mit der while-Schleife wiederholt ausführen.

Die for-Schleife für eine festgelegte Anzahl von Wiederholungen (range()) oder über Sequenzen (Strings, Listen) nutzen.

Die Schlüsselwörter break und continue verstehen.

📝 Erklärung

Schleifen ermöglichen die Wiederholung von Anweisungen.

Bei Python gibt es while und for Schleifen. Wir stellen sie beide vor.

Die while-Schleife: Wiederholt den Code, solange die Bedingung wahr (True) ist. Du musst sicherstellen, dass die Bedingung irgendwann False wird (ansonsten: Endlosschleife!).

i = 0
while i < 3:
    print(f"Durchlauf {i}")
    i = i + 1 # Zähler erhöhen, damit die Schleife endet

for-Schleife: Ideal, um über eine Reihe von Werten zu iterieren. Die Funktion range(Anzahl) erzeugt eine Sequenz von Zahlen.

for zahl in range(5):
    print(f"Zähle bis: {zahl}") # Ausgabe: 0 bis 4

✍️ Aufgabe: Zahlen-Raten

Löse folgende Aufgabenstellung und nutze dafür die Datei 4_code.py:

Generiere eine zufällige Zahl zwischen 0 und 100.
Tipp: Nutze dazu randint(). Mit randint kannst du dir Zahlen generieren lassen. Um es zu verwenden, musst du es aber in deinen Code importieren.
Beispiel:
from random import randint #importiert die Funktion randint aus dem Modul random
zahl = randint(0,10) #generiert eine Zahl zwischen 0 und 10

Starte eine while-Schleife, die solange läuft, bis die Zahl erraten wurde.

Innerhalb der Schleife: Frage den Benutzer nach der Zahl.

Prüfe mit einer if-Verzweigung, ob die Eingabe der generierten Zahl entspricht.

Wenn es übereinstimmt, gib eine Erfolgsmeldung aus und nutze break, um die Schleife zu verlassen.

Wenn es nicht übereinstimmt, gib an, ob die gesuchte Zahl höher oder niedriger ist und starte den nächsten Versuch.