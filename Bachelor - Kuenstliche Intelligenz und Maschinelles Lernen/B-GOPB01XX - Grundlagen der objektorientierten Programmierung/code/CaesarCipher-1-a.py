import sys  # Importiert das Modul für Kommandozeilenargumente

def encode_text(text, key):
    """
    Verschlüsselt den Text mit dem Cäsar-Verfahren.

    Parameter:
    text (str): Der Eingabetext (nur ASCII-Zeichen, keine Umlaute).
    key (int): Die Anzahl der Buchstaben, um die verschoben werden soll.

    Rückgabe:
    str: Der verschlüsselte (oder entschlüsselte) Text.
    """
    result = ""  # Ergebnis-String, wird Schritt für Schritt aufgebaut

    for char in text:  # Schleife über jedes Zeichen im Text
        if char.isupper():
            # Wenn es ein Großbuchstabe ist (A-Z):
            # ord('A') = 65, also wird A zur 0, B zur 1, ... Z zur 25
            # Danach wird um 'key' verschoben, modulo 26 (für Kreis)
            # Und wieder zurück in ein Zeichen umgewandelt
            shifted = ((ord(char) - ord('A') + key) % 26) + ord('A')
            result += chr(shifted)
        elif char.islower():
            # Wenn es ein Kleinbuchstabe ist (a-z), gleiches Prinzip wie oben
            shifted = ((ord(char) - ord('a') + key) % 26) + ord('a')
            result += chr(shifted)
        else:
            # Sonderzeichen (z. B. Leerzeichen, Punkt, Zahlen) bleiben unverändert
            result += char

    return result  # Rückgabe des verschlüsselten Textes

def main():
    # Überprüfen, ob mindestens zwei Argumente übergeben wurden:
    # sys.argv[0] ist der Dateiname selbst, [1] = Text, [2] = Schlüssel
    if len(sys.argv) < 3:
        print("❌ Fehler: Bitte gib einen Text und einen Schlüssel an.")
        print("Beispiel: python CaesarCipher-1-a.py \"Text\" 3")
        sys.exit(1)  # Beendet das Programm mit einem Fehlercode

    text = sys.argv[1]  # Der zu verschlüsselnde Text
    try:
        key = int(sys.argv[2])  # Der Schlüssel wird als ganze Zahl gelesen
    except ValueError:
        # Fehlerbehandlung, falls der Schlüssel keine Zahl ist
        print("❌ Fehler: Der Schlüssel muss eine ganze Zahl sein.")
        sys.exit(1)

    # Der Text wird mit dem Schlüssel verschlüsselt
    encrypted = encode_text(text, key)
    print("�� Verschlüsselter Text:", encrypted)  # Ausgabe des Ergebnisses

# Hauptprogramm starten, nur wenn dieses Skript direkt ausgeführt wird
if __name__ == "__main__":
    main()

    """
    So führst du das Skript aus:

    ➤ Verschlüsseln:
    Eingabe:
        python CaesarCipher-1-a.py "Das ist ein Text." 3
    Rückgabe:
        Verschlüsselter Text: Gdv lvw hlq Whaw.

    ➤ Entschlüsseln:
    Eingabe:
        python CaesarCipher-1-a.py "Gdv lvw hlq Whaw." -3
    Rückgabe:
        Verschlüsselter Text: Das ist ein Text.
    """