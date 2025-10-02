🎯 Lernziele

Exceptions (Ausnahmen/Fehler) erkennen und abfangen.

Den try, except-Block zur sicheren Code-Ausführung nutzen.

Programme vor dem Absturz durch unerwartete Benutzereingaben schützen.

📝 Erklärung

Wenn ein Programm auf einen Fehler stößt (z.B. Division durch Null oder falsche Typumwandlung), stürzt es ab (es wird beendet und zeigt eine Fehlermeldung). Um das zu verhindern, nutzen wir Exception Handling.

Der try-Block enthält den Code, der fehlschlagen könnte.
Der except-Block enthält den Code, der ausgeführt wird, falls ein Fehler auftritt.

try:
    zahl = int(input("Gib eine ganze Zahl ein: ")) # Kann fehlschlagen (ValueError)
    ergebnis = 10 / zahl # Kann fehlschlagen (ZeroDivisionError)
    print("Ergebnis: ", ergebnis)
except ValueError:
    print("Das war keine gültige Zahl. Bitte versuche es erneut.")
except ZeroDivisionError:
    print("Du kannst nicht durch Null teilen!")
except: # Fängt alle anderen Fehler ab (weniger spezifisch)
    print("Ein unbekannter Fehler ist aufgetreten.")

✍️ Aufgabe: Sichere Division

Löse folgende Aufgabenstellung und nutze dafür die Datei 8_code.py:

Frage den Benutzer nacheinander nach zwei Zahlen (Nenner und Zähler). Verwende dabei input() und versuche, die Eingaben in float umzuwandeln.

Umschließe die gesamte Logik (Eingabe und Berechnung) mit einem try-Block.

Berechne im try-Block die Division der beiden Zahlen.

Implementiere einen spezifischen except-Block für den ValueError (wenn der Benutzer Text statt Zahlen eingibt) und gib eine entsprechende Fehlermeldung aus.

Implementiere einen spezifischen except-Block für den ZeroDivisionError und gib eine entsprechende Warnung aus.