# 📘 B-DVIT03XX – Datenvisualisierung und -tools

![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?logo=r&logoColor=white)
![RStudio](https://img.shields.io/badge/RStudio-75AADB?logo=rstudio&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-Abgeschlossen-brightgreen)

---

## 📖 INHALTSVERZEICHNIS

- [📝 PROJEKTBESCHREIBUNG](#-projektbeschreibung)
- [✨ FEATURES](#-features)
- [🚀 TOOLS](#-tools)
- [📁 STRUKTUR](#-struktur)
- [⚡ QUICK START](#-quick-start)
- [⚠️ WICHTIGE HINWEISE](#️-wichtige-hinweise)
- [📝 LIZENZ](#-lizenz)
- [👤 AUTOR](#-autor)
- [📊 REPOSITORY STATISTIK](#-repository-statistik)

---

## 📝 PROJEKTBESCHREIBUNG

Diese Einsendeaufgabe befasst sich mit der **Konzeption und praktischen Umsetzung von Datenvisualisierungen** – basierend auf den Studieninhalten der Module **BUSIH02-H** (Datenvisualisierung), **DVIT01** (Datenvisualisierung und Storytelling) und **DVIT02** (Datenvisualisierung mit R) der Wilhelm Büchner Hochschule.

Die Arbeit gliedert sich in **drei Hauptaufgaben** mit insgesamt **zwölf Teilaufgaben**, die von der theoretischen Einordnung von Datenvisualisierungen über ethische Aspekte bis hin zur praktischen Umsetzung einer Datengeschichte mit R reichen.

---

### 📌 Aufgabe 1: Visualisierungskonzept für medizinische Sensordaten

**1a – Mehrwert der Datenvisualisierung im medizinischen Setting**
- Transformation von Rohdaten in handlungsleitende Informationen [2, S. 5]
- Reduktion der kognitiven Belastung durch grafische Mustererkennung [2, S. 113]
- Unterstützung der explorativen Datenanalyse zur Mustererkennung [2, S. 7]
- Kommunikationsinstrument für patientenseitige Wissensvermittlung [2, S. 8]

**1b – Bestimmung der E-Notation und Attributzuordnung**
- Klassifikation des Datensatzes als punktförmiges Datenvorkommen (Brodlie-Taxonomie) [1, S. 33, 36]
- Notation: \(E_6^P(q + n)\) mit sechs Attributen [1, S. 61, 63]
- Zuordnung der Attribute zu quantitativen (\(q\)) und nominalen (\(n\)) Skalenniveaus [1, S. 33, 39]

**1c – Prozessschritte von der Datenvorbereitung bis zur Visualisierung**
- Bereinigung: Filterung von Messfehlern und Rauschen [1, S. 11]
- Selektion: Horizontale und vertikale Filterung der Daten [1, S. 12]
- Normalisierung: Überführung in ein einheitliches Format [1, S. 12]
- Kodierung: Ordinal-numerische Kodierung nominaler Daten [1, S. 12–13]
- Mapping: Zuordnung zu visuellen Merkmalen [1, S. 31, 35]

**1d – Auswahl und Begründung der Visualisierungstypen**
- Streudiagramm-Matrix für ärztliche Exploration [1, S. 39]
- Liniendiagramm für patientenseitige Kommunikation [1, S. 63]

**1e – Risiken und Gegenmaßnahmen**
- Manipulative Achsenskalierung (Non-Zero Baseline) [1, S. 50; 2, S. 31, 43]
- Verzerrung durch Dreidimensionalität [2, S. 54, 58]
- Gegenmaßnahmen: 2D-Darstellung, Null-Basislinie [1, S. 50; 2, S. 44]

---

### 📌 Aufgabe 2: Ethische und gestalterische Aspekte der Datenvisualisierung

**2a – Typische Fehler und Manipulationen**
- Abgeschnittene \(y\)-Achse: optische Dramatisierung von Trends [1, S. 50–51; 2, S. 55]
- 3D-Effekte: perspektivische Verzerrung und erschwerte Vergleichbarkeit [2, S. 54, 58]
- Selektive Datendarstellung (Cherry Picking): unterschlagene Kontextinformationen [2, S. 71]

**2b – Maßnahmen für korrektes und ethisches Design**
- Transparenz durch korrekte Datenzitation [2, S. 11, 40]
- Verzicht auf manipulative Gestaltungselemente [2, S. 39, 44]
- Förderung der Barrierefreiheit und inklusiven Gestaltung [2, S. 37, 40]

**2c – Analyse eines 3D-Balkendiagramms**
- Rolle von Farben und präattentiven Merkmalen [1, S. 48–49; 2, S. 16, 31, 52]
- Verzerrung durch Dreidimensionalität und Non-Zero Baseline [1, S. 50; 2, S. 54, 58]
- Maßnahmen: 2D-Darstellung und Null-Basislinie [1, S. 50; 2, S. 55]

---

### 📌 Aufgabe 3: Praktische Umsetzung einer Datengeschichte mit R

**3a – Erstellung des data.frames**
- Erstellung eines `data.frame` mit Ländernamen, CO₂-Ausstoß, erneuerbaren Energien und BIP [3, S. 14–15, 60]
- Verwendung des Punkts als Dezimaltrennzeichen [3, S. 46]

**3b – Visualisierung der erneuerbaren Energien**
- Balkendiagramm mit `ggplot2` zur Darstellung der Ländervergleiche [3, S. 35]

**3c – Scatterplot: CO₂-Ausstoß vs. erneuerbare Energien**
- Untersuchung des negativen Zusammenhangs zwischen CO₂-Ausstoß und erneuerbaren Energien [2, S. 29, 53]
- Visualisierung mit Regressionslinie in `ggplot2` [2, S. 31]

**3d – Mini-Story für ein Laienpublikum**
- Zusammenfassung der Analyseergebnisse in einer verständlichen Erzählung [2, S. 44–46, 65, 67]

**3e – Export als RMarkdown-Report**
- Erstellung eines reproduzierbaren Berichts mit `RMarkdown` [3, S. 55–59]

---

### 📚 Quellen

- [1] Buchholz, Detlev: *Datenvisualisierung*. Wilhelm Büchner Hochschule, Darmstadt 2025 (Studienheft BUSIH02-H, Druck-Code 1225A04).
- [2] Dürkopp, Alexander: *Datenvisualisierung und Storytelling*. Wilhelm Büchner Hochschule, Darmstadt 2025 (Studienheft DVIT01, Druck-Code 0725N01).
- [3] Dürkopp, Alexander: *Datenvisualisierung mit R*. Wilhelm Büchner Hochschule, Darmstadt 2025 (Studienheft DVIT02, Druck-Code 0725N01).

---

## ✨ FEATURES

| Feature | Beschreibung |
|---------|-------------|
| 📊 **E-Notation** | Klassifikation von Daten nach Brodlie-Taxonomie |
| 🧠 **Kognitive Aspekte** | Ikonisches Gedächtnis, präattentive Merkmale, Gestaltprinzipien |
| ⚖️ **Ethische Gestaltung** | Transparenz, Barrierefreiheit, Verzicht auf Manipulation |
| 🎨 **Visualisierungstypen** | Streudiagramm-Matrix, Liniendiagramm, Balkendiagramm, Scatterplot |
| 💻 **R-Programmierung** | `data.frame`, `ggplot2`, `RMarkdown` |
| 📖 **Storytelling** | Datengetriebene Geschichte für Laienpublikum |
| 🐧 **Reproduzierbarkeit** | Vollständiger R-Code und LaTeX-Dokumentation |
| 🔗 **Versionskontrolle** | Git & GitHub für Nachvollziehbarkeit |

---

## 🚀 TOOLS

| Bereich | Werkzeug |
|---------|----------|
| **Dokumentation** | LaTeX (kompiliert mit texlive / Papeeria) |
| **Datenanalyse & Visualisierung** | R 4.6.1, RStudio, tidyverse, ggplot2, plotly, rmarkdown |
| **Versionskontrolle** | Git & GitHub |
| **Betriebssystem** | Windows 11 (22H2) |

---

## 📁 STRUKTUR

```text
📓 B-DVIT03XX - Datenvisualisierung und -tools/
├── 📄 README.md                                       # Diese Datei
├── 📄 main.tex                                        # LaTeX‑Hauptdokument
│
├── 📁 asset/
│   ├── 📁 code/                                       # R-Code-Dateien
│   │   ├── 📝 Aufgabe3a.tex
│   │   ├── 📝 Aufgabe3aII.tex
│   │   ├── 📝 Aufgabe3b.tex
│   │   ├── 📝 Aufgabe3c.tex
│   │   └── 📝 Aufgabe3e.tex
│   └── 📁 image/                                       # Bilder & Diagramme
│       ├── 🖼️ WBH.png                                 # WBH‑Logo
│       ├── 🖼️ Aufgabe3b.png                           # Balkendiagramm
│       └── 🖼️ Aufgabe3c.png                           # Scatterplot
│
├── 📁 chapter/                                        # LaTeX‑Kapitel
│   ├── 📝 Einleitung.tex
│   ├── 📝 Aufgabe1.tex
│   ├── 📝 Aufgabe2.tex
│   ├── 📝 Aufgabe3.tex
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
📓 B-DVIT03XX - Datenvisualisierung und -tools/
├── 📄 README.md              # Projektbeschreibung (diese Datei)
├── 📄 main.tex               # LaTeX‑Hauptdokument
├── 📁 asset/                 # Code & Bilder
├── 📁 chapter/               # LaTeX‑Kapitel
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
cd "Bachelor - Kuenstliche Intelligenz und Maschinelles Lernen/B-DVIT03XX - Datenvisualisierung und -tools"
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

### 💻 R-Code ausführen
```bash
# R starten (in RStudio oder Konsole)
R

# Pakete installieren (einmalig)
install.packages(c("tidyverse", "ggplot2", "plotly", "rmarkdown"))

# Arbeitsverzeichnis setzen (falls nötig)
setwd("C:/Users/.../B-DVIT03XX")

# Code aus den asset/code/ Dateien ausführen
source("asset/code/main.tex")  # data.frame erstellen
```

---

# ⚠️ WICHTIGE HINWEISE

- 🎓 **Eigenständigkeit** – alle Lösungen und die LaTeX‑Dokumentation sind eigenständig verfasst.
- 📚 **Quellenangaben** – alle zitierten Aussagen sind mit den Studienheften BUSIH02-H [1], DVIT01 [2] und DVIT02 [3] hinterlegt.
- 🧪 **Reproduzierbarkeit** – das gesamte Dokument muss aus den LaTeX‑Quellen kompilierbar sein.
- 💻 **R-Code** – alle R-Code-Dateien sind lauffähig und in der Asset-Struktur enthalten.
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
- 🎯 Ziel: Lösung der B‑Prüfung B‑DVIT03XX – Datenvisualisierung und -tools
- 🛠️ Werkzeuge: LaTeX, R, RStudio, Git

---

## 📊 REPOSITORY STATISTIK

| Metrik | Wert | Trend |
|--------|------|-------|
| **Stars** | ![GitHub Stars](https://img.shields.io/github/stars/mucahid-emin-tomakin/AcademicPortfolio) | 📈 |
| **Forks** | ![GitHub Forks](https://img.shields.io/github/forks/mucahid-emin-tomakin/AcademicPortfolio) | 🔄 |
| **Issues** | ![GitHub Issues](https://img.shields.io/github/issues/mucahid-emin-tomakin/AcademicPortfolio) | ✅ |
| **Letztes Update** | ![GitHub Last Commit](https://img.shields.io/github/last-commit/mucahid-emin-tomakin/AcademicPortfolio) | 🕐 |

---

### 🔧 Made with ❤️ on LaTeX & R
