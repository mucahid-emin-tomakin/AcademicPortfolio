# !/usr/bin/env python
# -*- coding: utf-8 -*-
# map.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

from collections import deque
import random
from config import (
    # GUI - Logging
    TomaKingGUI_LogSeparatorCharEqual,
    TomaKingGUI_LogSeparatorLength,
    # AUFGABE 1A - ASCII-Art
    TomaKing1A_ASCIIArt,
    # AUFGABE 1A - Symbole
    TomaKing1A_Wall,
    TomaKing1A_Empty,
    TomaKing1A_Depot,
    TomaKing1A_Target,
    # AUFGABE 1A - Parameter
    TomaKing1A_DepotCount,
    TomaKing1A_TargetCount,
    TomaKing1A_Seed,
    TomaKing1A_BorderSize,
    TomaKing1A_Directions,
    # AUFGABE 1A - Rand & Koordinaten
    TomaKing1A_BorderOffset,
    TomaKing1A_StartDepotIndex,
    TomaKing1A_MinCoordinate,
    TomaKing1A_SidesCount,
    # AUFGABE 1A - Statistics
    TomaKing1A_StatKeyWidth,
    TomaKing1A_StatKeyHeight,
    TomaKing1A_StatKeyDepotCount,
    TomaKing1A_StatKeyTargetCount,
    TomaKing1A_StatKeyWallCount,
    TomaKing1A_StatKeyEmptyCount,
    TomaKing1A_StatKeyDepots,
    TomaKing1A_StatKeyTargets,
    # AUFGABE 1A - Logging
    TomaKing1A_LogMapSize,
    TomaKing1A_LogDepots,
    TomaKing1A_LogTargets,
    TomaKing1A_LogWalls,
    TomaKing1A_LogEmpty,
    TomaKing1A_LogMapASCII,
    # AUFGABE 1A - Error Handling
    TomaKing1A_ErrorNotEnoughCells,
    TomaKing1A_ErrorNoFreeCells,
    TomaKing1A_ErrorNotConnected,
)

## =============================================================================
# =========================== AUFGABE 1A - MAP CLASS ============================
## =============================================================================

class Map:
    # Initialisiert die Karte mit festem Seed und ruft alle Erstellungs- und Prüfroutinen auf.
    def __init__(self, seed: int | None = None):
        self.seed = seed if seed is not None else TomaKing1A_Seed
        self._data = []
        self._depots = []
        self._targets = []
        self._init_from_ascii_art_with_border()
        self._place_depots_and_targets()
        self._validate()
        self._log_statistics()

## =============================================================================
# ======================= AUFGABE 1A - MAP-INITIALISATION =======================
## =============================================================================

    # Wandelt die ASCII-Art in eine 2D-Liste um und fügt auf allen vier Seiten einen freien Rand hinzu.
    def _init_from_ascii_art_with_border(self) -> None:
        original_height = len(TomaKing1A_ASCIIArt)
        original_width = max(len(row) for row in TomaKing1A_ASCIIArt)
        self.height = original_height + TomaKing1A_SidesCount * TomaKing1A_BorderSize
        self.width = original_width + TomaKing1A_SidesCount * TomaKing1A_BorderSize
        self._data = [
            [TomaKing1A_Empty for _ in range(self.width)]
            for _ in range(self.height)
        ]
        for y, row in enumerate(TomaKing1A_ASCIIArt):
            for x, char in enumerate(row):
                if char == TomaKing1A_Wall:
                    self._data[y + TomaKing1A_BorderOffset][x + TomaKing1A_BorderOffset] = TomaKing1A_Wall

## =============================================================================
# ========================= AUFGABE 1A - DEPOTS & ZIELE =========================
## =============================================================================

    # Platziert zufällig (aber reproduzierbar) die konfigurierte Anzahl Depots und Ziele auf freien Zellen.
    def _place_depots_and_targets(self) -> None:
        total = TomaKing1A_DepotCount + TomaKing1A_TargetCount
        free_cells = []
        for y in range(self.height):
            for x in range(self.width):
                if self._data[y][x] == TomaKing1A_Empty:
                    free_cells.append((x, y))
        if len(free_cells) < total:
            raise ValueError(TomaKing1A_ErrorNotEnoughCells.format(TomaKing1A_DepotCount, TomaKing1A_TargetCount))
        random.seed(self.seed)
        selected = random.sample(free_cells, total)
        self._depots = selected[:TomaKing1A_DepotCount]
        self._targets = selected[TomaKing1A_DepotCount:total]
        for x, y in self._depots:
            self._data[y][x] = TomaKing1A_Depot
        for x, y in self._targets:
            self._data[y][x] = TomaKing1A_Target

## =============================================================================
# ======================= AUFGABE 1A - VALIDIERUNG (BFS) ========================
## =============================================================================

    # Prüft, ob es mindestens eine freie Zelle gibt und ob alle Depots/Ziele vom ersten Depot aus erreichbar sind.
    def _validate(self) -> None:
        has_free_cell = False
        for y in range(self.height):
            for x in range(self.width):
                if self._data[y][x] == TomaKing1A_Empty:
                    has_free_cell = True
                    break
            if has_free_cell:
                break
        if not has_free_cell:
            raise ValueError(TomaKing1A_ErrorNoFreeCells)
        if not self._is_connected():
            raise ValueError(TomaKing1A_ErrorNotConnected)
    # Führt eine Breitensuche vom konfigurierten Start-Depot aus durch und prüft, ob alle Depots und Ziele erreicht werden.
    def _is_connected(self) -> bool:
        if not self._depots:
            return False
        start = self._depots[TomaKing1A_StartDepotIndex]
        visited = set()
        queue = deque([start])
        visited.add(start)
        targets = set(self._depots + self._targets)
        while queue:
            x, y = queue.popleft()
            for nx, ny in self.get_neighbors(x, y):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        return targets.issubset(visited)

## =============================================================================
# ====================== AUFGABE 1A - ÖFFENTLICHE METHODEN ======================
## =============================================================================

    # Prüft, ob eine Zelle begehbar ist (innerhalb der Karte und keine Wand).
    def is_walkable(self, x: int, y: int) -> bool:
        if not (TomaKing1A_MinCoordinate <= x < self.width and TomaKing1A_MinCoordinate <= y < self.height):
            return False
        return self._data[y][x] != TomaKing1A_Wall
    # Gibt alle begehbaren Nachbarzellen einer gegebenen Zelle zurück (4-Richtungen).
    def get_neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        directions = TomaKing1A_Directions
        result = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_walkable(nx, ny):
                result.append((nx, ny))
        return result
    # Gibt alle freien (begehbaren und leeren) Zellen der Karte als Liste zurück. - 1B
    def get_free_cells(self) -> list[tuple[int, int]]:
        result = []
        for y in range(self.height):
            for x in range(self.width):
                if self._data[y][x] == TomaKing1A_Empty:
                    result.append((x, y))
        return result
    # Gibt die Positionen aller Depots als Liste von Tupeln zurück. - 2A
    def get_depots(self) -> list[tuple[int, int]]:
        return list(self._depots)
    # Erzeugt einen ASCII-String der gesamten Karte (für Debugging/Logging).
    def to_string(self) -> str:
        rows = []
        for y in range(self.height):
            row = ''.join(self._data[y])
            rows.append(row)
        return '\n'.join(rows)
    # Gibt die Karte als String zurück (wird von print() verwendet).
    def __str__(self) -> str:
        return self.to_string()
    # Öffentlicher Zugriff auf den Zellenwert (Datenkapselung)
    def get_cell(self, x: int, y: int) -> str:
        if TomaKing1A_MinCoordinate <= x < self.width and TomaKing1A_MinCoordinate <= y < self.height:
            return self._data[y][x]
        return TomaKing1A_Wall

## =============================================================================
# ===================== AUFGABE 1A - STATISTIKEN & LOGGING ======================
## =============================================================================

    # Sammelt alle statistischen Kennzahlen der Karte (Größe, Anzahl Depots, Wände usw.).
    def get_statistics(self) -> dict:
        wall_count = 0
        empty_count = 0
        for y in range(self.height):
            for x in range(self.width):
                if self._data[y][x] == TomaKing1A_Wall:
                    wall_count += 1
                elif self._data[y][x] == TomaKing1A_Empty:
                    empty_count += 1
        return {
            TomaKing1A_StatKeyWidth:      self.width,
            TomaKing1A_StatKeyHeight:     self.height,
            TomaKing1A_StatKeyDepotCount: len(self._depots),
            TomaKing1A_StatKeyTargetCount:len(self._targets),
            TomaKing1A_StatKeyWallCount:  wall_count,
            TomaKing1A_StatKeyEmptyCount: empty_count,
            TomaKing1A_StatKeyDepots:     self._depots,
            TomaKing1A_StatKeyTargets:    self._targets,
        }
    # Gibt die Statistiken und die Karte im ASCII-Format auf der Konsole aus.
    def _log_statistics(self) -> None:
        stats = self.get_statistics()
        print(TomaKingGUI_LogSeparatorCharEqual * TomaKingGUI_LogSeparatorLength)
        print(TomaKing1A_LogMapSize.format(stats[TomaKing1A_StatKeyWidth], stats[TomaKing1A_StatKeyHeight]))
        print(TomaKing1A_LogDepots.format(stats[TomaKing1A_StatKeyDepotCount], stats[TomaKing1A_StatKeyDepots]))
        print(TomaKing1A_LogTargets.format(stats[TomaKing1A_StatKeyTargetCount], stats[TomaKing1A_StatKeyTargets]))
        print(TomaKing1A_LogWalls.format(stats[TomaKing1A_StatKeyWallCount]))
        print(TomaKing1A_LogEmpty.format(stats[TomaKing1A_StatKeyEmptyCount]))
        print(TomaKingGUI_LogSeparatorCharEqual * TomaKingGUI_LogSeparatorLength)
        print(TomaKing1A_LogMapASCII)
        print(self.to_string())