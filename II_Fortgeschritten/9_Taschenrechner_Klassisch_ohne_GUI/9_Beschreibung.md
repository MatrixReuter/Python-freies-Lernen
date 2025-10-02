🎯 Lernziele

Die in den Grundlagen gelernten Konzepte (Input, Funktionen, Verzweigungen) in einem größeren Projekt zusammenführen.

Eine logische Struktur zur Auswahl einer Operation erstellen.

📝 Erklärung

In dieser Lektion bauen wir den Kern unseres Taschenrechners, indem wir Funktionen für die Grundrechenarten definieren und die Verzweigungen (if/elif) nutzen, um basierend auf der Benutzereingabe die richtige Funktion auszuwählen.

Dies ist ein ausgezeichnetes Beispiel für Funktionale Programmierung, da wir kleine, spezialisierte Funktionen verwenden, die in einer Hauptstruktur zusammengefasst werden.

Vorgehen:

Definiere Funktionen für addieren, subtrahieren, etc.

Nimm zwei Zahlen und eine Operation (als String, z.B. "+") als Input.

Nutze if/elif, um zu prüfen, welche Operation gewählt wurde, und rufe die entsprechende Funktion auf.

✍️ Aufgabe: Vier-Grundrechenarten

Löse folgende Aufgabenstellung und nutze dafür die Datei 9_code.py:

Definiere die vier Funktionen: addieren(x, y), subtrahieren(x, y), multiplizieren(x, y) und dividieren(x, y). Jede Funktion soll das Ergebnis zurückgeben.

Lasse den Benutzer zwei Zahlen eingeben (mit Typumwandlung zu float).

Lasse den Benutzer die gewünschte Operation (+, -, *, /) eingeben.

Implementiere eine Kette von if, elif, else, um:

Bei gültiger Operation die entsprechende Funktion aufzurufen und das Ergebnis auszugeben.

Im else-Fall eine Fehlermeldung ("Ungültige Operation!") auszugeben.

Bonus: Schließe die Division in einen try/except-Block ein, um die ZeroDivisionError und ValueError abzufangen (aus Lektion 8).