🎯 Lernziele

Das Konzept der Klasse (Bauplan) und des Objekts (Instanz) verstehen.

Eine eigene Klasse mit Attributen (Eigenschaften) und Methoden (Funktionen) definieren.

Den Konstruktor __init__ zur Initialisierung von Objekten nutzen.

📝 Erklärung

Objektorientierte Programmierung (OOP) hilft, komplexe Programme besser zu organisieren. Eine Klasse ist wie ein Bauplan für etwas (z.B. ein Auto), während ein Objekt eine konkrete Instanz dieses Bauplans ist (z.B. mein rotes Auto).

Klasse definieren: Mit dem Schlüsselwort class.

Konstruktor (__init__): Diese spezielle Methode wird aufgerufen, wenn ein neues Objekt erstellt wird. Sie initialisiert die Attribute (Eigenschaften) des Objekts. self ist immer das erste Argument und referenziert das Objekt selbst.

Methoden: Normale Funktionen innerhalb der Klasse, die Aktionen des Objekts beschreiben.

class Hund:
    def __init__(self, name, rasse): # Konstruktor
        self.name = name # Attribut (Eigenschaft)
        self.rasse = rasse

    def bellen(self): # Methode (Aktion)
        print(f"{self.name} bellt: Wuff!")

# Objekt erstellen
mein_hund = Hund("Bello", "Golden Retriever")
mein_hund.bellen() # Methode aufrufen

✍️ Aufgabe: Der digitale Student

Löse folgende Aufgabenstellung und nutze dafür die Datei 7_code.py:

Definiere eine Klasse namens Student.

Die Klasse soll den Konstruktor __init__(self, name, matrikelnummer) haben, der zwei Attribute initialisiert.

Füge eine Methode namens zeige_info(self) hinzu, die Name und Matrikelnummer des Studenten in einem Satz ausgibt.

Erstelle zwei verschiedene Objekte (Instanzen) der Klasse Student mit eigenen Namen und Nummern.

Rufe für beide Objekte die Methode zeige_info() auf.