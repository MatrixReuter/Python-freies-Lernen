🎯 Lernziele

Grafische Elemente (Rechtecke) mit Pygame zeichnen.
Text (Schriftart, Rendering) auf dem Bildschirm ausgeben.
Button-Definitionen für die spätere Event-Verarbeitung vorbereiten.

📝 Erklärung

Nachdem das Fenster steht, können wir es mit Inhalt füllen. Pygame verwendet Funktionen wie pygame.draw.rect() zur Darstellung von Formen und das pygame.font-Modul zur Textanzeige.

Zeichnen: Die Funktion pygame.draw.rect(screen, Farbe, (x, y, Breite, Höhe)) zeichnet ein Rechteck. Dabei ist (x,y) die Position relativ zur oberen linken Ecke.

Text: Text wird nicht direkt gezeichnet, sondern muss zuerst in eine Oberfläche (Surface) gerendert werden (font.render()). Diese Oberfläche wird dann an der gewünschten Position auf den Bildschirm geblitzt (screen.blit()).

Buttons: Wir definieren die Buttons als Liste von Tupeln, wobei jedes Tupel den Text und die Startkoordinaten enthält.

✍️ Aufgabe: Eingabefeld und Buttons zeichnen

Nutze deinen funktionierenden Code aus 11. Mache ihn zu code.py und erweitere ihn wie folgt:

Definiere die Farben BLACK und GRAY.

Definiere eine Schriftart (font).
Tipp: Verwende dafür font = pygame.font.Font(None, 40)

Definiere die Variablen und die Button-Liste:

equation = "0" # Starteingabe
buttons = [
    ('/', 50, 100), ('*', 110, 100), ('-', 170, 100), ('+', 230, 100),
    ('=', 110, 160), ('C', 170, 160)
]

Zeichne innerhalb der Hauptschleife (nach screen.fill(WHITE)):

Ein graues Rechteck als Eingabefeld (oben, z.B. bei Position 50, 30 mit der Größe 200x40).

Den Text der equation-Variable im Eingabefeld (verwende font.render() und screen.blit()).
font.render benötigt 3 Argumente
    - den anzuzeigenden Text
    - Die Angabe True oder False, je nachdem ob die Kanten des Texts weich oder nicht weich sein sollen
    - Die Farbe des Texts
font.render gibt ein feritges Textobjekt zurück, welches mit screnn.blit() gezeichnet werden kann.
screen.blit benötigt 2 Arguemte
    - Das anzuzeigende Textobjekt
    - Die Ortsangabe, wo der Text angezeigt werden soll. Dabei müssen x und y wieder als Tupel angegeben werden

Eine Schleife über die buttons-Liste, um jeden Button als graues Rechteck und den jeweiligen Text darauf zu zeichnen.
Tipp: Verwende hier wieder die for-Schleife. Mit for text, x, y in buttons: bekommst du alle Buttons nacheinander

Ergebnis-Kontrolle: Dein Fenster sollte nun ein graues Eingabefeld mit einer "0" und alle Bedienelemente in einem statischen Layout anzeigen.