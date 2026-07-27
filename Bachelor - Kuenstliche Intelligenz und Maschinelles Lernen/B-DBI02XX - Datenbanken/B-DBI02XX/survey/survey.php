<?php
// survey.php - Umfrageseite mit Validierung und Formular

// Datenbankverbindung einbinden
require __DIR__ . '/inc/db.php';

// Namen aus GET-Parameter auslesen
$name = isset($_GET['name']) ? trim($_GET['name']) : '';

// ============================================================
// 1. Fehlerbehandlung: Name existiert bereits in der DB
// ============================================================
$error = null;
$userId = null;
$displayName = '';

if ($name !== '') {
    // Prüfen, ob der Name bereits in user_table existiert
    $stmt = $pdo->prepare("SELECT Id FROM user_table WHERE Name = ?");
    $stmt->execute([$name]);
    $existingUser = $stmt->fetch();

    if ($existingUser) {
        $error = "Nutzer existiert schon, bitte anderen Namen wählen!";
    }
}

// ============================================================
// 2. Leerer Parameter -> anonymous
// ============================================================
if ($name === '' && $error === null) {
    // Prüfen, ob anonymous bereits existiert
    $stmt = $pdo->prepare("SELECT Id FROM user_table WHERE Name = 'anonymous'");
    $stmt->execute();
    $anonymousUser = $stmt->fetch();

    if ($anonymousUser) {
        // anonymous existiert bereits -> ID verwenden
        $userId = $anonymousUser['Id'];
        $displayName = 'anonym';
    } else {
        // anonymous existiert noch nicht -> neu anlegen
        $stmt = $pdo->prepare("INSERT INTO user_table (Name) VALUES ('anonymous')");
        $stmt->execute();
        $userId = $pdo->lastInsertId();
        $displayName = 'anonym';
    }
}

// ============================================================
// 3. Neuer Name (existiert noch nicht in der DB)
// ============================================================
if ($name !== '' && $error === null) {
    // Prüfen (sicherheitshalber nochmal), ob der Name existiert
    $stmt = $pdo->prepare("SELECT Id FROM user_table WHERE Name = ?");
    $stmt->execute([$name]);
    $existingUser = $stmt->fetch();

    if (!$existingUser) {
        // Neuen User anlegen
        $stmt = $pdo->prepare("INSERT INTO user_table (Name) VALUES (?)");
        $stmt->execute([$name]);
        $userId = $pdo->lastInsertId();
        $displayName = htmlspecialchars($name, ENT_QUOTES, 'UTF-8');
    } else {
        // sollte nicht passieren, da wir oben schon prüfen, aber zur Sicherheit
        $userId = $existingUser['Id'];
        $displayName = htmlspecialchars($name, ENT_QUOTES, 'UTF-8');
    }
}

// ============================================================
// 4. Wenn Fehler aufgetreten ist -> Meldung anzeigen
// ============================================================
if ($error !== null) {
    ?>
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fehler - Umfrage</title>
    </head>
    <body>
        <h1>Umfrage zum Studium</h1>
        <p style="color: red; font-weight: bold;"><?php echo htmlspecialchars($error, ENT_QUOTES, 'UTF-8'); ?></p>
        <p><a href="index.php">Zurück zur Startseite</a></p>
    </body>
    </html>
    <?php
    exit;
}

// ============================================================
// 5. Umfrageformular anzeigen (wenn alles OK ist)
// ============================================================
?>
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Umfrage - <?php echo $displayName; ?></title>
</head>
<body>

    <h1>Umfrage zum Studium</h1>
    <p>Teilnehmer: <strong><?php echo $displayName; ?></strong></p>

    <form action="save.php" method="post">

        <!-- Frage 1: Jahr -->
        <p><strong>Frage 1:</strong> In welchem Jahr hast du mit dem Studium begonnen?</p>
        <select name="Q1" required>
            <option value="">Bitte wählen...</option>
            <option value="2020">2020</option>
            <option value="2021">2021</option>
            <option value="2022">2022</option>
            <option value="2023">2023</option>
            <option value="2024">2024</option>
            <option value="2025">2025</option>
            <option value="2026">2026</option>
        </select>

        <!-- Frage 2: Zufriedenheit -->
        <p><strong>Frage 2:</strong> Bist du mit deinem Studium bis jetzt zufrieden?</p>
        <label><input type="radio" name="Q2" value="JA" required> JA</label><br>
        <label><input type="radio" name="Q2" value="NEIN"> NEIN</label>

        <!-- Frage 3: Dauer für B-Aufgabe -->
        <p><strong>Frage 3:</strong> Wie lange benötigst du für die Lösung einer B-Aufgabe?</p>
        <select name="Q3" required>
            <option value="">Bitte wählen...</option>
            <option value="1 Woche">1 Woche</option>
            <option value="2 Wochen">2 Wochen</option>
            <option value="1 Monat">1 Monat</option>
            <option value="2 Monate">2 Monate</option>
            <option value="3 Monate">3 Monate</option>
            <option value="länger">länger</option>
        </select>

        <!-- Frage 4: Lieblingsmodul -->
        <p><strong>Frage 4:</strong> Welches ist dein Lieblingsmodul im Studium?</p>
        <input type="text" name="Q4" placeholder="z.B. DBI15" required>

        <!-- Frage 5: Warum dieses Studium? -->
        <p><strong>Frage 5:</strong> Warum hast du dich für dieses Studium entschieden?</p>
        <textarea name="Q5" rows="4" cols="50" placeholder="Deine Antwort..." required></textarea>

        <!-- Hidden-Felder für UserId und Name (für save.php) -->
        <input type="hidden" name="userId" value="<?php echo $userId; ?>">
        <input type="hidden" name="displayName" value="<?php echo $displayName; ?>">

        <br><br>
        <button type="submit">Umfrage absenden</button>
    </form>

</body>
</html>