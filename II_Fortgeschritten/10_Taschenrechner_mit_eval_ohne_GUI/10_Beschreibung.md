🎯 Lernziele

Die Leistungsfähigkeit und die Sicherheitsrisiken der Funktion eval() verstehen.

Einen Taschenrechner bauen, der eine komplette Gleichung als String verarbeitet.

📝 Erklärung

Während der Taschenrechner in Lektion 9 nur eine Operation gleichzeitig verarbeiten konnte, kann die eingebaute Python-Funktion eval() (Evaluate) einen String nehmen und diesen als gültigen Python-Ausdruck ausführen.

gleichung = "4 + 5 * 2"
ergebnis = eval(gleichung)
print(ergebnis) # Ausgabe: 14 (beachtet die Punkt-vor-Strich-Regel!)

Sicherheitshinweis: eval() ist sehr mächtig und sollte in echten Anwendungen nur mit vertrauenswürdigen Eingaben verwendet werden, da es beliebigen Python-Code ausführen kann! Für unsere Lernzwecke ist es jedoch ideal, um komplexe Ausdrücke zu verarbeiten.

Wir nutzen den try/except-Block aus Lektion 8, um potenzielle Fehler in der eingegebenen Gleichung (z.B. Tippfehler oder unvollständige Ausdrücke) elegant abzufangen.

✍️ Aufgabe: Komplexer Rechner

Löse folgende Aufgabenstellung und nutze dafür die Datei 10_code.py:

Nutze eine while True-Schleife, um den Taschenrechner kontinuierlich laufen zu lassen, bis der Benutzer ihn beendet (z.B. durch Eingabe von "ende").

Lasse den Benutzer die komplette Gleichung als String eingeben (z.B. "15 * (4 + 2) / 3").

Prüfe mit einem if, ob der Benutzer "ende" eingegeben hat, und nutze break (aus Lektion 4), um die Schleife zu verlassen.

Umschließe den Aufruf von eval() mit einem try/except-Block:

Im try-Block: Führe die Berechnung durch und gib das Ergebnis aus.

Im except-Block: Fange alle generischen Fehler ab (oder den spezifischeren SyntaxError) und gib eine Meldung wie "Ungültige Gleichung. Bitte korrigiere die Eingabe." aus.