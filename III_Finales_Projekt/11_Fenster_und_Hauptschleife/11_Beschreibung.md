🎯 Lernziele

Pygame initialisieren und beenden.

Ein Programmfenster definieren und erstellen.

Das Prinzip der Hauptschleife (Event-Loop) verstehen und anwenden.

📝 Erklärung

Programme mit grafischer Oberfläche (GUI) wie unser Taschenrechner laufen nicht linear ab, sondern warten in einer Hauptschleife auf Ereignisse (Events), z.B. Mausklicks oder Tastenanschläge. Pygame benötigt dafür eine ständige Wiederholung, das sogenannte Event-Loop.

Initialisierung: Mit pygame.init() wird Pygame gestartet.

Fenster: Das Anzeigefenster wird mit pygame.display.set_mode() erstellt und erhält eine Größe in Pixeln. Da das Anzeigefenster im Programm wieder verwendet werden muss, ist es erforderlich, das Anzeigefenster in einer Variable abzuspeichern.
#Beispiel: screen = pygame.display.set_mode((BREITE, HÖHE))
#beachte, dass die Angabe zur Größe durch ein Tupel übergeben werden müssen

Hauptschleife (while running:):

Zeichnen: Der Bildschirm wird in jedem Durchlauf neu gezeichnet (z.B. mit einer Farbe gefüllt: screen.fill(WHITE)).

Events: Hier werden Aktionen des Benutzers verarbeitet (in dieser Lektion nur das Schließen des Fensters).

Aktualisierung: Mit pygame.display.flip() wird der gezeichnete Puffer auf dem Bildschirm sichtbar.

Wichtig: Ohne die Hauptschleife würde das Fenster sofort nach dem Öffnen wieder schließen, da das Programmende erreicht wäre.

✍️ Aufgabe: Minimal-Fenster

Löse folgende Aufgabenstellung und nutze dafür die Datei 11_code.py:

Pygame zu initialisieren und das System-Modul zu importieren.

Ein Fenster mit der Größe 300x250 Pixel und dem Titel "Pygame Taschenrechner" zu erstellen.
Tipp: Verwende zum setzen des Titels pygame.display.set_caption(TITEl)

Eine Hauptschleife zu starten, die den Bildschirm in der Farbe Weiß (WHITE = (255, 255, 255)) füllt.

Die Events so zu verarbeiten, dass das Programm korrekt beendet wird, wenn der Benutzer auf das Schließen-Symbol klickt (event.type == pygame.QUIT).
Tipp: Wie oben bereits beschrieben wurde, benötigt pygame für die Eventverarbeitung ein ständig wiederholendes Event-Loop benötigt.
Die Events können in Form einer Liste mit dem Befehl pygame.event.get() abgerufen werden.
Für die Iteration durch diese Eventliste kann bzw. dem Aufrufen jedes einzelnen Listeneintrags bietet sich die for-Schleife an.
Diese kann auch wie folgt angewendet werden:
for event in events: