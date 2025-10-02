🎯 Lernziele

    Den Kontrollfluss des Programms mit if, elif und else steuern.

    Boolesche Ausdrücke und Vergleichsoperatoren (==, >, <=, !=) nutzen.

📝 Erklärung

Verzweigungen (oder Bedingungen) ermöglichen es deinem Programm, Entscheidungen zu treffen. Code in einem if-Block wird nur ausgeführt, wenn die Bedingung True (wahr) ist.

alter = 17

if alter >= 18:
    print("Du bist volljährig.") # Wird nur ausgeführt, wenn die Bedingung True ist
elif alter >= 16:
    print("Du bist fast volljährig.") # Alternative Bedingung
else:
    print("Du bist minderjährig.") # Fallback, wenn keine der Bedingungen True war

Wichtig: Achte auf die Einrückung (Indentation)! Python nutzt Einrückungen (typischerweise 4 Leerzeichen) statt Klammern, um Codeblöcke zu definieren.

✍️ Aufgabe: Der einfache Altersprüfer

Löse folgende Aufgabenstellung und nutze dafür die Datei 3_code.py:

Schreibe ein Programm mit dem überprüft werden kann, ob ein bestimmtes Jahr ein Schaltjahr ist. Der Benutzer soll dazu eine Jahreszahl eingeben können und das Programm soll als Feedback sagen, ob es sich bei dem Jahr um ein Schaltjahr handelt.

Ein Jahr ist ein Schaltjahr, wenn die Jahreszahl durch 4 teilbar ist. Ausnahme ist, wenn die Jahreszahl auch durch 100 teilbar ist. Dann ist es kein Schaltjahr. Wiederum ist die Ausnahme, wenn die Jahreszahl durch 400 teilbar ist. In dem Fall ist das Jahr doch ein Schaltjahr.

Tipp: Verwende "%". Hierbei handelt es sich um den Operator Modulo. Dieser funktioniert wie Division ohne Kommazahlen. Dabei wird nur der unteilbare Rest zurückgegeben.
Beispiel:
10 % 3 ergibt 1
8 % 5 ergibt 3
Mit zahl % 2 == 0 kannst du beispielsweise überprüfen, ob eine Zahl restlos geteilt werden kann