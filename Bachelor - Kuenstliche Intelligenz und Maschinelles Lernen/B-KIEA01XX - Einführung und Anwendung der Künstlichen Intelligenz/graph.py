# !/usr/bin/env python
# -*- coding: utf-8 -*-
# graph.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

from collections import deque # 3D
from config import (
    # GUI - Logging
    TomaKingGUI_LogSeparatorCharEqual,
    TomaKingGUI_LogSeparatorLength,
    # AUFGABE 1B - Geschwindigkeiten
    TomaKing1B_SpeedStandard,
    TomaKing1B_SpeedExpress,
    # AUFGABE 3A - Kosten-Modell
    TomaKing3A_BaseCost,
    # AUFGABE 3A - Engpass
    TomaKing3A_BottleneckMaxNeighbors,
    TomaKing3A_BottleneckPenalty,
    # AUFGABE 3A - Sample
    TomaKing3A_SampleSize,
    # AUFGABE 3A - Logging
    TomaKing3A_LogNodeCountTemplate,
    TomaKing3A_LogEdgeCountTemplate,
    TomaKing3A_LogBottleneckCountTemplate,
    TomaKing3A_LogSampleHeader,
    TomaKing3A_LogSampleNodeTemplate,
    TomaKing3A_LogSampleEdgeTemplate,
)

## =============================================================================
# ========================== AUFGABE 3A - GRAPH-KLASSE ==========================
## =============================================================================

class Graph:
    # Erzeugt einen gewichteten Graphen aus einer Karte. Knoten sind die freien Zellen, Kanten die 4-Nachbarschaften.
    def __init__(self, map_instance):
        self._map = map_instance
        self._nodes = map_instance.get_free_cells()
        self._bottlenecks = self._compute_bottlenecks()
        self._bfs_cache = {}   # 3D
        self._log_statistics()
        self._log_sample()

## =============================================================================
# ====================== AUFGABE 3A - KNOTEN & NACHBARSCHAFT ====================
## =============================================================================

    # Gibt die Anzahl der Knoten (befahrbaren Zellen) zurück.
    def get_node_count(self) -> int:
        return len(self._nodes)
    # Gibt alle Nachbarn eines Knotens zurück (delegiert an die Karte).
    def get_neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        return self._map.get_neighbors(x, y)
    # Gibt die Kantenanzahl als Summe der Nachbarschaften / 2 zurück (ungerichtete Kanten).
    def get_edge_count(self) -> int:
        total = 0
        for (x, y) in self._nodes:
            total += len(self._map.get_neighbors(x, y))
        return total // 2
    # Gibt die Liste aller Knoten (befahrbaren Zellen) zurück.
    def get_nodes(self) -> list[tuple[int, int]]:
        return list(self._nodes)

## =============================================================================
# ========================= AUFGABE 3A - ENGPASS-ANALYSE ========================
## =============================================================================

    # Ermittelt alle Engpass-Zellen (Zellen mit maximal TomaKing3A_BottleneckMaxNeighbors Nachbarn).
    def _compute_bottlenecks(self) -> set:
        bottlenecks = set()
        for (x, y) in self._nodes:
            if len(self._map.get_neighbors(x, y)) <= TomaKing3A_BottleneckMaxNeighbors:
                bottlenecks.add((x, y))
        return bottlenecks
    # Prüft, ob eine Zelle ein Engpass ist.
    def is_bottleneck(self, x: int, y: int) -> bool:
        return (x, y) in self._bottlenecks
    # Gibt die Anzahl der Engpass-Zellen zurück.
    def get_bottleneck_count(self) -> int:
        return len(self._bottlenecks)

## =============================================================================
# ==================== AUFGABE 3A - KANTEN-KOSTENMODELL =========================
## =============================================================================

    # Berechnet die Kosten einer Kante für eine gegebene Agentengeschwindigkeit.
    def get_edge_cost(self, from_pos: tuple, to_pos: tuple, agent_speed: int) -> float:
        cost = TomaKing3A_BaseCost / agent_speed
        if self.is_bottleneck(to_pos[0], to_pos[1]):
            cost += TomaKing3A_BottleneckPenalty
        return cost

## =============================================================================
# ======================= AUFGABE 3A - STATISTIKEN & LOG ========================
## =============================================================================

    # Liefert ein Dictionary mit den Graph-Kennzahlen.
    def get_statistics(self) -> dict:
        return {
            "nodes":       self.get_node_count(),
            "edges":       self.get_edge_count(),
            "bottlenecks": self.get_bottleneck_count(),
        }
    # Gibt die Graph-Statistiken und Beispiele auf der Konsole aus.
    def _log_statistics(self) -> None:
        print(TomaKing3A_LogNodeCountTemplate.format(self.get_node_count()))
        print(TomaKing3A_LogEdgeCountTemplate.format(self.get_edge_count()))
        print(TomaKing3A_LogBottleneckCountTemplate.format(self.get_bottleneck_count()))
    # Gibt eine Auswahl an Knoten mit ihren Nachbarschaften und Kantenkosten aus.
    def _log_sample(self) -> None:
        print(TomaKing3A_LogSampleHeader)
        for (x, y) in self._nodes[:TomaKing3A_SampleSize]:
            print(TomaKing3A_LogSampleNodeTemplate.format((x, y)))
            for (nx, ny) in self.get_neighbors(x, y):
                standard_cost = self.get_edge_cost((x, y), (nx, ny), TomaKing1B_SpeedStandard)
                express_cost  = self.get_edge_cost((x, y), (nx, ny), TomaKing1B_SpeedExpress)
                print(TomaKing3A_LogSampleEdgeTemplate.format(
                    (nx, ny), standard_cost, express_cost))
        print(TomaKingGUI_LogSeparatorCharEqual * TomaKingGUI_LogSeparatorLength)

## =============================================================================
# ====================== AUFGABE 3D - BFS-HEURISTIK-CACHE =======================
## =============================================================================

    # Berechnet die BFS-Distanz aller Knoten zu einem Ziel und cached das Ergebnis.
    def compute_bfs_from(self, goal: tuple) -> dict:
        dist = {goal: 0}
        queue = deque([goal])
        while queue:
            cx, cy = queue.popleft()
            for (nx, ny) in self.get_neighbors(cx, cy):
                if (nx, ny) not in dist:
                    dist[(nx, ny)] = dist[(cx, cy)] + 1
                    queue.append((nx, ny))
        return dist
    # Liefert die gecachte BFS-Distanz eines Knotens zum Ziel (lazy Population).
    def get_bfs_distance(self, node: tuple, goal: tuple) -> int:
        if goal not in self._bfs_cache:
            self._bfs_cache[goal] = self.compute_bfs_from(goal)
        return self._bfs_cache[goal].get(node, float("inf"))