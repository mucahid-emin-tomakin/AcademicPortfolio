<?php

// Datenbank-Konfiguration
$host     = 'localhost';
$database = 'umfrage_db';
$username = 'root';
$password = '';  // Standard bei XAMPP: leer

// PDO-Verbindung herstellen
try {
    $pdo = new PDO("mysql:host=$host;dbname=$database;charset=utf8mb4", $username, $password);
    
    // PDO-Fehlermodus auf Exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // Standard-Fetch-Modus (assoziative Arrays)
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    
} catch (PDOException $e) {
    // Bei Verbindungsfehler die Ausführung abbrechen
    die("Datenbankverbindung fehlgeschlagen: " . $e->getMessage());
}

?>