import sys  # Importiert das Modul für Kommandozeilenargumente (z.B. Text und Schlüssel)

def encode_text(text, key):
    """
    Verschlüsselt den Text mit dem Cäsar-Chiffre-Verfahren.
    
    Parameter:
    text (str): Der zu verschlüsselnde oder entschlüsselnde Text.
    key (int): Der Schlüssel für die Verschiebung der Buchstaben (positiv für Verschlüsselung, negativ für Entschlüsselung).
    
    Rückgabe:
    str: Der verschlüsselte oder entschlüsselte Text.
    """
    encrypted_text = ""  # Leerer String für das verschlüsselte Ergebnis

    # Schleife über jedes Zeichen im Text
    for char in text:
        # Wenn das Zeichen ein Kleinbuchstabe ist
        if char.islower():
            # Zykliche Verschiebung des Kleinbuchstabens im Alphabet
            new_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            encrypted_text += new_char
        # Wenn das Zeichen ein Großbuchstabe ist
        elif char.isupper():
            # Zykliche Verschiebung des Großbuchstabens im Alphabet
            new_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            # Andere Zeichen (z.B. Leerzeichen, Satzzeichen) bleiben unverändert
            encrypted_text += char
    
    return encrypted_text  # Rückgabe des verschlüsselten Texts

def string_histogram(text):
    """
    Zählt die Häufigkeit jedes Buchstabens im Text.

    Parameter:
    text (str): Der Eingabetext.

    Rückgabe:
    dict: Ein Wörterbuch mit Buchstaben als Schlüssel und deren Häufigkeit als Wert.
    """
    histogram = {}  # Leeres Dictionary für Häufigkeiten der Buchstaben
    
    # Schleife über jedes Zeichen im Text (in Kleinbuchstaben)
    for char in text.lower():
        if char.isalpha():  # Nur Buchstaben zählen
            # Wenn der Buchstabe bereits im Histogramm vorhanden ist, wird die Häufigkeit erhöht
            if char in histogram:
                histogram[char] += 1
            else:
                histogram[char] = 1
    
    return histogram  # Rückgabe des Histogramms

def frequencies(histogram):
    """
    Berechnet die Wahrscheinlichkeiten der Buchstaben auf Basis des Histogramms.

    Parameter:
    histogram (dict): Wörterbuch mit Buchstabenhäufigkeit.

    Rückgabe:
    list: Liste der Wahrscheinlichkeiten für jeden Buchstaben (a-z).
    """
    total_letters = sum(histogram.values())  # Gesamtanzahl aller Buchstaben im Text
    prob = [0] * 26  # Liste für Wahrscheinlichkeiten von a bis z
    
    # Berechnung der Wahrscheinlichkeit für jeden Buchstaben
    for char, count in histogram.items():
        index = ord(char) - ord('a')  # Bestimmung des Index des Buchstabens (0 = 'a', 25 = 'z')
        prob[index] = count / total_letters  # Berechnung der Wahrscheinlichkeit
    
    return prob  # Rückgabe der Wahrscheinlichkeiten

def format_frequencies(probabilities):
    """
    Formatiert die Wahrscheinlichkeiten der Buchstaben und gibt sie als Liste zurück.

    Parameter:
    probabilities (list): Liste der Wahrscheinlichkeiten für jeden Buchstaben.

    Rückgabe:
    list: Formatierte Ausgabe als Liste von Zeichen und deren Wahrscheinlichkeiten.
    """
    result = []
    # Iteration über alle Buchstaben von a bis z
    for i in range(26):
        letter = chr(ord('a') + i)  # Buchstabe anhand des Index berechnen
        prob = probabilities[i]  # Wahrscheinlichkeit des Buchstabens
        if prob > 0:  # Nur Buchstaben mit einer Wahrscheinlichkeit > 0% anzeigen
            result.append(f"{letter}={prob * 100:.1f}%,")
    
    # Optional: Alle Buchstaben mit 0% Wahrscheinlichkeit zusammenfassen
    zero_percent_letters = []
    for i in range(26):
        if probabilities[i] == 0:
            zero_percent_letters.append(chr(ord('a') + i))
    
    if zero_percent_letters:
        result.append(f"d-x=0%")  # "d-x" für Buchstaben mit 0% Häufigkeit
    
    return result  # Rückgabe der formatierten Ausgabe

def chi_squared(o, e):
    """
    Berechnet den Chi-Quadrat-Wert zwischen den beobachteten (o) und den erwarteten (e) Häufigkeiten.

    Parameter:
    o (list): Liste der beobachteten Häufigkeiten (verschlüsselter Text).
    e (list): Liste der erwarteten Häufigkeiten (Beispieltext).
    
    Rückgabe:
    float: Der Chi-Quadrat-Wert.
    """
    chi = 0
    for i in range(26):  # Für jeden Buchstaben a-z
        if e[i] > 0:  # Vermeidet Division durch Null
            chi += ((o[i] - e[i]) ** 2) / e[i]  # Berechnung des Chi-Quadrat-Werts
    
    return chi  # Rückgabe des Chi-Quadrat-Werts

def crack_caesar(exampletext, text):
    """
    Knackt den Cäsar-Chiffre basierend auf den Häufigkeiten des Beispieltexts.

    Parameter:
    exampletext (str): Beispieltext zur Berechnung der erwarteten Häufigkeiten.
    text (str): Der verschlüsselte Text, der entschlüsselt werden soll.

    Rückgabe:
    str: Der entschlüsselte Text.
    """
    # Berechnung der Histogramme und Wahrscheinlichkeiten des Beispieltexts und des verschlüsselten Texts
    example_histogram = string_histogram(exampletext)
    example_freq = frequencies(example_histogram)
    encrypted_histogram = string_histogram(text)
    encrypted_freq = frequencies(encrypted_histogram)
    
    # Teste alle möglichen Schlüssel (26 für das Alphabet)
    best_key = 0
    best_chi = float('inf')  # Setze den besten Chi-Quadrat-Wert initial auf unendlich
    
    for key in range(26):  # Schleife über alle Schlüsselwerte
        # Entschlüsselung mit dem aktuellen Schlüssel
        decrypted_text = encode_text(text, -key)
        decrypted_histogram = string_histogram(decrypted_text)
        decrypted_freq = frequencies(decrypted_histogram)
        
        # Berechnung des Chi-Quadrat-Werts für die aktuelle Entschlüsselung
        chi = chi_squared(decrypted_freq, example_freq)
        
        # Wenn der Chi-Quadrat-Wert besser (näher an Null) ist, setze den Schlüssel als besten
        if chi < best_chi:
            best_chi = chi
            best_key = key
    
    # Entschlüsselung mit dem besten Schlüssel
    decrypted_text = encode_text(text, -best_key)
    return decrypted_text  # Rückgabe des entschlüsselten Texts

def main():
    # Überprüfen, ob mindestens zwei Argumente übergeben wurden (Text und Schlüssel)
    if len(sys.argv) < 3:
        print("❌ Fehler: Bitte gib einen Text und einen Schlüssel an.")
        print("Beispiel: python CaesarCipher-1-d.py \"Text\" 3")
        sys.exit(1)  # Beendet das Programm mit einem Fehlercode

    text = sys.argv[1]  # Der zu verschlüsselnde Text
    try:
        key = int(sys.argv[2])  # Der Schlüssel wird als ganze Zahl gelesen
    except ValueError:
        # Fehlerbehandlung, falls der Schlüssel keine Zahl ist
        print("❌ Fehler: Der Schlüssel muss eine ganze Zahl sein.")
        sys.exit(1)
    
    # Verschlüsselten Text erzeugen
    encrypted_text = encode_text(text, key)
    print(f"\nVerschlüsselter Text: \n{encrypted_text}")
    
    # Wiedergabe der Häufigkeit vorkommender Buchstaben
    histogram = string_histogram(text)
    print(f"\nHäufigkeit vorkommender Buchstaben: \n{histogram}")
    
    # Berechnung der Wahrscheinlichkeiten und Ausgabe
    probabilities = frequencies(histogram)  # Wahrscheinlichkeiten berechnen
    formatted_output = format_frequencies(probabilities)  # Formatierte Ausgabe
    
    # Ausgabe der formatierten Wahrscheinlichkeiten
    print(f"\nWahrscheinlichkeiten der Buchstaben im Text:")
    print(f" ".join(formatted_output))
    
    # Entschlüsselten Text wiederherstellen
    decrypted_text = encode_text(encrypted_text, -key)
    print(f"\nEntschlüsselter Text: \n{decrypted_text}\n")

# Hauptprogramm starten
if __name__ == "__main__":
    main()  # Aufruf der main-Funktion