import os  # Importiert das Modul für die Interaktion mit dem Dateisystem

def print_directory(path, indentation_level=0, is_last=False, prefix=""):
    # Unicode-Symbole für die Baumstruktur-Darstellung
    HLINE = chr(9472)  # ─ (Horizontale Linie)
    VERT = chr(9474)   # │ (Vertikale Linie)
    LAST = chr(9492)   # └ (Symbol für das letzte Element)
    NODE = chr(9500)   # ├ (Symbol für die Verzweigung)

    # Öffnet das Verzeichnis und liest die Einträge
    with os.scandir(path) as entries:
        # Sortiert die Einträge alphabetisch (unabhängig von der Groß-/Kleinschreibung)
        entries = sorted(list(entries), key=lambda f: f.name.lower())
        total = len(entries)  # Gesamtzahl der Einträge im Verzeichnis

        # Durchläuft alle Einträge im Verzeichnis
        for index, entry in enumerate(entries):
            # Überprüft, ob der aktuelle Eintrag der letzte in der Liste ist
            is_last_entry = (index == total - 1)
            # Wählt das Symbol für die Verbindung (├── oder └──)
            connector = LAST if is_last_entry else NODE

            # Gibt den Eintrag mit der Baumstruktur aus
            print(f"{prefix}{connector}{HLINE*2} {entry.name}")

            # Wenn der Eintrag ein Verzeichnis ist, wird die Funktion rekursiv für dieses Verzeichnis aufgerufen
            if entry.is_dir():
                # Bestimmt, wie der Baum im nächsten rekursiven Schritt angezeigt wird
                new_prefix = prefix + ("    " if is_last_entry else VERT + "   ")
                # Rekursiver Aufruf für das Verzeichnis
                print_directory(entry.path, indentation_level + 1, is_last_entry, new_prefix)

# Hauptprogramm
if __name__ == "__main__":
    # Startet die Ausgabe für das aktuelle Verzeichnis (".")
    print_directory(".")