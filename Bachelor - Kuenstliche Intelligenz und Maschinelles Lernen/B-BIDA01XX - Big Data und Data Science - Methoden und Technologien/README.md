# 📊 B-BIDA01XX – Big Data und Data Science – Methoden und Technologien

![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.2.0-150458?logo=pandas&logoColor=white)
![scikit‑learn](https://img.shields.io/badge/scikit‑learn-1.4.0-F7931E?logo=scikit-learn&logoColor=white)
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

Diese Einsendeaufgabe befasst sich mit der **explorativen Datenanalyse, dem maschinellen Lernen und der Konzeption von Big‑Data‑Architekturen** – basierend auf den Studieninhalten der Module *Explorative Datenanalyse* (BID02), *Machine Learning* (BID03) und *Big Data Architektur* (BID04) der Wilhelm Büchner Hochschule.

Die Arbeit gliedert sich in drei Hauptaufgaben, die theoretische Konzepte mit praktischen Implementierungen verbinden:

**1. Explorative Analyse (Aufgabe 1)**
- Einlesen und Bereinigung des Datensatzes `movies2019.csv` (Filme, Distributoren, Genres, Umsätze).
- Konvertierung der Umsatzspalte von String in numerische Werte.
- Visualisierung der Genres mittels Count‑Plot und Barplots (Gesamtumsatz pro Genre / pro Monat).
- Summenstatistik nach Genre und Ermittlung der Top‑5‑Distributoren.
- Identifikation fehlender Informationen für eine vollständige Erfolgsbeurteilung (z. B. Produktionskosten, Marketingausgaben).

**2. Regression und Klassifikation (Aufgabe 2)**
- Verwendung des *California Housing*-Datensatzes (`sklearn.datasets`).
- Laden, Beschreibung und Konvertierung in Pandas‑DataFrame.
- Summenstatistik, Pairplot und Korrelationsanalyse (stärkste Korrelation: `MedInc` mit 0.688).
- Lineare Regression (ohne geografische Koordinaten) mit Train‑Test‑Split (MSE = 0.6422, R² = 0.5099).
- Entscheidungsbaum‑Regression mit manueller Hyperparameter‑Optimierung (beste Tiefe ≈ 7–8).
- Diskussion der Verfälschung durch Weglassen von *Latitude* und *Longitude* und methodische Ansätze zu deren Berücksichtigung (Polynomial‑Features, räumliche Regression, Interaktionsterme).

**3. Clusteranalyse (Aufgabe 3)**
- Einsatz des *Wine*-Datensatzes (`sklearn.datasets`).
- Analyse der Datentypen, Countplot der Zielvariable und Korrelationsplot.
- Kombination von Merkmalen und Zielvariable für einen Pairplot (erkennbare Cluster in der Spalte `proline`).
- Elbow‑Methode (unskaliert und skaliert mit `StandardScaler`) zur Bestimmung der Cluster‑Anzahl – beide liefern \(k = 3\).
- Visualisierung der K‑Means‑Clusterung mittels Hauptkomponentenanalyse (PCA).

Die gesamte Analyse wurde in **Python** mit **Jupyter Notebooks** durchgeführt und die Ergebnisse in einer **LaTeX‑Dokumentation** festgehalten. Die Arbeit umfasst etwa 80 Seiten (inkl. Abbildungs‑, Tabellen‑ und Code‑Verzeichnis) und ein Literaturverzeichnis mit drei zentralen Quellen (die Studienhefte der Module).

---

## ✨ FEATURES

| Feature | Beschreibung |
|---------|-------------|
| 🧹 Datenbereinigung | Konvertierung von String‑Umsätzen in numerische Werte mit eigener `apply()`‑Funktion |
| 📊 Explorative Visualisierung | Count‑Plots, Barplots, Pairplots, Korrelations‑Heatmaps |
| 🧮 Statistische Analyse | Summenstatistiken, Mittelwerte, Standardabweichungen, Korrelationskoeffizienten |
| 🤖 Lineare Regression | Train‑Test‑Split, MSE und R²‑Score (0.5099) mit `sklearn.linear_model` |
| 🌳 Entscheidungsbaum | Hyperparameter‑Optimierung (max_depth) und Overfitting‑Analyse |
| 🧩 Clustering | K‑Means, Elbow‑Methode, PCA‑Visualisierung, StandardScaler‑Vergleich |
| 🐍 Reproduzierbarer Code | Vollständige Jupyter‑Notebooks mit allen Zwischenschritten |
| 📄 LaTeX‑Dokumentation | Professionelles wissenschaftliches Layout mit allen Code‑Listings und Abbildungen |
| 🔗 Versionskontrolle | Git & GitHub für Nachvollziehbarkeit und Zusammenarbeit |

---

## 🚀 TOOL

| Bereich | Werkzeug |
|---------|----------|
| **Programmiersprache** | Python 3.12 |
| **Interaktive Entwicklung** | Jupyter Notebook |
| **Data Science‑Bibliotheken** | pandas, numpy, matplotlib, seaborn, scikit‑learn, statsmodels, scipy, missingno |
| **Paketmanagement** | Miniforge mit conda‑forge‑Kanal |
| **Dokumentation** | LaTeX (kompiliert mit Papeeria / lokalem TeXLive) |
| **Visualisierungen** | Seaborn, Matplotlib, Pairplots, Heatmaps |
| **Versionskontrolle** | Git & GitHub |

---

## 📁 STRUKTUR

```text
📓 B-BIDA01XX - Big Data und Data Science - Methoden und Technologien/
├── 📄 README.md                                              # Diese Datei
├── 📄 main.tex                                                # LaTeX‑Hauptdokument
│
├── 📁 asset/
│   ├── 📁 code/                                                # Alle Code‑Listings (als .tex)
│   │   ├── 📝 Aufgabe1a.tex
│   │   ├── 📝 Aufgabe1b.tex
│   │   ├── 📝 Aufgabe1c.tex
│   │   ├── 📝 Aufgabe1d.tex
│   │   ├── 📝 Aufgabe1e.tex
│   │   ├── 📝 Aufgabe1f.tex
│   │   ├── 📝 Aufgabe1g.tex
│   │   ├── 📝 Aufgabe2a.tex
│   │   ├── 📝 Aufgabe2b.tex
│   │   ├── 📝 Aufgabe2c.tex
│   │   ├── 📝 Aufgabe2d.tex
│   │   ├── 📝 Aufgabe2e.tex
│   │   ├── 📝 Aufgabe2f.tex
│   │   ├── 📝 Aufgabe2g.tex
│   │   ├── 📝 Aufgabe2h.tex
│   │   ├── 📝 Aufgabe3a.tex
│   │   ├── 📝 Aufgabe3b.tex
│   │   ├── 📝 Aufgabe3c.tex
│   │   ├── 📝 Aufgabe3d.tex
│   │   ├── 📝 Aufgabe3e.tex
│   │   ├── 📝 Aufgabe3f.tex
│   │   ├── 📝 Aufgabe3g.tex
│   │   ├── 📝 Aufgabe3h.tex
│   │   ├── 📝 CondaForge.tex
│   │   ├── 📝 CondaForgeII.tex
│   │   ├── 📝 CondaForgeIII.tex
│   │   ├── 📝 CondaForgeIV.tex
│   │   ├── 📝 JupyterServers.tex
│   │   ├── 📝 Miniforge.tex
│   │   ├── 📝 PythonInstallation.tex
│   │   └── 📝 PythonInstallationII.tex
│   │
│   └── 📁 image/                                                # Alle Abbildungen (Screenshots, Plots)
│       ├── 🖼️ Aufgabe1b.png
│       ├── 🖼️ Aufgabe1e.png
│       ├── 🖼️ Aufgabe1f.png
│       ├── 🖼️ Aufgabe2d.png
│       ├── 🖼️ Aufgabe2e.png
│       ├── 🖼️ Aufgabe2g.png
│       ├── 🖼️ Aufgabe2h.png
│       ├── 🖼️ Aufgabe3b.png
│       ├── 🖼️ Aufgabe3d.png
│       ├── 🖼️ Aufgabe3e.png
│       ├── 🖼️ Aufgabe3f.png
│       ├── 🖼️ Aufgabe3g.png
│       ├── 🖼️ Aufgabe3h.png
│       ├── 🖼️ JupyterServers.png
│       ├── 🖼️ PythonInstallerPath.png
│       └── 🖼️ WBH.png
│
├── 📁 chapter/                                                 # LaTeX‑Kapitel
│   ├── 📝 Einleitung.tex
│   ├── 📝 Aufgabe1.tex
│   ├── 📝 Aufgabe2.tex
│   ├── 📝 Aufgabe3.tex
│   └── 📝 Zusammenfassung.tex
│
├── 📁 config/                                                   # Konfiguration & Einstellungen
│   ├── 📝 acronym.tex                                           # Abkürzungsverzeichnis
│   ├── 📝 bibliography.bib                                      # Literaturverzeichnis (3 Einträge)
│   ├── 📝 settings.tex                                          # Dokument‑Einstellungen
│   └── 📝 titlepage.tex                                         # Titelseite mit Matrikelnummer
│
├── 📁 data/                                                      # Die verwendeten Datensätze
│   ├── 📊 movies2019.csv
│   ├── 📊 california_housing.csv
│   └── 📊 wine.csv
│
├── 📁 notebooks/                                                 # Die Jupyter‑Notebooks
│   ├── 📓 Aufgabe_1_Explorative_Analyse.ipynb
│   ├── 📓 Aufgabe_2_Regression_Klassifikation.ipynb
│   └── 📓 Aufgabe_3_Clustering.ipynb
│
└── 📁 output/                                                    # Exportierte Grafiken & Zwischenergebnisse
```

### 📁 Struktur-Legende
```text
📓 B-BIDA01XX - Big Data und Data Science - Methoden und Technologien/
├── 📄 README.md              # Projektbeschreibung (diese Datei)
├── 📄 main.tex               # LaTeX‑Hauptdokument
├── 📁 asset/
│   ├── 📁 code/              # Alle Code‑Listings (als .tex) für LaTeX
│   └── 📁 image/             # Abbildungen (Screenshots, Plots)
├── 📁 chapter/               # LaTeX‑Kapitel (Einleitung, 3 Aufgaben, Zusammenfassung)
├── 📁 config/                # Einstellungen, Abkürzungen, Literatur, Titelseite
├── 📁 data/                  # Die CSV‑Datensätze
├── 📁 notebooks/             # Die Jupyter‑Notebooks (.ipynb)
└── 📁 output/                # Exportierte Grafiken und Zwischenergebnisse
```

---

## ⚡ QUICK START

### 🔧 Voraussetzungen
- **Python 3.12** (empfohlen über Miniforge / conda‑forge)
- **Git** (optional, für Versionskontrolle)
- **LaTeX‑Distribution** (z.B. TeXLive oder MiKTeX) – für die PDF‑Erstellung

### 📦 Git & GitHub
```bash
# Repository klonen
git clone https://github.com/mucahid-emin-tomakin/AcademicPortfolio.git
cd AcademicPortfolio

# Ins Projektverzeichnis wechseln
cd "Bachelor - Kuenstliche Intelligenz und Maschinelles Lernen/B-BIDA01XX - Big Data und Data Science - Methoden und Technologien"
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

### 🐍 Conda‑Umgebung einrichten (isolierte Umgebung)
```bash
# Umgebung erstellen (Name: B-BIDA01XX, Python 3.12)
conda create -n B-BIDA01XX python=3.12

# Umgebung aktivieren
conda activate B-BIDA01XX

# Data‑Science‑Bibliotheken installieren
conda install jupyter pandas numpy matplotlib seaborn scikit-learn

# Zusätzliche Pakete (optional)
conda install statsmodels scipy missingno
```

### 📓 Jupyter Notebooks starten
```bash
# In den Notebook-Ordner wechseln
cd notebooks

# Jupyter Server starten
jupyter notebook
```
- Das Dashboard öffnet sich im Browser unter `http://localhost:8888`.
- Öffne die gewünschten Notebooks im Ordner `notebooks/`.

### ⚙️ conda‑forge‑Kanal konfigurieren (optional)
```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
```

---

## ⚠️ WICHTIGE HINWEISE

- 🔒 Keine großen Binärdateien – die Datensätze (*.csv) sind enthalten, aber die Jupyter‑Notebooks sollten ohne externe Datenquellen ausführbar sein.
- 🎓 Eigenständigkeit – alle Analysen, Interpretationen und Reflexionen sind eigenständig verfasst und wissenschaftlich belegt.
- 📚 Quellenangaben – alle zitierten Aussagen sind mit den drei Studienheften [1–3] hinterlegt.
- 🧪 Reproduzierbarkeit – das gesamte Dokument muss aus den LaTeX‑Quellen kompilierbar sein; alle Notebooks sind im Ordner notebooks/ enthalten und lassen sich mit der angegebenen Conda‑Umgebung ausführen.
- 🌍 Plattformunabhängigkeit – die Arbeit wurde unter Windows 11 (22H2) entwickelt, die verwendeten Tools sind jedoch plattformunabhängig.
- 📌 Pfadangaben – in den Notebooks werden relative Pfade (../data/, ../output/) verwendet; beim Klonen ist keine Anpassung nötig.

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
- 🎯 Ziel: Praktische Umsetzung von explorativer Datenanalyse, Machine Learning und Big‑Data‑Konzepten
- 🛠️ Werkzeuge: Python, Jupyter, LaTeX, conda‑forge, Git

---

## 📊 REPOSITORY STATISTIK

| Metrik | Wert | Trend |
|--------|------|-------|
| **Stars** | ![GitHub Stars](https://img.shields.io/github/stars/mucahid-emin-tomakin/AcademicPortfolio) | 📈 |
| **Forks** | ![GitHub Forks](https://img.shields.io/github/forks/mucahid-emin-tomakin/AcademicPortfolio) | 🔄 |
| **Issues** | ![GitHub Issues](https://img.shields.io/github/issues/mucahid-emin-tomakin/AcademicPortfolio) | ✅ |
| **Letztes Update** | ![GitHub Last Commit](https://img.shields.io/github/last-commit/mucahid-emin-tomakin/AcademicPortfolio) | 🕐 |

---

### 🔧 Made with ❤️ on LaTeX, Python, and Jupyter
