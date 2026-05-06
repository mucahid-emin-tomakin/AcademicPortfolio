# 🕹️ B-INF01XX – Einführungsprojekt für Informatiker

![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)
![UML](https://img.shields.io/badge/UML-Modellierung-orange)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-Abgeschlossen-brightgreen)

---

## 📖 Inhaltsverzeichnis

- [📝 PROJEKTBESCHREIBUNG](#-projektbeschreibung)
- [✨ FEATURES](#-features)
- [🚀 TOOL](#-tool)
- [📁 STRUKTUR](#-struktur)
- [⚡ QUICK START](#-quick-start)
- [⚠️ WICHTIGE HINWEISE](#️-wichtige-hinweise)
- [📝 LIZENZ](#-lizenz)
- [👤 AUTOR](#-autor)
- [📊 REPOSITORY STATISTIK](#-repository-statistik)

---

## 📝 PROJEKTBESCHREIBUNG

Das Projekt dokumentiert einen vollständigen, softwaretechnischen Arbeitsablauf – von der Anforderungsanalyse über die UML‑Modellierung bis zur Implementierung und kritischen Reflexion. Im Mittelpunkt steht die Entwicklung des klassischen Spiels **Pong**, das in vier Aufgaben schrittweise erweitert wird.

**1. Projektdokumentation & Reflexion**  
- Kickoff-Meeting mit Klärung der Projektziele und Rahmenbedingungen (Zielplattform Linux, Steuerung, Spielregeln)  
- Erstellung von Storyboards und verbaler Anforderungsdefinition  
- Analysephase mit Nominal-/Verbalphrasenanalyse und CRC-Karten  
- Entwurf von Konzept‑ und Implementierungsklassendiagrammen  
- Implementierung auf einem Raspberry Pi unter Python mit den Bibliotheken **pygame** und der internen **spiel.py**  
- Testphase (Fehlerdokumentation, z. B. fehlender Startbutton, ungenaue KI-Bewegung)  
- Detaillierte Zeitaufstellung für jeden Arbeitsschritt  
- Abschließende persönliche Reflexion über den Projektverlauf, Teamarbeit und den Einsatz von Bibliotheken  

**2. Pong mit farbigen Objekten**  
Der Ball wird rot, der linke Schläger grün und der rechte Schläger blau dargestellt. Dazu wird eine von `Ball` abgeleitete Klasse `ColoredBall` verwendet; die Schlägerfarben werden direkt gesetzt.

**3. Tastatursteuerung & ESC-Abbruch**  
Erweiterung um eine von `Schlaeger` abgeleitete Klasse `TastaturSchlaeger` und eine von `Spiel` abgeleitete Klasse `SpielErweitert`, die auf die Pfeiltasten (hoch/runter) reagiert und das Spiel bei Druck auf ESC beendet.

**4. Individuelle Erweiterung**  
Ein eigenes Feature: Der Ball ändert seine Farbe bei jedem Abprall an der X‑Achse (wird schwarz) und an der Y‑Achse (wird rot). Dadurch verschwindet er zeitweise, was den Schwierigkeitsgrad erhöht. Umgesetzt durch Überschreiben der `bounce()`-Methode in `ColoredBall`.

Alle Textteile, Diagramme und Codeausschnitte sind im LaTeX-Hauptdokument `main.tex` zusammengeführt und über **Papeeria** (Online-LaTeX-Editor) kompiliert worden. Die entstehenden PDFs sind nicht im Repository enthalten, sondern nur die Quellen.

---

## ✨ FEATURES

| Feature | Beschreibung |
|---------|-------------|
| 📋 Projekttagebuch | Detaillierter Projektverlauf mit Zeitaufwänden, Entscheidungen und Ergebnissen |
| 🎨 UML-Diagramme | Konzept‑ und Implementierungsdiagramme für das Softwaredesign |
| 🖼️ Storyboards | Visuelle Planung der Benutzeroberfläche und Spielinteraktion |
| 🕹️ Pong‑Implementierung | Lauffähiges Pong‑Spiel mit farbigen Objekten |
| ⌨️ Tastatursteuerung | Umstellung von Maus‑ auf Tastaturbedienung inkl. ESC‑Abbruch |
| 🚀 Eigenes Feature | Selbstentwickelte Erweiterung (farbwechselnder Ball bei Kollision) |
| 🔍 Reflexion | Kritische Betrachtung des gesamten Projektablaufs mit Pro/Contra |
| 📄 LaTeX‑Satz | Professionelle Dokumentation mit eingebundenen Grafiken und Listings |
| ☁️ Online-Editor | Erstellung und Kompilierung mit Papeeria (keine lokale Installation nötig) |

---

## 🚀 TOOL

| Bereich | Werkzeug |
|---------|----------|
| Dokumentation | LaTeX (erstellt mit Papeeria / lokalem TeXLive) |
| Programmierung | Python 3, pygame, spiel.py (projektinterne Bibliothek) |
| Modellierung | UML (Klassendiagramme, erstellt mit [draw.io](https://app.diagrams.net/)) |
| Versionskontrolle | Git & GitHub |
| Betriebssystem (Ziel) | Oracle VM Linux (Debian) |

---

## 📁 STRUKTUR

```text
📓 B-INF01XX - Einfuehrungsprojekt für Informatiker/
├── 📁 img/
│   ├── 🖼️ Aufgabe2Ergebnis.png
│   ├── 🖼️ Aufgabe2Konzeptklassendiagramm.png
│   ├── 🖼️ Aufgabe3Konzeptklassendiagramm.png
│   ├── 🖼️ Aufgabe4Ergebnis.png
│   ├── 🖼️ Aufgabe4ErgebnisII.png
│   ├── 🖼️ Aufgabe4Konzeptklassendiagramm.png
│   ├── 🖼️ EigenesStoryBoard.jpg
│   ├── 🖼️ Implementierungsklassendiagramm.png
│   ├── 🖼️ Konzeptklassendiagramm.png
│   └── 🖼️ StoryBoard.png
└── 📄 main.tex
```

### 📁 Struktur-Legende
```text
📓 B-INF01XX - Einführungsprojekt für Informatiker/
├── 📄 README.md          # Projektbeschreibung (diese Datei)
├── 📁 img/               # Bilder, Screenshots, Storyboards, Diagramme
└── 📄 main.tex           # LaTeX-Hauptdokument
```

---

## ⚡ QUICK START

### 📦 Git & GitHub
```bash
# Repository klonen
git clone https://github.com/mucahid-emin-tomakin/AcademicPortfolio.git
cd AcademicPortfolio

# Ins Projektverzeichnis wechseln
cd "Bachelor - Kuenstliche Intelligenz und Maschinelles Lernen/B-INF01XX - Einfuehrungsprojekt für Informatiker"
```

### 📝 LaTeX Kompilierung
```bash
# LaTeX-Dokument kompilieren (mehrfach für Verzeichnisse & Referenzen)
pdflatex main.tex && pdflatex main.tex
# oder automatisch
latexmk -pdf main.tex

# Alternativ: Online mit Papeeria arbeiten
# 1. Gehe auf https://m.papeeria.com
# 2. Erstelle ein neues Projekt und importiere den gesamten Ordner als ZIP
# 3. Papeeria kompiliert main.tex automatisch in der Cloud
```

### 🐍 Python virtueller Umgebung
```bash
# Python‑Spiele starten (benötigt pygame und die mitgelieferte spiel.py)
python aufgabe2.py
python aufgabe3.py
python aufgabe4.py

# Mit virtueller Umgebung
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

## ⚠️ WICHTIGE HINWEISE

- 🔒 Keine PDFs committen – das Repository enthält nur LaTeX‑Quelltexte, Bilder und Python‑Dateien.
- 🎓 Eigenständigkeit – alle Beschreibungen, Reflexionen und Analysen sind in eigenen Worten formuliert.
- 📚 Quellenangaben – externe Hilfsmittel wie ChatGPT (für Rückfragen) sind im Dokument vermerkt.
- 🧪 Reproduzierbarkeit – das gesamte Dokument muss aus dem LaTeX‑Code heraus kompilierbar sein, entweder lokal oder über Papeeria.

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
- 📘 Typ: Einsendeaufgabe / Projektdokumentation
- 🎯 Ziel: Simulation eines berufspraktischen IT-Projektablaufs
- 🛠️ Werkzeuge: Werkzeuge: Python, pygame, LaTeX (Papeeria), UML, Git

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
