# 📊 B-DBI02XX – Datenbanken – PHP/MySQL Umfrageanwendung

![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-8.2-777BB4?logo=php&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-10.4-003545?logo=mariadb&logoColor=white)
![XAMPP](https://img.shields.io/badge/XAMPP-8.2-FB7A24?logo=xampp&logoColor=white)
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

Diese Einsendeaufgabe befasst sich mit der **Entwicklung einer webbasierten Umfrageanwendung** auf Basis von **PHP** und **MariaDB** – basierend auf den Studieninhalten der Module *Datenbanken in Webanwendungen* (DBI15) und *Verteilte Datenbanken* (DBI05) der Wilhelm Büchner Hochschule.

Die Arbeit gliedert sich in sechs Hauptaufgaben, die den vollständigen Entwicklungszyklus einer Webanwendung abdecken:

**1. Datenbankdesign (Aufgabe 1)**
- Erstellung der Datenbank `umfrage_db` mit zwei Tabellen:
  - `user_table` (Id, Name) – für die Nutzerverwaltung
  - `survey_table` (Id, UserId, Datum, Q1–Q5) – für die Umfrageantworten
- Fremdschlüsselbeziehung zwischen den Tabellen (UserId → Id)
- Befüllung der `user_table` mit drei Testdatensätzen (`anonymous`, `Lara`, `Luisa`)
- Export der gesamten Datenbank als `db.sql` über phpMyAdmin

**2. Projektstruktur und Datenbankanbindung (Aufgabe 2)**
- Einrichtung der Ordnerstruktur `survey/inc/` für die Webanwendung
- Implementierung der Datei `db.php` mit **PDO** (PHP Data Objects) für die Datenbankverbindung
- Verwendung von Prepared Statements zur Sicherheit gegen SQL-Injection
- Konfiguration der Verbindungsparameter (Host, Datenbankname, Benutzer, Passwort)

**3. Startseite und Namensübergabe (Aufgabe 3)**
- Erstellung von `index.php` (Startseite mit Namenseingabe)
- Übergabe des Namens per **GET**-Request an `survey.php`
- Erlaubnis einer leeren Eingabe für anonyme Teilnahme
- XSS-Schutz durch `htmlspecialchars()`

**4. Validierung und Umfrageformular (Aufgabe 4)**
- Prüfung, ob der eingegebene Name bereits in `user_table` existiert
- Ausgabe einer Fehlermeldung bei bereits registrierten Nutzern
- Behandlung leerer Eingaben als `anonymous` (ohne doppelte Anlage)
- Anzeige eines Umfrageformulars mit fünf Fragen (Dropdown, Radio, Textfeld, Textarea)

**5. Speichern der Umfragedaten (Aufgabe 5)**
- Entgegennahme der POST-Daten aus dem Formular
- Erzeugung des aktuellen Datums mit `date('Y-m-d')`
- Speicherung in `survey_table` mit Prepared Statements
- Anzeige einer Erfolgsmeldung mit Link zum Report

**6. Auswertung der Umfragedaten (Aufgabe 6)**
- Erstellung von `report.php` mit drei SQL-Abfragen
- Ermittlung der **angemeldeten Personen** (DISTINCT, nicht anonymous)
- Ermittlung der **anonymen Personen** (alle anonymous-Einträge)
- Ermittlung der **Gesamtteilnahmen** (COUNT(*) aus survey_table)
- Übersichtliche Ausgabe als Liste

Die gesamte Entwicklung wurde in der **XAMPP**-Umgebung (Apache + MariaDB + PHP) durchgeführt und die Ergebnisse in einer **LaTeX‑Dokumentation** festgehalten. Die Arbeit umfasst etwa 60 Seiten (inkl. Abbildungs‑, Tabellen‑ und Code‑Verzeichnis) und ein Abkürzungsverzeichnis mit den relevanten Fachbegriffen.

---

## ✨ FEATURES

| Feature | Beschreibung |
|---------|-------------|
| 🗄️ Datenbankanbindung | PDO mit Prepared Statements für sicheren Datenbankzugriff |
| 👤 Nutzerverwaltung | Registrierte Nutzer vs. anonyme Teilnahme |
| ✅ Validierung | Prüfung auf bereits existierende Nutzer |
| 📝 Umfrageformular | Fünf Fragen in verschiedenen Eingabetypen (Select, Radio, Text, Textarea) |
| 💾 Datenspeicherung | INSERT in `survey_table` mit automatischem Datum |
| 📊 Auswertung | Drei Statistiken (angemeldet, anonym, gesamt) |
| 🛡️ Sicherheit | XSS-Schutz mit `htmlspecialchars()`, SQL-Injection-Schutz mit PDO |
| 🎨 Benutzerfreundlichkeit | Klare Navigation zwischen den Seiten |
| 📄 LaTeX‑Dokumentation | Professionelles wissenschaftliches Layout mit allen Code‑Listings und Abbildungen |
| 🔗 Versionskontrolle | Git & GitHub für Nachvollziehbarkeit |

---

## 🚀 TOOL

| Bereich | Werkzeug |
|---------|----------|
| **Programmiersprache** | PHP 8.2 |
| **Datenbank** | MariaDB 10.4 (über XAMPP) |
| **Webserver** | Apache 2.4 (über XAMPP) |
| **Datenbankverwaltung** | phpMyAdmin 5.2 |
| **Entwicklungsumgebung** | XAMPP 8.2 |
| **Dokumentation** | LaTeX (kompiliert mit lokalem TeXLive / Papeeria) |
| **Versionskontrolle** | Git & GitHub |
| **Betriebssystem** | Windows 11 (22H2) |

---

## 📁 STRUKTUR

```text
📓 B-DBI02XX - Datenbanken/
├── 📄 README.md                                              # Diese Datei
├── 📄 main.tex                                                # LaTeX‑Hauptdokument
│
├── 📁 B-DBI02XX/                                               # Die Webanwendung
│   └── 📁 survey/                                              # Hauptverzeichnis der Anwendung
│       ├── 📄 index.php                                        # Startseite mit Namenseingabe
│       ├── 📄 survey.php                                       # Validierung + Umfrageformular
│       ├── 📄 save.php                                         # Speichern der Umfragedaten
│       ├── 📄 report.php                                       # Auswertung der Daten
│       └── 📁 inc/                                             # Include‑Ordner
│           ├── 📄 db.php                                       # Datenbankverbindung (PDO)
│           └── 📄 db.sql                                       # SQL‑Dump der Datenbank
│
├── 📁 asset/
│   ├── 📁 code/                                                # Alle Code‑Listings (als .tex)
│   │   ├── 📝 Aufgabe1a.tex
│   │   ├── 📝 Aufgabe1b.tex
│   │   ├── 📝 Aufgabe1c.tex
│   │   ├── 📝 Aufgabe2.tex
│   │   ├── 📝 Aufgabe2II.tex
│   │   ├── 📝 Aufgabe3.tex
│   │   ├── 📝 Aufgabe3II.tex
│   │   ├── 📝 Aufgabe4.tex
│   │   ├── 📝 Aufgabe4II.tex
│   │   ├── 📝 Aufgabe5.tex
│   │   ├── 📝 Aufgabe6.tex
│   │   └── 📝 Einleitung.tex
│   │
│   └── 📁 image/                                                # Alle Abbildungen (Screenshots)
│       ├── 🖼️ Aufgabe3.png
│       ├── 🖼️ Aufgabe3II.png
│       ├── 🖼️ Aufgabe3III.png
│       ├── 🖼️ Aufgabe3IV.png
│       ├── 🖼️ Aufgabe4.png
│       ├── 🖼️ Aufgabe4II.png
│       ├── 🖼️ Aufgabe5.png
│       ├── 🖼️ Aufgabe6.png
│       └── 🖼️ WBH.png
│
├── 📁 chapter/                                                 # LaTeX‑Kapitel
│   ├── 📝 Einleitung.tex
│   ├── 📝 Aufgabe1.tex
│   ├── 📝 Aufgabe2.tex
│   ├── 📝 Aufgabe3.tex
│   ├── 📝 Aufgabe4.tex
│   ├── 📝 Aufgabe5.tex
│   ├── 📝 Aufgabe6.tex
│   └── 📝 Zusammenfassung.tex
│
└── 📁 config/                                                   # Konfiguration & Einstellungen
    ├── 📝 acronym.tex                                           # Abkürzungsverzeichnis
    ├── 📝 bibliography.bib                                      # Literaturverzeichnis
    ├── 📝 settings.tex                                          # Dokument‑Einstellungen
    └── 📝 titlepage.tex                                         # Titelseite mit Matrikelnummer
```

### 📁 Struktur-Legende
```text
📓 B-DBI02XX - Datenbanken/
├── 📄 README.md              # Projektbeschreibung (diese Datei)
├── 📄 main.tex               # LaTeX‑Hauptdokument
├── 📁 B-DBI02XX/             # Die Webanwendung
│   └── 📁 survey/            # Hauptverzeichnis der Anwendung
│       ├── 📄 index.php      # Startseite
│       ├── 📄 survey.php     # Validierung + Formular
│       ├── 📄 save.php       # Speichern
│       ├── 📄 report.php     # Auswertung
│       └── 📁 inc/
│           ├── 📄 db.php     # Datenbankverbindung
│           └── 📄 db.sql     # SQL‑Dump
├── 📁 asset/
│   ├── 📁 code/              # Code‑Listings für LaTeX
│   └── 📁 image/             # Screenshots & Abbildungen
├── 📁 chapter/               # LaTeX‑Kapitel (Einleitung, 6 Aufgaben, Zusammenfassung)
└── 📁 config/                # Einstellungen, Abkürzungen, Literatur, Titelseite
```

---

## ⚡ QUICK START

### 🔧 Voraussetzungen
- **XAMPP** 8.2 (Apache + MariaDB + PHP)
- **Git** (optional, für Versionskontrolle)
- **LaTeX‑Distribution** (z.B. TeXLive oder MiKTeX) – für die PDF‑Erstellung

### 📦 Git & GitHub
```bash
# Repository klonen
git clone https://github.com/mucahid-emin-tomakin/AcademicPortfolio.git
cd AcademicPortfolio

# Ins Projektverzeichnis wechseln
cd "Bachelor - Kuenstliche Intelligenz und Maschinelles Lernen/B-DBI02XX - Datenbanken"
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

### 🗄️ Datenbank einrichten
1. **XAMPP starten**: Apache + MySQL (MariaDB) starten.
2. **phpMyAdmin öffnen**: `http://localhost/phpmyadmin/`.
3. **Neue Datenbank anlegen**: Name `umfrage_db`, Zeichensatz `utf8mb4_general_ci`.
4. **SQL-Import**: Tab "Import" → Datei `B-DBI02XX/survey/inc/db.sql` auswählen → "Los" klicken.
5. **Prüfen**: Die Tabellen `user_table` und `survey_table` sollten erscheinen.

### 🌐 Anwendung starten
1. **Dateien verschieben**: Die gesamte `B-DBI02XX/` in das `htdocs`-Verzeichnis von XAMPP kopieren:
   ```bash
   # Beispiel (Windows)
   C:\xampp\htdocs\B-DBI02XX\
   ```
2. **Webserver starten**: Apache läuft (wurde bereits gestartet).
3. **Anwendung aufrufen**: Im Browser `http://localhost/B-DBI02XX/survey/index.php` öffnen.
4. **Umfrage durchlaufen**:
- Name eingeben (oder leer lassen für anonym)
- Fünf Fragen beantworten
- Absenden → Erfolgsmeldung
- Report aufrufen: `http://localhost/B-DBI02XX/survey/report.php`

---

## ⚠️ WICHTIGE HINWEISE

- 🔒 **Keine sensiblen Daten** – die Anwendung verwendet nur Testdaten und ist für den lokalen Betrieb konzipiert.
- 🎓 **Eigenständigkeit** – alle Code-Implementierungen und die LaTeX-Dokumentation sind eigenständig verfasst.
- 📚 **Quellenangaben** – alle zitierten Aussagen sind mit den Studienheften [1–3] hinterlegt.
- 🧪 **Reproduzierbarkeit** – das gesamte Dokument muss aus den LaTeX‑Quellen kompilierbar sein; alle PHP‑Dateien sind im Ordner `B-DBI02XX/survey/` enthalten.
- 🌍 **Plattformunabhängigkeit** – die Arbeit wurde unter Windows 11 (22H2) entwickelt, die verwendeten Tools sind jedoch plattformunabhängig.
- 📌 **Pfadangaben** – in den PHP‑Dateien werden relative Pfade (`require __DIR__ . '/inc/db.php'`) verwendet; beim Klonen ist keine Anpassung nötig.
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
- 🎯 Ziel: Praktische Umsetzung einer webbasierten Umfrageanwendung mit PHP und MariaDB
- 🛠️ Werkzeuge: PHP, MariaDB, XAMPP, LaTeX, Git

---

## 📊 REPOSITORY STATISTIK

| Metrik | Wert | Trend |
|--------|------|-------|
| **Stars** | ![GitHub Stars](https://img.shields.io/github/stars/mucahid-emin-tomakin/AcademicPortfolio) | 📈 |
| **Forks** | ![GitHub Forks](https://img.shields.io/github/forks/mucahid-emin-tomakin/AcademicPortfolio) | 🔄 |
| **Issues** | ![GitHub Issues](https://img.shields.io/github/issues/mucahid-emin-tomakin/AcademicPortfolio) | ✅ |
| **Letztes Update** | ![GitHub Last Commit](https://img.shields.io/github/last-commit/mucahid-emin-tomakin/AcademicPortfolio) | 🕐 |

---

### 🔧 Made with ❤️ on LaTeX, PHP, and MariaDB
