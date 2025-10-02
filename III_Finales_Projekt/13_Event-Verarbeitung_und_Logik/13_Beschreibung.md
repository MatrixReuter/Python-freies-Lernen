🎯 Lernziele

Maus- und Tastatur-Events auslesen und verarbeiten.

Die Koordinaten von Mausklicks nutzen, um den gedrückten Button zu erkennen.

Die eingebaute Python-Funktion eval() zur Berechnung der Gleichung verwenden.

📝 Erklärung

Die volle Funktionalität des Taschenrechners kommt durch die Event-Verarbeitung in der Hauptschleife.

Mausklicks (pygame.MOUSEBUTTONDOWN): Wenn ein Klick registriert wird, müssen wir die Mausklick-Koordinaten (mx, my) mit den Koordinaten der Buttons vergleichen.

Koordinaten-Check: Für jeden Button prüft man: Ist mx zwischen der linken Kante (x) und der rechten Kante (x + 50) UND ist my zwischen der oberen Kante (y) und der unteren Kante (y + 50)?

Die Logik:

Ziffern/Operatoren: Werden zur Variablen equation hinzugefügt.

'C' (Clear): Setzt equation auf einen leeren String ("").

'=' (Gleich): Führt die Berechnung durch. Die Funktion eval(equation) interpretiert den String als Python-Ausdruck und gibt das Ergebnis zurück (z.B. eval("5+3") gibt 8 zurück).

Fehlerbehandlung: Da eval() bei ungültigen Ausdrücken (z.B. "5+") abstürzt, muss der Aufruf in einen try...except-Block eingeschlossen werden, um eine Error-Meldung anzuzeigen.

✍️ Aufgabe: Interaktiven Rechner fertigstellen

Nutze deinen funktionierenden Code aus 12. Füge ihn zu 13_code.py und implementiere die gesamte Event-Verarbeitung aus dem vollständigen Code-Beispiel:

Implementiere die Maus-Event-Verarbeitung:

Finde heraus, welcher Button geklickt wurde.
Tipp: Um die Position des Mauszeigers zu bekommen, verwende pygame.mouse.get_pos() -> hier werden x und y als einzelne Argumente zurück gegeben

Füge Ziffern/Operatoren zu equation hinzu.

Implementiere die Logik für 'C' (Löschen) und '=' (Berechnung mit try-except und eval()).

Implementiere die Tastatur-Event-Verarbeitung (pygame.KEYDOWN):

Erlaube die Eingabe von Ziffern und Operatoren.
Tipp: mit event.unicode.isdigit() kannst du herausfinden, ob die geklickte Taste eine Zahl ist.
event.unicode (ohne Klammern) gibt das geklickte Tastensymbol zurück

Implementiere ENTER (pygame.K_RETURN) als '=' Funktion.

Implementiere die Rücktaste (pygame.K_BACKSPACE) zum Löschen des letzten Zeichens.
Tipp: Strings können wie eine Liste gelesen werden. Mit [:-1] wird der komplette String mit Ausnahme des letzten Zeichens zurück gegeben.


Ergebnis-Kontrolle: Dein Taschenrechner sollte jetzt voll funktionsfähig sein. Teste ihn gründlich!


⭐ Zusatzaufgabe (Vertiefung)

Für Schüler, die schnell fertig sind:

Design-Anpassung: Verändere das Layout des Taschenrechners. Ordne die Tasten wie bei einem Standardrechner in einem 4x4-Gitter an.

Weitere Funktion: Füge eine Klasse Calculator hinzu, die die Methode zur Berechnung (calculate()) und die Fehlerbehandlung kapselt, anstatt eval() direkt in der Hauptschleife zu verwenden.