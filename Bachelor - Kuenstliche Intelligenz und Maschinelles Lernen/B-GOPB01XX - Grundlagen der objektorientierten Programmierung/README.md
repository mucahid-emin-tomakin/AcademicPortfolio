# 🕹️ B-GOPB01XX – Grundlagen der objektorientierten Programmierung

![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-007396?logo=java&logoColor=white)
![Status](https://img.shields.io/badge/Status-Abgeschlossen-brightgreen)

---

## 📖 Inhaltsverzeichnis

- [✨ FEATURES](#-features)
- [📝 PROJEKTBESCHREIBUNG](#-projektbeschreibung)
- [⚡ QUICK START](#-quick-start)
- [📁 STRUKTUR](#-struktur)
- [🚀 TOOL](#-tool)
- [⚠️ WICHTIGE HINWEISE](#️-wichtige-hinweise)
- [📝 LIZENZ](#-lizenz)
- [👤 AUTOR](#-autor)
- [📊 REPOSITORY STATISTIK](#-repository-statistik)

---

## ✨ FEATURES

| Feature | Beschreibung |
|---------|-------------|
| 🌳 Tree | Rekursive Verzeichnisstruktur mit Zählfunktion |
| 🔐 Cäsar-Chiffre | Verschlüsselung, Häufigkeitsanalyse & Chi-Quadrat-Entschlüsselung |
| 📡 CDMA | Code-Multiplexverfahren für parallele Datenübertragung |
| 📈 Glatte Kurve | Interaktives Polygon mit Corner-Cutting-Algorithmus |
| 🐍 Python | Drei schrittweise erweiterte Python-Projekte |
| ☕ Java | Komplexe objektorientierte Java-Anwendungen mit GUI |
| 📄 LaTeX-Satz | Professionelle Dokumentation mit eingebundenen Listings |

---

## 📝 PROJEKTBESCHREIBUNG

Das Dokument fasst vier aufeinander aufbauende Programmierprojekte zusammen, die grundlegende Techniken der objektorientierten Programmierung vermitteln. Zwei Projekte sind in Python, zwei in Java umgesetzt.

**1. Tree (Python)**  
- Schrittweise Entwicklung eines Tools zur baumartigen Darstellung von Verzeichnisstrukturen  
- Teil A: Einfache Ausgabe mit Unicode-Symbolen, alphabetisch sortiert  
- Teil B: Rekursiver Durchlauf aller Unterverzeichnisse mit dynamischer Einrückung  
- Teil C: Ergänzung um Datei- und Ordnerzähler mit Rückgabe als Tupel  

**2. Cäsar-Chiffre (Python)**  
- Teil A: Ver- und Entschlüsselung von ASCII-Text mit zyklischer Buchstabenverschiebung  
- Teil B: Erstellung eines Buchstaben-Histogramms (Häufigkeitswörterbuch)  
- Teil C: Berechnung des Wahrscheinlichkeitsvektors für a–z  
- Teil D: Automatisches Knacken des Codes mit Chi-Quadrat-Test und Shakespeare-Referenztext  

**3. CDMA – Code Division Multiple Access (Java)**  
- Teil A: Implementierung der Klasse `Chip` mit orthogonalen 4-stelligen Codes  
- Teil B: Codierung und Decodierung einzelner Bits mit `BitMessage` (Skalarprodukt)  
- Teil C: Übertragung ganzer ASCII-Zeichen (8 Bit) mit der Klasse `ByteMessage`  

**4. Glatte Kurve – Corner Cutting (Java)**  
- Teil A: Interaktives JFrame mit Maus-Listener zum Setzen von Polygonpunkten  
- Teil B: Unterteilungsschritt nach dem Corner-Cutting-Verfahren (75:25-Gewichtung)  
- Teil C: Mehrfache rekursive Unterteilung und farbliche Darstellung der glatten Kurve  
- Teil D: Auslagerung der Schrittzahl in separate Methode für beliebige Verfeinerungen  

Die gesamte Arbeit ist in **LaTeX** gesetzt und als PDF aus `main.tex` generierbar.

---

## ⚡ QUICK START

```bash
# Ins Projektverzeichnis wechseln
cd "Bachelor - Kuenstliche Intelligenz und Maschinelles Lernen/B-GOPB01XX - Grundlagen der objektorientierten Programmierung"

# LaTeX-Dokument kompilieren (mehrfach für Verzeichnisse & Referenzen)
pdflatex main.tex && pdflatex main.tex
# oder automatisch
latexmk -pdf main.tex

# Tree ausführen (Python)
cd code
python Tree-1-a.py
python Tree-1-b.py
python Tree-1-c.py

# Cäsar-Chiffre ausführen (Python)
python CaesarCipher-1-a.py "Das ist ein Text" 3
python CaesarCipher-1-b.py "Das ist ein Text" 3
python CaesarCipher-1-c.py "Das ist ein Text" 3
python CaesarCipher-1-d.py "Das ist ein Text" 3

# CDMA kompilieren und ausführen (Java)
javac CDMA1a.java && java CDMA1a
javac CDMA1b.java && java CDMA1b
javac CDMA1c.java && java CDMA1c

# Glatte Kurve kompilieren und ausführen (Java, mit GUI)
javac GlatteKurve1a.java && java GlatteKurve1a
javac GlatteKurve1b.java && java GlatteKurve1b
javac GlatteKurve1c.java && java GlatteKurve1c
```

---

## 📁 STRUKTUR

```text
B-GOPB01XX - Grundlagen der objektorientierten Programmierung/
├── 📁 code/
│   ├── ☕ CDMA1a.java
│   ├── ☕ CDMA1b.java
│   ├── ☕ CDMA1c.java
│   ├── 🐍 CaesarCipher-1-a.py
│   ├── 🐍 CaesarCipher-1-b.py
│   ├── 🐍 CaesarCipher-1-c.py
│   ├── 🐍 CaesarCipher-1-d.py
│   ├── ☕ GlatteKurve1a.java
│   ├── ☕ GlatteKurve1b.java
│   ├── ☕ GlatteKurve1c.java
│   ├── 🐍 Tree-1-a.py
│   ├── 🐍 Tree-1-b.py
│   └── 🐍 Tree-1-c.py
├── 📁 literature/
│   ├── 📝 acronym.tex
│   └── ⚙️ settings.tex
├── 📁 tex/
│   ├── 📘 CDMA (Java).tex
│   ├── 📘 Cäsar-Chiffre (Python).tex
│   ├── 📘 Deckblatt.tex
│   ├── 📘 Glatte Kurve (Java).tex
│   └── 📘 Tree (Python).tex
└── 📄 main.tex
```

### 📁 Struktur-Legende
```text
B-GOPB01XX - Grundlagen der objektorientierten Programmierung/
├── 📄 README.md          # Projektbeschreibung (diese Datei)
├── 📁 code/              # Quellcode (Python + Java)
│   ├── ☕ .java          # Java Skript
│   ├── 🐍 .py            # Python Skript
├── 📁 tex/               # LaTeX-Moduldateien für jedes Teilprojekt
├── 📁 literature/        # Literaturverzeichnis und Einstellungen
│   ├── 📝 acronym.tex    # Abkürzungsverzeichnis
│   └── ⚙️ settings.tex   # Dokument-Einstellungen
└── 📄 main.tex           # LaTeX-Hauptdokument
```

---

## 🚀 TOOL

| Bereich | Werkzeug |
|---------|----------|
| Dokumentation | LaTeX (erstellt mit Papeeria / lokalem TeXLive) |
| Programmierung | Python 3 (Tree, Cäsar-Chiffre), Java (CDMA, Glatte Kurve) |
| GUI | Java Swing (Glatte Kurve) |
| Versionskontrolle | Git & GitHub |

---

## ⚠️ WICHTIGE HINWEISE

- 🔒 Keine PDFs committen – das Repository enthält nur LaTeX‑Quelltexte und Code.
- 🎓 Eigenständigkeit – alle Beschreibungen sind in eigenen Worten formuliert.
- 📚 Quellenangaben – die Aufgabenstellung ist als separates Dokument verfügbar; externe Hilfsmittel sind im Dokument vermerkt.
- 🧪 Reproduzierbarkeit – das gesamte Dokument muss aus dem LaTeX‑Code heraus kompilierbar sein.

---

## 📝 LIZENZ

  Dieses Projekt ist unter der **MIT License** lizenziert - frei für persönliche und kommerzielle Nutzung.

---

## 👤 AUTOR

**Mücahid Emin Tomakin (TomaKing)**

| Platform | Link | Icon |
|----------|------|------|
| **GitHub** | [@mucahid-emin-tomakin](https://github.com/mucahid-emin-tomakin) | 🐙 |
| **Studium** | B.Sc. Künstliche Intelligenz & Maschinelles Lernen | 🎓 |

**Über dieses Repository:**
- 📘 Typ: Einsendeaufgabe / Programmierdokumentation
- 🎯 Ziel: Grundlegende Techniken der objektorientierten Programmierung in Python und Java
- 🛠️ Werkzeuge: Python, Java, LaTeX, Git

---

## 📊 REPOSITORY STATISTIK

| Metrik | Wert | Trend |
|--------|------|-------|
| **Stars** | ![GitHub Stars](https://img.shields.io/github/stars/mucahid-emin-tomakin/AcademicPortfolio) | 📈 |
| **Forks** | ![GitHub Forks](https://img.shields.io/github/forks/mucahid-emin-tomakin/AcademicPortfolio) | 🔄 |
| **Issues** | ![GitHub Issues](https://img.shields.io/github/issues/mucahid-emin-tomakin/AcademicPortfolio) | ✅ |
| **Letztes Update** | ![GitHub Last Commit](https://img.shields.io/github/last-commit/mucahid-emin-tomakin/AcademicPortfolio) | 🕐 |

---

### 🔧 Made with ❤️ on LaTeX
