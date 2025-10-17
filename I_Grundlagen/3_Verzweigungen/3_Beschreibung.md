🎯 Lernziele

    Den Kontrollfluss des Programms mit if, elif und else steuern.

    Boolesche Ausdrücke und Vergleichsoperatoren (==, >, <=, !=) nutzen.

📝 Erklärung

Verzweigungen (oder Bedingungen) ermöglichen es deinem Programm, Entscheidungen zu treffen.
In Abhängigkeit von bestimmten Ereignissen können wir den Computer unterschiedliche Dinge tun lassen.
Im Code nutzen wir dazu if-Blöcke. Code in einem if-Block wird nur ausgeführt, wenn die Bedingung True (wahr) ist.

es_regnet = True
if es_regnet:
    print("Nimm einen Schirm mit nach draußen")

Beachte, dass alles, was zu dem if-Block gehört, mit einem TAB eingerückt werden muss. Die TAB-Taste findest du ganz links auf deiner Tastatur. Sie hat normalerweise zwei Pfeile, von denen einer nach links und der andere nach rechts zeigt.

Wir können innerhalb eines if-Blocks auch weitere Dinge überprüfen, wenn die erste Bedingung nicht stimmt. Dazu verwenden wir elif. elif bedeutet "else if" bzw. "ansonsten wenn". elifs können wir unendlich viele innerhalb eines if-Blocks verwenden.
Mit else können wir zudem eine Abzweigung schaffen, welche ausgeführt wird, wenn alle vorherigen if un elif Bedingungen falsch waren. else hat selbst keine Bedingung.

alter = 17

if alter >= 18:
    print("Du bist volljährig.") # Wird nur ausgeführt, wenn die Bedingung True ist
elif alter >= 16:
    print("Du bist fast volljährig.") # Alternative Bedingung
else:
    print("Du bist minderjährig.") # Fallback, wenn keine der Bedingungen True war

Wichtig: Achte auf die Einrückung (Indentation)! Python nutzt wie vorher bereits erwähnt Einrückungen (typischerweise 4 Leerzeichen oder ein TAB) statt Klammern, um Codeblöcke zu definieren.

✍️ Aufgabe: Der einfache Altersprüfer

Löse folgende Aufgabenstellung und nutze dafür die Datei 3_code.py:

Schreibe ein Programm mit dem überprüft werden kann, ob ein bestimmtes Jahr ein Schaltjahr ist. Der Benutzer soll dazu eine Jahreszahl eingeben können und das Programm soll als Feedback sagen, ob es sich bei dem Jahr um ein Schaltjahr handelt.

Ein Jahr ist ein Schaltjahr, wenn die Jahreszahl durch 4 teilbar ist. Ausnahme ist, wenn die Jahreszahl auch durch 100 teilbar ist. Dann ist es kein Schaltjahr. Wiederum ist die Ausnahme, wenn die Jahreszahl durch 400 teilbar ist. In dem Fall ist das Jahr doch ein Schaltjahr.
Beispiele:
2024 -> Ist ein Schaltjahr, weil es durch 4 teilbar ist
2100 -> Ist kein Schaltjahr, weil es zwar durch 4 teilbar ist, aber auch durch 100
2000 -> Ist ein Schaltjahr, obwohl es durch 100 teilbar ist. Weil es durch 400 teilbar ist, ist es ein Schaltjahr.
2025 -> Ist kein Schaltjahr, weil es nicht durch 4 teilbar ist.

Wichtiger Hinweis: 400 ist ein Vielfaches von 100, 100 ist ein Vielfaches von 4. Bei der Verwendung von if und mehreren elifs wird nur die Abzweigung ausgeführt, bei der zuerst die Bedingung stimmte. Wenn beispielsweise 1900 zuerst auf die Teilbarkeit durch 4 überprüft wird, wird die Teilbarkeit auf 100 nicht mehr überprüft.

Tipp: Verwende "%". Hierbei handelt es sich um den Operator Modulo. Dieser funktioniert wie Division ohne Kommazahlen. Dabei wird nur der unteilbare Rest zurückgegeben.
Beispiel:
10 % 3 ergibt 1
8 % 5 ergibt 3
Mit zahl % 2 == 0 kannst du beispielsweise überprüfen, ob eine Zahl restlos geteilt werden kann