🎯 Lernziele

Den Code mit der while-Schleife wiederholt ausführen.

Die for-Schleife für eine festgelegte Anzahl von Wiederholungen (range()) oder über Sequenzen (Strings, Listen) nutzen.

Die Schlüsselwörter break und continue verstehen.

📝 Erklärung

Schleifen ermöglichen die Wiederholung von Anweisungen.

Bei Python gibt es while und for Schleifen. Wir stellen sie beide vor.

Die while-Schleife: Wiederholt den Code, solange die Bedingung wahr (True) ist. Du musst sicherstellen, dass die Bedingung irgendwann False wird (ansonsten: Endlosschleife!).
Eine Möglichkeit dafür ist, dass eine Variable als Zähler fungiert. Damit kann festgelegt werden, wie häufig die Schleife ausgeführt werden soll.

i = 0
while i < 3:
    print("Durchlauf " + str(i))
    i = i + 1 # Zähler erhöhen, damit die Schleife endet

while-Schleifen können auch durch ein break beendet werden.

while True:
    user = input("Schreibe 'stop' zum beenden: )
    if user == "stop":
        break

Ein break wird als unelegant angesehen. Eine Alternative ist das Verwenden von boolschen Variablen

waiting = True
while waiting:
    user = input("Schreibe 'stop' zum beenden: )
    if user == "stop":
        waiting = False

for-Schleife: Ideal, um über eine Reihe von Werten zu iterieren. Die Funktion range(Anzahl) erzeugt eine Sequenz von Zahlen.

for zahl in range(5):
    print("Zähle bis: " + str(zahl)) # Ausgabe: 0 bis 4

Die Variable zahl ist hierbei lokal und existiert nur innerhalb der for-Schleife. Ihr Wert steigt in jedem Zyklus um 1.
Die range Funktion kann 1 bis 3 Argumente empfangen. Geben wir nur einen Wert ein, so legen wir damit nur den Endwert fest (wobei mit Erreichen des Endwerts die Schleife beendet wird). Die lokale Variable beginnt bei 0.
Geben wir 2 Werte ein, so legt der erste Wert den Startwert für die lokale Variable fest und die zweite den Endwert. range(2, 5) im obrigen Beispiel würde nur die Ausgaben 2 bis 4 erzeugen.
Geben wir 3 Werte ein, so legen die ersten beiden Werte wie zuvor Start- und Endwert der lokalen Variable fest. Der dritte Wert gibt an, um wie viel die lokale Variable je Zyklus erhöht wird. Beispiel:
for i in range(2, 10, 3):
    print(i) # Erzeugt die Ausgaben 2, 5, 8

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