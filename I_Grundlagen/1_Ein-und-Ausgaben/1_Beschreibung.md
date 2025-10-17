🎯 Lernziele

    - Die Funktion print() zur Ausgabe von Text in der Konsole nutzen.
    - Die Funktion input() zur Aufnahme von Benutzereingaben nutzen.
    - Mit Strings (Text) arbeiten und diese verketten.

📝 Erklärung

print() ist der erste Befehl, den man in Python lernt.
Er kann dazu genutzt werden, um alle möglichen Arten von Ausgaben zu machen.
Da ein Programm sonst eine Art Blackbox ist, können wir uns mit print verschiedene Daten während der Programmlaufzeit ausgeben lassen.
Print kann sowohl Texte oder den Inhalt von Variablen in der Konsole ausgeben.
Alles, was in Anführungszeichen steht, wird als String (Text) behandelt.
String ist eine Variable, welche eine Zeichenkette darstellt. Weitere Variablen werden im nächsten Kapitel vorgestellt.

# Beispiel: Text ausgeben
print("Hallo Welt!")
print("Programmieren macht Spaß")


Die Funktion input() wartet darauf, dass der Benutzer eine Eingabe macht und die ENTER-Taste drückt.
Die eingegebene Information wird grundsätzlich als String zurückgegeben.


# Beispiel: Eingabe abfragen und direkt ausgeben
name = input("Wie ist dein Name? ")
print("Schön dich kennenzulernen, " + name)

Beachte, dass das "+" Zeichen Strings miteinander verbindet (verkettet).
Der String "Wie ist dein Name? " in input ist lediglich ein Hilfstext für den Anwender des Programms. Er hat darüberhinaus keine Bedeutung.
Beachte, dass unter der Variable name der Wert abgespeichert wird, welchen der User über die Konsole nach Programmstart eingibt. Dieser Wert wird innerhalb der print Funktion eingegeben.

✍️ Aufgabe: Begrüßung und Nachfrage

Löse folgende Aufgabenstellung und nutze dafür die Datei 1_code.py:

Gib eine Begrüßung aus, die den Zweck des Programms erklärt (z.B. "Willkommen zum Python-Kurs!").
Nutze input(), um den Benutzer nach seinem Namen zu fragen. Speichere die Antwort in einer geeigneten Variable.
Gib eine finale, personalisierte Nachricht aus.
Diese Nachricht muss sowohl die Begrüßung als auch den gespeicherten Namen enthalten (z.B. "Hallo [Name], schön das du da bist!").