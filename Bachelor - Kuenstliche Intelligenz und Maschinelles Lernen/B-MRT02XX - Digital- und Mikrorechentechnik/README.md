# ⚙️ B-MRT02XX – Digital- und Mikrorechentechnik

![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?logo=arduino&logoColor=white)
![draw.io](https://img.shields.io/badge/draw.io-F08705?logo=diagramsdotnet&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-Abgeschlossen-brightgreen)

---

## 📖 INHALTSVERZEICHNIS

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

Diese Einsendeaufgabe befasst sich mit den **Grundlagen der Digital- und Mikrorechentechnik** – basierend auf den Studieninhalten der Module **MRT11**, **MRT12** und **MRT13** der Wilhelm Büchner Hochschule.

Die Arbeit gliedert sich in **sieben Aufgaben**, die von der Booleschen Algebra über Automatentheorie, KV-Diagramme und Assembler-Programmierung bis hin zur Mikrocontroller-Programmierung mit Arduino reichen.

**1. Boolesche Algebra (Aufgabe 1)**
- Vereinfachung zweier boolescher Gleichungen unter Anwendung der Gesetze von De Morgan, der doppelten Negation, der Idempotenz und der Absorption.
- Ergebnis 1a: \( y_1 = \overline{x_1} \cup \overline{x_2} \cup \overline{x_3} \)
- Ergebnis 1b: \( y_2 = x_1 \cup (x_3 \cap \overline{x_2}) \)

**2. Mealy-Automat (Aufgabe 2)**
- Entwurf eines Paritätsprüfers für serielle 3‑Bit‑Folgen mit sieben Zuständen (\( Z_1 \) bis \( Z_7 \)).
- Optimierung auf fünf Zustände durch Verlagerung der Ausgangslogik in die Zustände \( Z_4 \) und \( Z_5 \).
- Zustandsübergangstabellen und Zustandsgraphen als **draw.io**‑Diagramme.

**3. KV-Diagramm (Aufgabe 3)**
- Auswertung einer Wertetabelle mit vier Eingängen (\( A, B, C, D \)) und vier Ausgängen (\( Q_0, Q_1, Q_2, Q_3 \)).
- Erstellung der KV‑Diagramme für alle Ausgänge.
- Minimierte Gleichungen:
  - \( Q_0 = \overline{A} \cdot B \;\cup\; A \cdot \overline{B} \)
  - \( Q_1 = A \cdot \overline{C} \;\cup\; \overline{A} \cdot C \)
  - \( Q_2 = \overline{C} \cdot D \;\cup\; C \cdot \overline{D} \)
  - \( Q_3 = D \)
- Skizzierung der Gesamtschaltung mit UND‑, ODER‑ und NICHT‑Gattern.

**4. Digitaltechnik – Stack-Programmierung (Aufgabe 4)**
- Entwicklung eines maschinenorientierten Programms mit Stack als Zwischenspeicher.
- Laden von Registern mit 8‑Bit‑Konstanten (\( 20_h, 10_h, 80_h, 40_h \)).
- Pushen aller Register auf den Stack, Löschen und Wiederherstellen ausschließlich über den Stack.
- Manuelle Simulation zur Verifikation der Korrektheit.

**5. Flipflops – Schieberegister (Aufgabe 5)**
- Konstruktion einer Schieberegisterkette aus drei D‑Flipflops zur periodischen Erzeugung der Bitfolge \( 010011 \).
- Zustandsfolgetabelle, KV‑Diagramm für den Eingang \( D_0 \) und Schaltbild der Digitalschaltung.

**6. Arduino – Ampelsteuerung (Aufgabe 6)**
- Entwicklung eines Arduino‑Sketches für eine Vierphasen‑Ampel (Rot, Rot‑Gelb, Grün, Gelb) mit 5 Sekunden Pause zwischen den Zuständen.
- Endlosschleife mit `loop()`‑Funktion.

**7. Arduino – Würfelsteuerung (Aufgabe 7)**
- Entwurf einer Logik für einen elektronischen Würfel mit neun Anzeigeleuchten (\( a \)–\( i \)).
- Zuordnungs- und Wahrheitstabelle für vier Schalter (\( S_1 \)–\( S_4 \)).
- Minimierte Funktionsgleichungen in disjunktiver Normalform (DNF) für alle neun LEDs.

Die gesamte Arbeit wurde in **LaTeX** dokumentiert, alle Diagramme mit **draw.io** erstellt und die Arduino‑Sketche in der **Arduino‑IDE** entwickelt.

---

## ✨ FEATURES

| Feature | Beschreibung |
|---------|-------------|
| 📐 Boolesche Algebra | Schrittweise Vereinfachung mit De Morgan, doppelter Negation, Idempotenz und Absorption |
| 🔄 Mealy-Automat | Paritätsprüfer mit Zustandsgraphen und Übergangstabellen |
| 📊 KV-Diagramm | Vier Ausgänge minimiert, Gesamtschaltung mit UND/ODER/NICHT |
| 🧮 Stack-Programmierung | Assembler‑Code mit PUSH/POP und manueller Simulation |
| ⚡ Flipflops | Schieberegister mit D‑Flipflops und periodischer Bitfolge |
| 🚦 Arduino-Ampel | Vier Phasen mit 5 Sekunden Pause |
| 🎲 Arduino-Würfel | Neun LEDs, vier Schalter, DNF‑Gleichungen |
| 📄 LaTeX‑Dokumentation | Professionelles Layout mit Abbildungs‑, Tabellen‑ und Code‑Verzeichnis |
| 🔗 Versionskontrolle | Git & GitHub für Nachvollziehbarkeit |

---

## 🚀 TOOL

| Bereich | Werkzeug |
|---------|----------|
| **Dokumentation** | LaTeX (kompiliert mit texlive / Papeeria) |
| **Diagramme** | draw.io (https://app.diagrams.net) |
| **Arduino-Sketche** | Arduino‑IDE 2.x |
| **Versionskontrolle** | Git & GitHub |
| **Betriebssystem** | Windows 11 (22H2) |

---

## 📁 STRUKTUR

```text
📓 B-MRT02XX - Digital- und Mikrorechentechnik/
├── 📄 README.md                                      # Diese Datei
├── 📄 main.tex                                        # LaTeX‑Hauptdokument
│
├── 📁 asset/
│   ├── 📁 code/                                       # Code‑Listings (als .tex)
│   │   ├── 📝 Aufgabe4.tex                            # Assembler‑Programm
│   │   └── 📝 Aufgabe6.tex                            # Arduino‑Ampel
│   │
│   └── 📁 image/                                      # Abbildungen (draw.io)
│       ├── 🖼️ Aufgabe2.png                            # Mealy‑Automat (7 Zustände)
│       ├── 🖼️ Aufgabe2II.png                          # Mealy‑Automat (5 Zustände)
│       ├── 🖼️ Aufgabe3.png                            # KV‑Diagramm Gesamtschaltung
│       ├── 🖼️ Aufgabe5.png                            # Schieberegister Schaltbild
│       └── 🖼️ WBH.png                                 # WBH‑Logo (Titelseite)
│
├── 📁 chapter/                                        # LaTeX‑Kapitel
│   ├── 📝 Einleitung.tex
│   ├── 📝 Aufgabe1.tex
│   ├── 📝 Aufgabe2.tex
│   ├── 📝 Aufgabe3.tex
│   ├── 📝 Aufgabe4.tex
│   ├── 📝 Aufgabe5.tex
│   ├── 📝 Aufgabe6.tex
│   ├── 📝 Aufgabe7.tex
│   └── 📝 Zusammenfassung.tex
│
└── 📁 config/                                         # Konfiguration & Einstellungen
    ├── 📝 acronym.tex                                 # Abkürzungsverzeichnis
    ├── 📝 bibliography.bib                            # Literaturverzeichnis
    ├── 📝 settings.tex                                # Dokument‑Einstellungen
    └── 📝 titlepage.tex                               # Titelseite mit Matrikelnummer
```

### 📁 Struktur-Legende
```text
📓 B-MRT02XX - Digital- und Mikrorechentechnik/
├── 📄 README.md              # Projektbeschreibung (diese Datei)
├── 📄 main.tex               # LaTeX‑Hauptdokument
├── 📁 asset/
│   ├── 📁 code/              # Code‑Listings (Assembler, Arduino)
│   └── 📁 image/             # draw.io‑Diagramme (PNG)
├── 📁 chapter/               # LaTeX‑Kapitel (Einleitung, 7 Aufgaben, Zusammenfassung)
└── 📁 config/                # Einstellungen, Abkürzungen, Literatur, Titelseite
```

---

## ⚡ QUICK START

### 📦 Git & GitHub
```bash
# Repository klonen
git clone https://github.com/mucahid-emin-tomakin/AcademicPortfolio.git
cd AcademicPortfolio

# Ins Projektverzeichnis wechseln
cd "Bachelor - Kuenstliche Intelligenz und Maschinelles Lernen/B-MRT02XX - Digital- und Mikrorechentechnik"
```

### 📝 LaTeX Kompilierung

**Option A: Lokal mit LaTeX**
```bash
# Einmalig (mehrfach für Verzeichnisse & Referenzen)
pdflatex main.tex && pdflatex main.tex

# Automatisch mit latexmk (empfohlen)
latexmk -pdf main.tex
```

**Option B: Docker (empfohlen, keine lokale LaTeX-Installation nötig)**
```bash
# Kompilieren mit texlive/texlive-Image (vollständige LaTeX-Distribution)
docker run --rm -v "${PWD}:/work" -w /work texlive/texlive latexmk -pdf main.tex

# Bei Pfaden mit Leerzeichen die Anführungszeichen setzen
docker run --rm -v "${PWD}:/work" -w /work texlive/texlive latexmk -pdf main.tex
```
- Das `texlive/texlive-Image` wird beim ersten Mal heruntergeladen (ca. 4 GB).
- Alle folgenden Kompilierungen sind sofort verfügbar.
- Die generierte `main.pdf` erscheint im Projektordner.

**Option C: Online mit Papeeria**
```bash
# 1. Gehe auf https://m.papeeria.com
# 2. Erstelle ein neues Projekt und importiere den gesamten Ordner als ZIP
# 3. Papeeria kompiliert main.tex automatisch in der Cloud
```

### 🖼️ Diagramme bearbeiten (optional)

1. Öffne [draw.io](https://app.diagrams.net)
2. Klicke auf **Datei → Import → Aus XML**
3. Lade die gewünschte `.png`-Datei aus `asset/image/` (oder bearbeite direkt die XML-Quelle)
4. Exportiere als PNG und überschreibe die Datei im `asset/image/`-Ordner

**Vorhandene Diagramme:**
- `Aufgabe2.png` – Mealy-Automat mit 7 Zuständen
- `Aufgabe2II.png` – Mealy-Automat mit 5 Zuständen (optimiert)
- `Aufgabe3.png` – Gesamtschaltung der KV-Diagramme
- `Aufgabe5.png` – Schieberegisterkette mit D-Flipflops

---

## ⚠️ WICHTIGE HINWEISE

- 🎓 **Eigenständigkeit** – alle Lösungen und die LaTeX‑Dokumentation sind eigenständig verfasst.
- 📚 **Quellenangaben** – alle zitierten Aussagen sind mit den Studienheften MRT11 [2], MRT12 [1] und MRT13 [3] hinterlegt.
- 🧪 **Reproduzierbarkeit** – das gesamte Dokument muss aus den LaTeX‑Quellen kompilierbar sein; alle Code‑Listings sind im Ordner `asset/code/` enthalten.
- 🌍 **Plattformunabhängigkeit** – die Arbeit wurde unter Windows 11 (22H2) entwickelt, die verwendeten Tools sind jedoch plattformunabhängig.
- ⚠️ **Git LF/CRLF Warnungen** – die Warnungen `LF will be replaced by CRLF` sind unproblematisch und treten bei Windows‑Entwicklern auf; sie betreffen nur die Zeilenenden der Dateien.

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
- 📘 Typ: Einsendeaufgabe / Fachdokumentation
- 🎯 Ziel: Lösung der B‑Prüfung B‑MRT02XX – Digital- und Mikrorechentechnik
- 🛠️ Werkzeuge: LaTeX, draw.io, Arduino‑IDE, Git

---

## 📊 REPOSITORY STATISTIK

| Metrik | Wert | Trend |
|--------|------|-------|
| **Stars** | ![GitHub Stars](https://img.shields.io/github/stars/mucahid-emin-tomakin/AcademicPortfolio) | 📈 |
| **Forks** | ![GitHub Forks](https://img.shields.io/github/forks/mucahid-emin-tomakin/AcademicPortfolio) | 🔄 |
| **Issues** | ![GitHub Issues](https://img.shields.io/github/issues/mucahid-emin-tomakin/AcademicPortfolio) | ✅ |
| **Letztes Update** | ![GitHub Last Commit](https://img.shields.io/github/last-commit/mucahid-emin-tomakin/AcademicPortfolio) | 🕐 |

---

### 🔧 Made with ❤️ on LaTeX and draw.io
