import os  # Importiert das Modul für das Arbeiten mit dem Dateisystem

# Funktion zum Ausdrucken der Verzeichnisstruktur
def print_directory(path, indentation_level=0, is_last=False, prefix=""):
    # Unicode Symbole für eine strukturierte Baumdarstellung
    HLINE = chr(9472)  # ─ (Horizontale Linie)
    VERT = chr(9474)   # │ (Vertikale Linie)
    LAST = chr(9492)   # └ (Letztes Element im Verzeichnisbaum)
    NODE = chr(9500)   # ├ (Anderes Element im Verzeichnisbaum)

    n_files = 0  # Zählt die Anzahl der Dateien
    n_dirs = 0   # Zählt die Anzahl der Verzeichnisse

    # Durchläuft die Verzeichniseinträge
    with os.scandir(path) as entries:
        entries = sorted(list(entries), key=lambda f: f.name.lower())  # Sortiert die Einträge alphabetisch
        total = len(entries)  # Gesamtzahl der Einträge (Dateien und Ordner)

        # Durchläuft jeden Eintrag im Verzeichnis
        for index, entry in enumerate(entries):
            # Bestimmt, ob der aktuelle Eintrag der letzte im Verzeichnis ist
            is_last_entry = (index == total - 1)
            # Wenn es der letzte Eintrag ist, verwenden wir das "LAST"-Symbol für die Baumstruktur
            connector = LAST if is_last_entry else NODE

            # Gibt den Eintrag mit dem entsprechenden Symbol aus
            print(f"{prefix}{connector}{HLINE*2} {entry.name}")

            # Wenn der Eintrag ein Verzeichnis ist, rufen wir die Funktion rekursiv auf
            if entry.is_dir():
                n_dirs += 1  # Erhöht den Zähler für Verzeichnisse
                # Bestimmt das neue Präfix für die nachfolgenden Einträge (zur Darstellung der Baumstruktur)
                new_prefix = prefix + ("    " if is_last_entry else VERT + "   ")
                # Rekursiver Aufruf der Funktion für Unterverzeichnisse
                files, dirs = print_directory(entry.path, indentation_level + 1, is_last_entry, new_prefix)
                n_files += files  # Fügt die Anzahl der Dateien aus dem Unterverzeichnis hinzu
                n_dirs += dirs    # Fügt die Anzahl der Verzeichnisse aus dem Unterverzeichnis hinzu
            else:
                # Wenn der Eintrag eine Datei ist, erhöhen wir den Datei-Zähler
                n_files += 1

    # Gibt die Anzahl der Dateien und Verzeichnisse im aktuellen Verzeichnis zurück
    return n_files, n_dirs


# Hauptprogramm
if __name__ == "__main__":
    # Ruft die Funktion auf und erhält die Anzahl der Dateien und Verzeichnisse
    n_files, n_dirs = print_directory(".")
    print()  # Leerzeile
    # Gibt die Gesamtzahl der Verzeichnisse und Dateien aus
    print(f"{n_dirs} directories, {n_files} files")