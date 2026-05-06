# 📊 B-IBI02XX – Informationssysteme und Business Intelligence

![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)
![ERP](https://img.shields.io/badge/ERP-Systeme-blue)
![BI](https://img.shields.io/badge/Business_Intelligence-FF6B6B?logo=openai&logoColor=white)
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
| 🏭 Zukunftsfähige ERP-Systeme | Fünf Erfolgsfaktoren adaptiver ERP-Architekturen |
| 👥 Projektteam & Migration | Rollenkonzept und Zieldefinition für ERP-Migration |
| 🔗 ERP vs. SCM | Fünf Unterschiede und Gemeinsamkeiten der Systemklassen |
| ⭐ Star-Schema | Multidimensionales Datenmodell für Reseller-Analysen |
| ⛏️ Data-Mining-Prozess | Text-Mining und Sentimentanalyse von Internetquellen |
| 🧹 Stammdatenbereinigung | MDM-Konzept zur Zentralisierung von Kundendaten |
| 📈 Prozesskennzahlen | Fünf KPIs zur Messung der ERP-Wirkung |
| 📄 LaTeX-Satz | Wissenschaftliche Dokumentation mit 31 Quellen |

---

## 📝 PROJEKTBESCHREIBUNG

Diese Einsendeaufgabe behandelt zentrale Themen moderner betrieblicher Informationssysteme und Business Intelligence. Die fünf Aufgaben decken sowohl konzeptionelle als auch praktische Aspekte ab.

**1. ERP-Systeme, Migration & SCM**  
- Zukunftsfähige ERP-Systeme zeichnen sich durch Wandlungsfähigkeit, KI-Integration, rekonfigurierbare Prozesse, Interoperabilität und Cloud-Fähigkeit aus.  
- Für die innerbetriebliche Migration wird ein Projektteam mit Lenkungsausschuss, Gesamtprojektleiter, Key Usern und externen Dienstleistern entworfen; Ziele umfassen Durchlaufzeitverkürzung, RoI, Datenaktualität und Transparenz.  
- Fünf Unterschiede (Fokus, Planungsart, Aktualität, Geschwindigkeit, Zielsetzung) und Gemeinsamkeiten (Ressourcenmanagement, Modularität, Prozessintegration, Entscheidungsunterstützung, Transparenz) von ERP- und SCM-Systemen werden gegenübergestellt.

**2. Star-Schema für Reseller**  
- Entwurf eines multidimensionalen Datenmodells mit zentraler Faktentabelle (Umsatz, Menge, Deckungsbeitrag) und vier Dimensionstabellen: Zeit, Produkt, Mitarbeiter, Standort.  
- Ermöglicht Analysen wie „Welcher Umsatz wurde mit Elektronik am Standort Berlin durch Mitarbeiter X erzielt?“

**3. Data-Mining-Prozess anhand von Internettexten**  
- Vier-Phasen-Modell: Datenerfassung (Extraktion aus Foren/Blogs), Datenaufbereitung (Bereinigung von Slang/Sarkasmus), Mustererkennung (Sentimentanalyse, Clustering), Wissensgenerierung (Frühwarnung, Rückgewinnungsanalyse).  

**4. Stammdatenbereinigung & MDM**  
- Fünfstufiges Konzept: Data Profiling (Dublettenerkennung), Harmonisierung (einheitliche Formate), Cleansing & Merging (Golden Record), Architekturwahl (Transaction Hub), Data Governance (Data Stewards, Workflows).  

**5. ERP-gestützte Prozesse & Kennzahlen**  
- Übersicht der unterstützten Bereiche: Materialwirtschaft, Produktion, Vertrieb, Finanzen, Personal.  
- Fünf KPIs: Durchlaufzeit, Prozesskosten, Lagerumschlagshäufigkeit, Termintreue, Datenqualität.

Die Arbeit ist in **LaTeX** gesetzt, umfasst 15 Seiten mit 31 wissenschaftlichen Quellen und ist als PDF aus `main.tex` generierbar.

---

## ⚡ QUICK START

```bash
# Ins Projektverzeichnis wechseln
cd "Bachelor - Kuenstliche Intelligenz und Maschinelles Lernen/B-IBI02XX - Informationssysteme und Business Intelligence"

# LaTeX-Dokument kompilieren
pdflatex main.tex && pdflatex main.tex
# oder automatisch
latexmk -pdf main.tex

# Alternativ: Online mit Papeeria arbeiten
# 1. Gehe auf https://m.papeeria.com
# 2. Erstelle ein neues Projekt und importiere den gesamten Ordner als ZIP
# 3. Papeeria kompiliert main.tex automatisch in der Cloud
```

---

## 📁 STRUKTUR

```text
B-IBI02XX - Informationssysteme und Business Intelligence/
├── 📁 asset/
│   └── 📁 image/
│       ├── 🖼️ Data-Mining-Prozess.png
│       ├── 🖼️ ERP-Prozesse.png
│       ├── 🖼️ Stammdaten.png
│       ├── 🖼️ Star-Schema.png
│       └── 🖼️ WBH.png
├── 📁 chapter/
│   ├── 📝 1.tex
│   ├── 📝 2.tex
│   ├── 📝 3.tex
│   ├── 📝 4.tex
│   ├── 📝 5.tex
│   └── 📝 Zusammenfassung.tex
├── 📁 config/
│   ├── 📝 acronym.tex
│   ├── 📝 bibliography.bib
│   ├── 📝 settings.tex
│   └── 📝 titlepage.tex
├── 📄 main.tex
├── 📁 Detailed/
│   ├── 📁 asset/
│   │   └── 📁 image/
│   │       └── 🖼️ Stammdaten.png
│   ├── 📁 chapter/
│   │   ├── 📝 1.tex
│   │   ├── 📝 2.tex
│   │   ├── 📝 3.tex
│   │   ├── 📝 4.tex
│   │   └── 📝 5.tex
│   ├── 📁 config/
│   │   ├── 📝 acronym.tex
│   │   ├── 📝 bibliography.bib
│   │   ├── 📝 settings.tex
│   │   └── 📝 titlepage.tex
└── └── 📄 main.tex
```

### 📁 Struktur-Legende
```text
B-IBI02XX - Informationssysteme und Business Intelligence/
├── 📄 README.md          # Projektbeschreibung (diese Datei)
├── 📁 asset/image/       # Abbildungen (Star-Schema, Data-Mining, ERP-Prozesse)
├── 📁 chapter/           # LaTeX-Kapitel für jede der fünf Aufgaben
├── 📁 config/            # Einstellungen, Literaturverzeichnis, Deckblatt
│   ├── 📝 acronym.tex    # Abkürzungsverzeichnis
│   ├── 📝 bibliography.bib # Quellenverzeichnis (31 Einträge)
│   ├── 📝 settings.tex   # Dokument-Einstellungen
│   └── 📝 titlepage.tex  # Deckblatt
└── 📄 main.tex           # LaTeX-Hauptdokument
```

---

## 🚀 TOOL

| Bereich | Werkzeug |
|---------|----------|
| Dokumentation | LaTeX (erstellt mit Papeeria / lokalem TeXLive) |
| Visualisierung | Eigene Darstellungen (Star-Schema, ERP-Prozesse) |
| Literatur | 31 Quellen (Gronau, Gattnar, Goram, Apel u.a.) |
| Versionskontrolle | Git & GitHub |

---

## ⚠️ WICHTIGE HINWEISE

- 🔒 Keine PDFs committen – das Repository enthält nur LaTeX‑Quelltexte und Abbildungen.
- 🎓 Eigenständigkeit – alle Ausführungen sind in eigenen Worten formuliert und wissenschaftlich belegt.
- 📚 Quellenangaben – sämtliche Aussagen sind mit 31 Literaturverweisen hinterlegt.
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
- 📘 Typ: Einsendeaufgabe / Fachdokumentation
- 🎯 Ziel: Fundierte Analyse betrieblicher Informationssysteme und Business Intelligence
- 🛠️ Werkzeuge: LaTeX, Papeeria, Git

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
