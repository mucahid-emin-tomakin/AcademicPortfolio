import sys  # Importiert das Modul für Kommandozeilenargumente

def string_histogram(text): 
    """
    Zählt die Häufigkeit aller Buchstaben im übergebenen Text.

    Parameter:
    text (str): Der Eingabetext.

    Rückgabe:
    dict: Ein Dictionary mit Buchstaben (in Kleinbuchstaben) als Schlüssel 
          und ihrer Häufigkeit als Wert.
    """
    histogram = {}  # Leeres Wörterbuch zur Speicherung der Buchstabenhäufigkeit

    for char in text:  # Schleife über jedes Zeichen im Text
        if char.isalpha():  # Nur Buchstaben zählen, keine Zahlen oder Sonderzeichen
            char = char.lower()  # Großbuchstaben in Kleinbuchstaben umwandeln
            if char in histogram:
                # Wenn Buchstabe schon im Dictionary ist, Zähler erhöhen
                histogram[char] += 1
            else:
                # Wenn Buchstabe noch nicht enthalten ist, mit 1 starten
                histogram[char] = 1

    return histogram  # Rückgabe des fertigen Histogramms


def main():
    # Überprüfen, ob mindestens zwei Argumente übergeben wurden:
    # sys.argv[0] ist der Dateiname selbst, [1] = Text, [2] = Schlüssel
    if len(sys.argv) < 3:
        print("❌ Fehler: Bitte gib einen Text und einen Schlüssel an.")
        print("Beispiel: python CaesarCipher-1-b.py \"Text\" 3")
        sys.exit(1)  # Beendet das Programm mit einem Fehlercode

    text = sys.argv[1]  # Der zu verschlüsselnde Text
    try:
        key = int(sys.argv[2])  # Der Schlüssel wird als ganze Zahl gelesen
    except ValueError:
        # Fehlerbehandlung, falls der Schlüssel keine Zahl ist
        print("❌ Fehler: Der Schlüssel muss eine ganze Zahl sein.")
        sys.exit(1)
    histogram = string_histogram(text)  # Aufruf der Funktion zur Zählung
    print(histogram)  # Ausgabe des Ergebnisses als Dictionary


# Dieser Block stellt sicher, dass das Programm nur ausgeführt wird,
# wenn die Datei direkt gestartet wird (nicht beim Import in andere Dateien)
if __name__ == "__main__":
    main()