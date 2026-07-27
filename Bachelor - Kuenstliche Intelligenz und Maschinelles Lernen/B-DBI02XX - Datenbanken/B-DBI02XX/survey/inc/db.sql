-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 26. Jul 2026 um 16:09
-- Server-Version: 10.4.32-MariaDB
-- PHP-Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `umfrage_db`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `survey_table`
--

CREATE TABLE `survey_table` (
  `Id` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  `Datum` date NOT NULL,
  `Q1` varchar(255) NOT NULL,
  `Q2` varchar(255) NOT NULL,
  `Q3` varchar(255) NOT NULL,
  `Q4` varchar(255) NOT NULL,
  `Q5` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `user_table`
--

CREATE TABLE `user_table` (
  `Id` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `user_table`
--

INSERT INTO `user_table` (`Id`, `Name`) VALUES
(1, 'anonymous'),
(2, 'Lara'),
(3, 'Luisa');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `survey_table`
--
ALTER TABLE `survey_table`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `UserId` (`UserId`);

--
-- Indizes für die Tabelle `user_table`
--
ALTER TABLE `user_table`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `survey_table`
--
ALTER TABLE `survey_table`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `user_table`
--
ALTER TABLE `user_table`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `survey_table`
--
ALTER TABLE `survey_table`
  ADD CONSTRAINT `survey_table_ibfk_1` FOREIGN KEY (`UserId`) REFERENCES `user_table` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
