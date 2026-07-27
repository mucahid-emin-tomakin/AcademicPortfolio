<?php
// report.php - Auswertung der Umfragedaten

// Datenbankverbindung einbinden
require __DIR__ . '/inc/db.php';

// ============================================================
// 1. Angemeldete Personen (nicht anonymous)
// ============================================================
$sqlAngemeldet = "
    SELECT COUNT(DISTINCT s.UserId) AS count
    FROM survey_table s
    JOIN user_table u ON s.UserId = u.Id
    WHERE u.Name != 'anonymous'
";
$stmt = $pdo->query($sqlAngemeldet);
$angemeldet = $stmt->fetchColumn();

// ============================================================
// 2. Anonyme Personen (alle anonymen Teilnahmen)
// ============================================================
$sqlAnonym = "
    SELECT COUNT(*) AS count
    FROM survey_table s
    JOIN user_table u ON s.UserId = u.Id
    WHERE u.Name = 'anonymous'
";
$stmt = $pdo->query($sqlAnonym);
$anonym = $stmt->fetchColumn();

// ============================================================
// 3. Gesamt (alle Teilnahmen)
// ============================================================
$sqlGesamt = "SELECT COUNT(*) FROM survey_table";
$stmt = $pdo->query($sqlGesamt);
$gesamt = $stmt->fetchColumn();

// ============================================================
// 4. Ausgabe
// ============================================================
?>
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auswertung</title>
</head>
<body>
    <h1>Auswertung</h1>
    <ul>
        <li><strong>Angemeldete Personen:</strong> <?php echo $angemeldet; ?></li>
        <li><strong>Anonyme Personen:</strong> <?php echo $anonym; ?></li>
        <li><strong>Gesamt an der Umfrage teilgenommene Personen:</strong> <?php echo $gesamt; ?></li>
    </ul>
    <p><a href="index.php">Zurück zur Startseite</a></p>
</body>
</html>