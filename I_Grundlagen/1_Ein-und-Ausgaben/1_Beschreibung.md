🎯 Lernziele

    - Die Funktion print() zur Ausgabe von Text in der Konsole nutzen.
    - Die Funktion input() zur Aufnahme von Benutzereingaben nutzen.
    - Mit Strings (Text) arbeiten und diese verketten.

📝 Erklärung

print() ist der erste Befehl, den man in Python lernt.
Er gibt Text oder den Inhalt von Variablen auf dem Bildschirm (Konsole) aus.
Alles, was in Anführungszeichen steht, wird als String (Text) behandelt.


# Beispiel: Text ausgeben
print("Hallo Welt!")
print("Programmieren macht Spaß")

Die Funktion input() wartet darauf, dass der Benutzer eine Eingabe macht und die ENTER-Taste drückt.
Die eingegebene Information wird als String zurückgegeben.


# Beispiel: Eingabe abfragen und direkt ausgeben
name = input("Wie ist dein Name? ")
print("Schön dich kennenzulernen, " + name)

Beachte, dass das "+" Zeichen Strings miteinander verbindet (verkettet).

✍️ Aufgabe: Begrüßung und Nachfrage

Löse folgende Aufgabenstellung und nutze dafür die Datei 1_code.py:

Gib eine Begrüßung aus, die den Zweck des Programms erklärt (z.B. "Willkommen zum Python-Kurs!").
Nutze input(), um den Benutzer nach seinem Namen zu fragen. Speichere die Antwort in einer geeigneten Variable.
Gib eine finale, personalisierte Nachricht aus.
Diese Nachricht muss sowohl die Begrüßung als auch den gespeicherten Namen enthalten (z.B. "Hallo [Name], schön das du da bist!").