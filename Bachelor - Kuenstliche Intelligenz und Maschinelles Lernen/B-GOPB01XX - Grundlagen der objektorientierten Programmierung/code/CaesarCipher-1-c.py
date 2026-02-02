import sys  # Importiert das Modul für Kommandozeilenargumente

def string_histogram(text):
    """
    Zählt die Buchstabenhäufigkeit im gegebenen Text.

    Parameter:
    text (str): Eingabetext

    Rückgabe:
    dict: Buchstabenhäufigkeit (nur a–z)
    """
    histogram = {}  # Leeres Dictionary für die Häufigkeit der Buchstaben

    for char in text:  # Schleife über jedes Zeichen im Text
        if char.isalpha():  # Überprüft, ob das Zeichen ein Buchstabe ist (a-z, A-Z)
            char = char.lower()  # Wandelt den Buchstaben in Kleinbuchstaben um
            # Wenn der Buchstabe schon im Dictionary ist, wird der Wert (Häufigkeit) erhöht,
            # andernfalls wird er mit 1 initialisiert
            histogram[char] = histogram.get(char, 0) + 1

    return histogram  # Rückgabe des Histogramms mit der Häufigkeit der Buchstaben


def frequencies(histogram):
    """
    Berechnet die Wahrscheinlichkeiten für jeden Buchstaben a–z 
    basierend auf einem Histogramm.

    Parameter:
    histogram (dict): Dictionary mit Buchstabenhäufigkeit

    Rückgabe:
    list: Liste mit 26 Wahrscheinlichkeiten (Position 0 = 'a', ..., Position 25 = 'z')
    """
    total_letters = sum(histogram.values())  # Gesamtanzahl aller Buchstaben im Text
    freq_list = [0.0] * 26  # Initialisiert eine Liste mit 26 Einträgen (für a-z)

    for letter, count in histogram.items():  # Schleife durch das Histogramm
        if letter.isalpha():  # Überprüft, ob es sich wirklich um einen Buchstaben handelt
            # Berechnet den Index des Buchstabens (0 für 'a', 1 für 'b', ..., 25 für 'z')
            index = ord(letter.lower()) - ord('a')
            # Berechnet die Wahrscheinlichkeit als Häufigkeit / Gesamtanzahl der Buchstaben
            freq_list[index] = count / total_letters

    return freq_list  # Rückgabe der Wahrscheinlichkeitsliste


def main():
    # Überprüfen, ob mindestens zwei Argumente übergeben wurden:
    # sys.argv[0] ist der Dateiname selbst, [1] = Text, [2] = Schlüssel
    if len(sys.argv) < 3:
        print("❌ Fehler: Bitte gib einen Text und einen Schlüssel an.")
        print("Beispiel: python CaesarCipher-1-c.py \"Text\" 3")
        sys.exit(1)  # Beendet das Programm mit einem Fehlercode

    text = sys.argv[1]  # Der zu verschlüsselnde Text
    try:
        key = int(sys.argv[2])  # Der Schlüssel wird als ganze Zahl gelesen
    except ValueError:
        # Fehlerbehandlung, falls der Schlüssel keine Zahl ist
        print("❌ Fehler: Der Schlüssel muss eine ganze Zahl sein.")
        sys.exit(1)
    hist = string_histogram(text)  # Aufruf der Funktion, um das Histogramm zu berechnen
    freqs = frequencies(hist)  # Berechnung der Wahrscheinlichkeiten basierend auf dem Histogramm

    # Ausgabe der Wahrscheinlichkeiten in Prozent
    print("�� Buchstabenhäufigkeit (in %):")
    for i, freq in enumerate(freqs):
        letter = chr(ord('a') + i)  # Berechnet den Buchstaben basierend auf dem Index
        # Ausgabe des Buchstabens und der Wahrscheinlichkeit (in Prozent)
        print(f"{letter}: {freq * 100:.2f}%")

# Dieser Block sorgt dafür, dass das Programm nur ausgeführt wird,
# wenn dieses Skript direkt gestartet wird
if __name__ == "__main__":
    main()