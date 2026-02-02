import os  # Importiert das Modul für die Interaktion mit dem Dateisystem

def print_directory(path):
    # Definition der Zeichen für das Zeichnen der Verzeichnisstruktur
    HLINE = chr(9472)  # ─ (Horizontale Linie)
    VERT = chr(9474)   # │ (Vertikale Linie)
    LAST = chr(9492)   # └ (Letztes Element)
    NODE = chr(9500)   # ├ (Verzweigungspunkt)

    # Öffnen des angegebenen Verzeichnispfads und Durchsuchen der Einträge
    with os.scandir(path) as entries:
        # Sortieren der Einträge alphabetisch (unabhängig von Groß-/Kleinschreibung)
        entries = sorted(entries, key=lambda f: f.name.lower())
        total = len(entries)  # Anzahl der Einträge im Verzeichnis

        # Schleife durch alle Einträge im Verzeichnis
        for i, entry in enumerate(entries):
            # Prüfen, ob der Eintrag der letzte in der Liste ist
            if i == total - 1:
                symbol = LAST + HLINE + HLINE  # Wenn letzter Eintrag, verwende └──
            else:
                symbol = NODE + HLINE + HLINE  # Andernfalls verwende ├──
            print(symbol, entry.name)  # Ausgabe des Symbols und des Namens des Eintrags

# Hauptprogramm, das die Funktion mit dem aktuellen Verzeichnis aufruft
if __name__ == "__main__":
    print_directory(".")  # Aufruf der Funktion mit dem aktuellen Verzeichnis