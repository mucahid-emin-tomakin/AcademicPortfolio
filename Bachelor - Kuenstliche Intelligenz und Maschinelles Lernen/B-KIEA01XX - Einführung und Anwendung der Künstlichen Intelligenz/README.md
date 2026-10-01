# 📊 B-KIEA01XX – Einführung und Anwendung der Künstlichen Intelligenz

![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![SWI-Prolog](https://img.shields.io/badge/SWI--Prolog-9.x-EF3E42?logo=swi-prolog&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF6F00)
![matplotlib](https://img.shields.io/badge/matplotlib-3.x-11557C?logo=matplotlib&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white)
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

Diese Einsendeaufgabe befasst sich mit der **Implementierung eines Multiagenten-Logistik-Simulationsspiels** – basierend auf den Studieninhalten der Module *Grundlagen der Künstlichen Intelligenz* (KII00), *Suche und Planung* (KII04A), *Wissensrepräsentation* (KII11), *Maschinelles Lernen* (KII12) und *Begleitliteratur* (KIIBU) der Wilhelm Büchner Hochschule.

Mehrere Lieferroboter (Agenten) bewegen sich auf einer diskreten 2D-Karte, verteilen Lieferaufträge untereinander über das **Contract-Net-Protokoll** und planen ihre Wege mit dem **A\*-Algorithmus**. Die Wissensbasis wird zusätzlich in **SWI-Prolog** repräsentiert und als Vorfilter in die Simulation integriert.

Die Arbeit gliedert sich in fünf Hauptaufgaben, die Theorie mit praktischer Umsetzung verbinden:

**1. Karten- und Agentenmodell (Aufgabe 1)**
- Diskrete 2D-Karte (71×15 Zellen) mit ASCII-Art-Wandmuster, 2 Depots, 4 Zielen und 55 Engpass-Zellen
- Zwei Agententypen: **Standard** (Speed 1, Kapazität 5) und **Express** (Speed 2, Kapazität 3)
- Hauptschleife mit Nachrichtenbus, Kollisionsauflösung und Batteriesystem
- Grafische Darstellung mit **Tkinter** (schwarzer Hintergrund, Akzentfarbe `#2CFF05`)

**2. Agenten-Kommunikation und Auftragsvergabe (Aufgabe 2)**
- **Contract-Net-Protokoll** mit den drei Nachrichtentypen `ANNOUNCE`, `BID`, `AWARD`
- Periodische Paketgenerierung (alle 10 Steps), Bieterverfahren mit **Manhattan-Distanz** als Kostenfunktion
- Zuschlagslogik mit deterministischem Tie-Breaker (minimale Kosten, dann Agent-ID)

**3. Wegsuche (Aufgabe 3)**
- Graph-Erzeugung aus der Karte mit typspezifischen Kantenkosten (`BaseCost / speed`) und Engpass-Aufschlag
- **A\*-Algorithmus** mit Manhattan-Heuristik und Prioritätswarteschlange (`heapq`)
- Agenten-Integration: Zustandsautomat (`TO_DEPOT` → `PICKUP` → `TO_TARGET` → `DELIVER`) mit Replanning bei Blockaden
- Verbesserte **BFS-Heuristik** mit Lazy-Cache (58 % weniger Expansionen)

**4. PROLOG-Wissensbasis (Aufgabe 4)**
- Fakten-Export (`facts.pl`) mit `road/2`, `wall/2`, `depot/3`, `target/3`
- Regeln (`rules.pl`) für `bottleneck/2`, `cost/3`, `vertex/3`, `reachable/2`, `candidate_agent/2`
- **subprocess-Brücke** zu SWI-Prolog als Vorfilter vor A\* und Contract-Net-Bieten

**5. Simulationsexperimente und Auswertung (Aufgabe 5)**
- 15 Simulationsläufe (3 Konfigurationen: 3 / 5 / 10 Agenten × 5 Seeds × 200 Steps)
- Leistungskennzahlen, A\*-Metriken, Kommunikationsmetriken und Konfliktanalyse
- Automatische **Plot-Generierung** (matplotlib), CSV-Export und statistische Aggregation

Die gesamte Simulation wurde in **Python 3.10** mit **Tkinter** implementiert, die Wissensbasis in **SWI-Prolog** repräsentiert und die Ergebnisse in einer **LaTeX-Dokumentation** festgehalten.

---

## ✨ FEATURES

| Feature | Beschreibung |
|---------|-------------|
| 🗺️ Diskretes Kartenmodell | ASCII-Art-basierte 2D-Karte mit Depots, Zielen und Engpass-Analyse |
| 🤖 Multiagentensystem | Standard- und Express-Agenten mit eigenem Zustandsautomaten |
| 📨 Contract-Net-Protokoll | ANNOUNCE, BID, AWARD – vollständige Auktionslogik mit Tie-Breaker |
| 🧭 A\*-Wegsuche | Prioritätswarteschlange, zulässige Manhattan-Heuristik, Pfad-Rekonstruktion |
| 🔁 Replanning | Automatische Neuplanung bei Kollisionen und Blockaden |
| ⚡ BFS-Heuristik | Wall-aware Alternative zur Manhattan-Heuristik (58 % weniger Expansionen) |
| 🧠 PROLOG-Wissensbasis | Fakten-Export, Regeln für Erreichbarkeit und Kandidatenauswahl |
| 🔗 PROLOG-Brücke | subprocess-Anbindung an SWI-Prolog mit Fallback auf Python |
| 🎨 Tkinter-GUI | Dynamische Karten-Skalierung, Step-/AutoRun-Buttons, Info-Zeile |
| 📊 Experiment-Runner | 15 Läufe, Aggregation, Histogramme, Boxplots, CSVs |
| 📈 Leistungsmetriken | Lieferzeit, Erfolgsquote, Pfadlänge, A\*-Expansionen, Nachrichten, Konflikte |
| 📄 LaTeX-Dokumentation | Professionelles Layout mit allen Code-Listings und Plots |
| 🔗 Versionskontrolle | Git & GitHub für Nachvollziehbarkeit und Reproduzierbarkeit |

---

## 🚀 TOOL

| Bereich | Werkzeug |
|---------|----------|
| **Programmiersprache** | Python 3.10 |
| **Logikprogrammierung** | SWI-Prolog 9.x |
| **GUI-Framework** | Tkinter (Python-Standardbibliothek) |
| **Data-Science-Bibliotheken** | matplotlib, seaborn, numpy, pandas |
| **Paketmanagement** | Miniforge mit conda-forge-Kanal |
| **Dokumentation** | LaTeX (kompiliert mit TeXLive / Papeeria) |
| **Versionskontrolle** | Git & GitHub |

---

## 📁 STRUKTUR

```text
📓 B-KIEA01XX - Einfuehrung und Anwendung der Kuenstlichen Intelligenz/
├── 📄 README.md                                                # Diese Datei
├── 📄 main.tex                                                 # LaTeX-Hauptdokument
│
├── 📁 B-KIEA01XX/                                              # Python-Simulation
│   ├── 📄 agent.py                                             # Agentenmodell (Standard, Express)
│   ├── 📄 astar.py                                             # A*-Algorithmus mit Heuristik-Dispatcher
│   ├── 📄 config.py                                            # Zentrale Konfiguration (Single Source of Truth)
│   ├── 📄 depot.py                                             # Depot-Klasse (Contract-Net-Manager)
│   ├── 📄 experiment.py                                        # Experiment-Runner (15 Läufe, Auswertung)
│   ├── 📄 geometry.py                                          # Manhattan-Distanz-Utility
│   ├── 📄 graph.py                                             # Gewichteter Graph mit Engpass-Cache
│   ├── 📄 gui.py                                               # Tkinter-GUI
│   ├── 📄 main.py                                              # Orchestrator (interaktive Simulation)
│   ├── 📄 map.py                                               # Kartenmodell mit BFS-Validierung
│   ├── 📄 message.py                                           # Nachrichten-Klasse
│   ├── 📄 package.py                                           # Paketmodell mit Lebenszyklus
│   ├── 📄 prolog.py                                            # Fakten-Export und PROLOG-Abfragen
│   ├── 📄 query.py                                             # subprocess-Brücke zu SWI-Prolog
│   ├── 📄 simulation.py                                        # Hauptschleife und Metriken
│   ├── 📄 rules.pl                                             # Hand-gepflegte PROLOG-Regeln
│   ├── 📄 facts.pl                                             # Generierte PROLOG-Fakten (Karte)
│   ├── 📄 agents.pl                                            # Generierte PROLOG-Fakten (Agenten)
│   │
│   └── 📁 asset/
│       ├── 📁 gif/                                             # Demonstrations-GIFs
│       │   ├── 🎞️ main.gif
│       │   └── 🎞️ experiment.gif
│       │
│       ├── 📁 image/                                           # Alle Plots aus Aufgabe 5
│       │   ├── 🖼️ 5A-Lieferzeit.png
│       │   ├── 🖼️ 5A-Erfolgsquote.png
│       │   ├── 🖼️ 5A-Pfadlaenge.png
│       │   ├── 🖼️ 5B-ExpandedHistogram.png
│       │   ├── 🖼️ 5B-ExpandedBoxplot.png
│       │   ├── 🖼️ 5B-TimeHistogram.png
│       │   ├── 🖼️ 5B-TimeBoxplot.png
│       │   ├── 🖼️ 5B-TimeMax.png
│       │   ├── 🖼️ 5C-MsgHistogram.png
│       │   ├── 🖼️ 5C-BidHistogram.png
│       │   ├── 🖼️ 5C-MsgBar.png
│       │   ├── 🖼️ 5C-BidBar.png
│       │   ├── 🖼️ 5D-Collisions.png
│       │   ├── 🖼️ 5D-Replans.png
│       │   └── 🖼️ 5D-Combined.png
│       │
│       └── 📁 results/                                         # Alle CSV-Ergebnisse
│           ├── 📊 5A-Results.csv
│           ├── 📊 5B-Results.csv
│           ├── 📊 5C-Results.csv
│           └── 📊 5D-Results.csv
│
├── 📁 asset/                                                   # LaTeX-Assets
│   ├── 📁 code/                                                # Alle Code-Listings (als .tex)
│   │   ├── 📝 Einleitung.tex ... EinleitungIX.tex
│   │   ├── 📝 1A-config.py, 1A-gui.py, 1A-main.py, 1A-map.py
│   │   ├── 📝 1B-agent.py, 1B-config.py, 1B-gui.py, ...
│   │   ├── 📝 1C-agent.py, 1C-config.py, 1C-message.py, ...
│   │   ├── 📝 2A-depot.py, 2A-simulation.py, ...
│   │   ├── 📝 3A-graph.py, 3B-astar.py, 3C-agent.py, 3D-astar.py
│   │   ├── 📝 4A-prolog.py, 4A-rules.pl, 4B-rules.pl, 4C-query.py, ...
│   │   ├── 📝 5A-experiment.py ... 5D-simulation.py
│   │   └── 📝 *-terminal.tex (Konsolenausgaben)
│   │
│   └── 📁 image/                                               # LaTeX-Grafiken
│       ├── 🖼️ 1A-GUI.png
│       ├── 🖼️ 1B-GUI.png
│       ├── 🖼️ 1C-GUI.png
│       ├── 🖼️ 1C-GUI-II.png
│       └── 🖼️ WBH.png
│
├── 📁 chapter/                                                 # LaTeX-Kapitel
│   ├── 📝 Einleitung.tex
│   ├── 📝 Aufgabe1.tex
│   ├── 📝 Aufgabe2.tex
│   ├── 📝 Aufgabe3.tex
│   ├── 📝 Aufgabe4.tex
│   ├── 📝 Aufgabe5.tex
│   └── 📝 Schlusswort.tex
│
└── 📁 config/                                                  # LaTeX-Konfiguration
    ├── 📝 acronym.tex                                          # Abkürzungsverzeichnis
    ├── 📝 bibliography.bib                                     # Literaturverzeichnis
    ├── 📝 settings.tex                                         # Dokument-Einstellungen
    └── 📝 titlepage.tex                                        # Titelseite
```

### 📁 Struktur-Legende
```text
📓 B-KIEA01XX - Einfuehrung und Anwendung der Kuenstlichen Intelligenz/
├── 📄 README.md              # Projektbeschreibung (diese Datei)
├── 📄 main.tex               # LaTeX-Hauptdokument
├── 📁 B-KIEA01XX/            # Python-Simulation (Quellcode + generierte Artefakte)
│   └── 📁 asset/
│       ├── 📁 gif/           # Demonstrations-GIFs
│       ├── 📁 image/         # Plots aus Aufgabe 5 (5A–5D)
│       └── 📁 results/       # CSV-Ergebnisse aus Aufgabe 5
├── 📁 asset/                 # LaTeX-Assets
│   ├── 📁 code/              # Code-Listings (*.tex) für die Doku
│   └── 📁 image/             # LaTeX-Grafiken (GUI-Screenshots, WBH-Logo)
├── 📁 chapter/               # LaTeX-Kapitel (Einleitung + Aufgabe 1–5)
└── 📁 config/                # LaTeX-Konfiguration (Settings, Bibliography, Titelseite)
```

---

## ⚡ QUICK START

### 🔧 Voraussetzungen
- **Python 3.10** (empfohlen über Miniforge / conda-forge)
- **SWI-Prolog 9.x** (für Aufgabe 4 – installierbar via `winget install SWI-Prolog.SWI-Prolog`)
- **Git** (optional, für Versionskontrolle)
- **LaTeX-Distribution** (z. B. TeXLive oder MiKTeX) – für die PDF-Erstellung

### 📦 Git & GitHub
```bash
# Repository klonen
git clone https://github.com/mucahid-emin-tomakin/AcademicPortfolio.git
cd AcademicPortfolio

# Ins Projektverzeichnis wechseln
cd "Bachelor - Kuenstliche Intelligenz und Maschinelles Lernen/B-KIEA01XX - Einfuehrung und Anwendung der Kuenstlichen Intelligenz"
```

### 🐍 Conda-Umgebung einrichten (isolierte Umgebung)
```bash
# Umgebung erstellen (Name: B-KIEA01XX, Python 3.10)
conda create -n B-KIEA01XX python=3.10

# Umgebung aktivieren
conda activate B-KIEA01XX

# Benötigte Pakete installieren
conda install matplotlib seaborn numpy pandas jupyter
```

### 🧠 SWI-Prolog installieren (für Aufgabe 4)
```powershell
# Windows (winget)
winget install SWI-Prolog.SWI-Prolog

# macOS
brew install swi-prolog

# Linux (Debian/Ubuntu)
sudo apt install swi-prolog

# PATH prüfen
swipl --version
```

### 🎮 Interaktive Simulation starten (mit GUI)
```bash
cd B-KIEA01XX
python main.py
```
- Ein randloses Tkinter-Fenster öffnet sich mit der Karte, den Agenten und der Info-Zeile.
- **Step**-Button: Führt einen Simulationsschritt aus.
- **AutoRun**-Button: Startet die Endlosschleife (100 ms Delay).
- **Stop**-Button: Stoppt den AutoRun-Modus.
- **Escape**-Taste: Beendet die Anwendung.

### 📊 Experimente ausführen (Aufgabe 5)
```bash
cd B-KIEA01XX
python experiment.py
```
Dies führt 15 Simulationsläufe (3 Konfigurationen × 5 Runs × 200 Steps) aus und erzeugt:
- `B-KIEA01XX/asset/results/5A-Results.csv` … `5D-Results.csv`
- `B-KIEA01XX/asset/image/5A-*.png` … `5D-*.png`

### 🔍 PROLOG-Wissensbasis isoliert testen (Aufgabe 4)
```bash
cd B-KIEA01XX
swipl
?- consult("rules.pl").
?- bottleneck(0, 0).
true.
?- vertex((1, 0), (0, 0), C).
C = 1.5.
```

### 📝 LaTeX-Kompilierung

**Option A: Lokal mit LaTeX**
```bash
latexmk -pdf main.tex
```

**Option B: Docker (empfohlen, keine lokale LaTeX-Installation nötig)**
```bash
docker run --rm -v "${PWD}:/work" -w /work texlive/texlive latexmk -pdf main.tex
```

**Option C: Online mit Papeeria**
```bash
# 1. Gehe auf https://m.papeeria.com
# 2. Erstelle ein neues Projekt und importiere den gesamten Ordner als ZIP
# 3. Papeeria kompiliert main.tex automatisch in der Cloud
```

---

## ⚠️ WICHTIGE HINWEISE

- 🔒 **Keine großen Binärdateien** – die generierten PROLOG-Dateien (`facts.pl`, `agents.pl`) werden bei jedem Start neu geschrieben und können bei Bedarf aus dem Repository ausgeschlossen werden.
- 🎓 **Eigenständigkeit** – alle Algorithmen (A\*, BFS-Heuristik, Contract-Net-Protokoll, Zustandsautomat), die PROLOG-Regeln und die Auswertung wurden eigenständig implementiert und reflektiert.
- 🤖 **KI-Transparenz** – gemäß den WBH-Vorgaben wird der Einsatz von Coding-Assistenten in Abschnitt 5e der Dokumentation („Reflexion des KI-Einsatzes") vollständig offengelegt.
- 📚 **Quellenangaben** – alle zitierten Aussagen sind mit den fünf Studienheften [KII00, KII04A, KII11, KII12, KIIBU] hinterlegt.
- 🧪 **Reproduzierbarkeit** – alle Zufallszahlen sind durch Seeds fixiert (`TomaKing1A_Seed = 42`), sodass die Ergebnisse deterministisch reproduzierbar sind.
- 🌍 **Plattformunabhängigkeit** – entwickelt unter Windows 11 (22H2), die verwendeten Tools sind jedoch plattformunabhängig.
- 📌 **Pfadangaben** – die PROLOG-Brücke nutzt `pathlib.Path(__file__).resolve().parent`, sodass die Simulation unabhängig vom aktuellen Arbeitsverzeichnis gestartet werden kann.
- ⚙️ **PROLOG-Fallback** – bei fehlender SWI-Prolog-Installation weicht die Simulation automatisch auf Python-Logik zurück (`[PROLOG] Fallback auf Python-Logik`).
- 🎞️ **GIF-Größe** – `main.gif` ist ca. 53 MB groß (Empfehlung von GitHub: < 50 MB). Bei langsamer Verbindung kann der `git clone` länger dauern; alternativ kann das GIF lokal komprimiert werden.

---

## 📝 LIZENZ

Dieses Projekt ist unter der **MIT License** lizenziert – frei für persönliche und kommerzielle Nutzung.

---

## 👤 AUTOR

**Mücahid Emin Tomakin (TomaKing)**

| Platform | Link | Icon |
|----------|------|------|
| **GitHub** | [@mucahid-emin-tomakin](https://github.com/mucahid-emin-tomakin) | 🐙 |
| **Studium** | B.Sc. Künstliche Intelligenz & Maschinelles Lernen | 🎓 |

**Über dieses Repository:**
- 📘 Typ: Einsendeaufgabe / Fachdokumentation
- 🎯 Ziel: Implementierung eines Multiagenten-Logistik-Simulationsspiels mit A\*, Contract-Net und PROLOG
- 🛠️ Werkzeuge: Python, Tkinter, SWI-Prolog, matplotlib, LaTeX, Git

---

## 📊 REPOSITORY STATISTIK

| Metrik | Wert | Trend |
|--------|------|-------|
| **Stars** | ![GitHub Stars](https://img.shields.io/github/stars/mucahid-emin-tomakin/AcademicPortfolio) | 📈 |
| **Forks** | ![GitHub Forks](https://img.shields.io/github/forks/mucahid-emin-tomakin/AcademicPortfolio) | 🔄 |
| **Issues** | ![GitHub Issues](https://img.shields.io/github/issues/mucahid-emin-tomakin/AcademicPortfolio) | ✅ |
| **Letztes Update** | ![GitHub Last Commit](https://img.shields.io/github/last-commit/mucahid-emin-tomakin/AcademicPortfolio) | 🕐 |

---

### 🔧 Made with ❤️ on LaTeX, Python, Tkinter, and SWI-Prolog
