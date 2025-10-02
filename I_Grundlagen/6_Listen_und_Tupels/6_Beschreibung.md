🎯 Lernziele

Listen ([]) und Tupel (()) als geordnete Sammlungen von Daten verwenden.
Auf einzelne Elemente über den Index zugreifen (Index beginnt bei 0!).
Die wichtigsten Listenmethoden (append(), remove()) anwenden.

Den Unterschied zwischen veränderbar (Liste) und unveränderbar (Tupel) verstehen.

📝 Erklärung

Datenstrukturen erlauben es, mehrere Werte unter einem Namen zu speichern.

Listen (List): Werden mit eckigen Klammern [] erstellt und sind veränderbar (mutable). Du kannst Elemente hinzufügen (append()), entfernen (remove()) oder ändern.

einkaufsliste = ["Milch", "Brot", "Eier"]
einkaufsliste.append("Käse") # Fügt "Käse" am Ende hinzu
print(einkaufsliste[1]) # Ausgabe: Brot (Index 1)

Tupel (Tuple): Werden mit runden Klammern () erstellt und sind unveränderbar (immutable). Das bedeutet, einmal erstellte Tupel können nicht mehr verändert werden – ideal für feste Datensätze (z.B. Koordinaten).

koordinaten = (10, 25)
print(koordinaten[0]) # Ausgabe: 10
# koordinaten[0] = 12 würde einen Fehler geben!

✍️ Aufgabe: To-Do-Manager

Löse folgende Aufgabenstellung und nutze dafür die Datei 6_code.py:

Erstelle eine leere Liste namens todo_liste.

Nutze eine for-Schleife und die Funktion range(3), um den Benutzer dreimal nach einer Aufgabe zu fragen. Füge jede Eingabe mit .append() der todo_liste hinzu.

Erstelle ein Tupel namens prioritaet mit den Elementen "Hoch", "Mittel", "Niedrig".

Nutze eine for-Schleife (oder eine while-Schleife), um alle Elemente in der todo_liste auszugeben. Gib dabei den Index des Elements und die Aufgabe aus.
Tipp: mit der Funktion len() kannst du die Länge einer Liste ermitteln

Zusatz (Listenmethode): Frage den Benutzer am Ende, welche Aufgabe er bereits erledigt hat (gib die Nummer/den Index ein). Entferne die entsprechende Aufgabe mit der Methode .pop(Index).