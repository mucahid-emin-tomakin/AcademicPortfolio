# 📄 LaTeX‑Template

![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)
![Template](https://img.shields.io/badge/Template-Wiederverwendbar-blue)
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

Dieser Ordner enthält die **zentralen LaTeX-Vorlagen**, die in sämtlichen Projekten und Einsendeaufgaben meines AcademicPortfolios zum Einsatz kommen.  
Ziel ist es, ein einheitliches, professionelles Erscheinungsbild aller Dokumente zu gewährleisten und gleichzeitig den Aufwand für wiederkehrende Einstellungen zu minimieren.

Das Template liegt in **zwei Varianten** vor:

- **Documented** – Eine ausführlich kommentierte Fassung, die als Lern- und Referenzvorlage dient. Jede Datei enthält detaillierte Erklärungen zu den verwendeten LaTeX-Befehlen und Einstellungen.

- **Production** – Eine schlanke, produktionsreife Fassung ohne Kommentare, die direkt in neue Projekte kopiert werden kann.

Beide Varianten sind identisch aufgebaut und enthalten neben der Hauptdatei `main.tex` jeweils:
- Ein **Deckblatt** mit studiengangsbezogenen Formalien
- Ein **Abkürzungsverzeichnis**, das projektspezifisch ergänzt werden kann
- **Globale Dokument-Einstellungen** (Schriftart, Seitenränder, PDF-Metadaten …)
- Ein **BibTeX-Literaturverzeichnis**, das als Grundstock für wissenschaftliche Arbeiten dient
- **Prompt-Vorlagen** (`promts.tex`) mit standardisierten Arbeitsanweisungen
- Ein **Kapitel-Template** (`chapter/template.tex`) als Vorlage für neue Inhaltskapitel
- **Asset-Ordner** (`asset/code/`, `asset/image/`) für Quellcode-Listings und Abbildungen

---

## ✨ FEATURES

| Feature | Beschreibung |
|---------|-------------|
| 📝 Documented-Variante | Ausführlich kommentierte Lernvorlage mit Erklärungen zu allen LaTeX-Befehlen |
| 🚀 Production-Variante | Schlanke, produktionsreife Vorlage zum direkten Kopieren in neue Projekte |
| 📄 Deckblatt | Einheitliches Titelblatt mit Matrikelnummer, Studiengang, Abgabedatum etc. |
| 📝 Abkürzungsverzeichnis | Automatisch sortiertes Akronym-Verzeichnis mit `glossaries` |
| ⚙️ Dokument-Einstellungen | Zentrale Konfiguration (Schriftart, Seitenlayout, PDF-Metadaten) |
| 📚 BibTeX-Literaturverzeichnis | Vorbereitete `.bib`-Datei für wissenschaftliche Quellen |
| 🤖 Prompt-Vorlagen | Standardisierte Arbeitsanweisungen für KI-gestütztes Arbeiten |
| 📖 Kapitel-Template | Vorbereitete Kapiteldatei als Ausgangspunkt für neue Inhalte |
| 📁 Asset-Struktur | Vordefinierte Ordner für Code (`asset/code/`) und Bilder (`asset/image/`) |
| 🔄 Wiederverwendbarkeit | Alle Dateien können in neue Projekte übernommen werden |
| ☁️ Papeeria-kompatibel | Funktioniert sowohl lokal als auch in der Cloud |

---

## 🚀 TOOL

| Bereich | Werkzeug |
|---------|----------|
| Dokumentation | LaTeX (erstellt mit Papeeria / lokalem TeXLive) |
| Versionskontrolle | Git & GitHub |

---

## 📁 STRUKTUR

```text
📓 LaTeX-Template/
├── 📁 Documented/                    # Ausführlich kommentierte Lernvorlage
│   ├── 📄 main.tex                    # Hauptdatei
│   ├── 📁 chapter/
│   │   └── 📝 template.tex            # Kapitel-Vorlage
│   ├── 📁 config/
│   │   ├── 📝 acronym.tex             # Abkürzungsverzeichnis
│   │   ├── 📝 bibliography.bib        # BibTeX-Literaturverzeichnis
│   │   ├── 📝 promts.tex              # Prompt-Vorlagen (Arbeitsanweisungen)
│   │   ├── ⚙️ settings.tex            # Dokument-Einstellungen
│   │   └── 📝 titlepage.tex           # Deckblatt
│   └── 📁 asset/
│       ├── 📁 code/                   # Quellcode-Listings
│       └── 📁 image/                  # Abbildungen
│
├── 📁 Production/                     # Schlanke, produktionsreife Vorlage
│   ├── 📄 main.tex                    # Hauptdatei
│   ├── 📁 chapter/
│   │   └── 📝 template.tex            # Kapitel-Vorlage
│   ├── 📁 config/
│   │   ├── 📝 acronym.tex             # Abkürzungsverzeichnis
│   │   ├── 📝 bibliography.bib        # BibTeX-Literaturverzeichnis
│   │   ├── 📝 promts.tex              # Prompt-Vorlagen (Arbeitsanweisungen)
│   │   ├── ⚙️ settings.tex            # Dokument-Einstellungen
│   │   └── 📝 titlepage.tex           # Deckblatt
│   └── 📁 asset/
│       ├── 📁 code/                   # Quellcode-Listings
│       └── 📁 image/                  # Abbildungen
│
└── 📄 README.md                       # Diese Datei
```

### 📁 Struktur-Legende
```text
📓 LaTeX-Template/
├── 📁 Documented/                     # Ausführlich kommentierte Lernvorlage
│   ├── 📄 main.tex                    # Hauptdatei – Einstiegspunkt, bindet config und chapter ein
│   ├── 📁 chapter/                    # Inhaltskapitel
│   │   └── 📝 template.tex            # Kapitel-Vorlage – kann kopiert und befüllt werden
│   ├── 📁 config/                     # Zentrale Konfigurationsdateien
│   │   ├── 📝 acronym.tex             # Abkürzungsverzeichnis (glossaries, alphabetisch sortiert)
│   │   ├── 📝 bibliography.bib        # BibTeX-Datenbank für Literaturquellen
│   │   ├── 📝 promts.tex              # Prompt-Vorlagen – standardisierte Arbeitsanweisungen
│   │   ├── ⚙️ settings.tex            # Globale Einstellungen (Schriftart, Seitenlayout, PDF-Metadaten)
│   │   └── 📝 titlepage.tex           # Deckblatt – Titel, Autor, Matrikelnummer, Studiengang etc.
│   └── 📁 asset/                      # Statische Ressourcen
│       ├── 📁 code/                   # Platz für Quellcode-Dateien (Listings)
│       └── 📁 image/                  # Platz für Abbildungen
│
├── 📁 Production/                     # Schlanke, produktionsreife Vorlage (gleicher Aufbau wie Documented)
│   └── ... (identische Unterstruktur)
│
└── 📄 README.md                       # Diese Datei – Beschreibung und Nutzungshinweise
```

---

## ⚡ QUICK START

### 📦 Git & GitHub
```bash
# Repository klonen
git clone https://github.com/mucahid-emin-tomakin/AcademicPortfolio.git
cd AcademicPortfolio

# In den Template-Ordner wechseln
cd LaTeX-Template
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

### 📝 Mit einem neuen Projekt starten (Production-Variante)
```bash
# Production-Vorlage in ein neues Projekt kopieren
cp -r LaTeX-Template/Production "Bachelor - Kuenstliche Intelligenz und Maschinelles Lernen/NEUES_PROJEKT"
cd "Bachelor - Kuenstliche Intelligenz und Maschinelles Lernen/NEUES_PROJEKT"

# Titlepage.tex anpassen (Deckblatt)
# → config/titlepage.tex öffnen und Name, Titel etc. eintragen

# Kapitel befüllen (template.tex kopieren und umbenennen)
cp chapter/template.tex chapter/1.tex

# Dokument kompilieren
pdflatex main.tex && pdflatex main.tex
# oder automatisch
latexmk -pdf main.tex
```

### 📖 Documented-Variante studieren
```bash
# Zum Lernen und Nachschlagen die kommentierte Fassung öffnen
cd LaTeX-Template/Documented
cat config/settings.tex    # Erklärungen zu den Einstellungen lesen
cat config/titlepage.tex   # Deckblatt-Aufbau nachvollziehen
```

---

## ⚠️ WICHTIGE HINWEISE

- 🔧 Documented vs. Production – Die Documented-Variante enthält ausführliche Kommentare und dient als Lernreferenz. Für neue Projekte sollte die schlanke Production-Variante kopiert werden.
- 🎓 Anpassbarkeit – Deckblatt (titlepage.tex), Abkürzungen (acronym.tex) und Prompts (promts.tex) müssen projektspezifisch angepasst werden.
- 📚 Quellenpflege – Die bibliography.bib kann zentral gepflegt und in allen Projekten referenziert werden.
- 🧪 Konsistenz – Alle Projekte des AcademicPortfolios profitieren von einem einheitlichen Erscheinungsbild.

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
- 📘 Typ: Zentrale Dokument-Vorlagen
- 🎯 Ziel: Wiederverwendbare LaTeX-Bausteine für alle akademischen Arbeiten
- 🛠️ Werkzeuge: LaTeX (Papeeria), Git

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
