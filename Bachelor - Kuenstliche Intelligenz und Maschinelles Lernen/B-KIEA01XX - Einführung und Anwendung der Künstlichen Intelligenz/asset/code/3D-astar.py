# !/usr/bin/env python
# -*- coding: utf-8 -*-
# astar.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import heapq
from geometry import manhattan
from config import (
    # GUI - Logging
    TomaKingGUI_LogSeparatorCharLine,
    TomaKingGUI_LogSeparatorLength,
    # AUFGABE 3A - Kosten-Modell
    TomaKing3A_BaseCost,
    # AUFGABE 3B - Algorithmus
    TomaKing3B_InitialCost,
    # AUFGABE 3D - Heuristik-Modus
    TomaKing3D_HeuristicMode,
    TomaKing3D_ModeManhattan,
    TomaKing3D_ModeBFS,
    # AUFGABE 3D - Demo-Lauf
    TomaKing3D_DemoStart,
    TomaKing3D_DemoGoal,
    TomaKing3D_DemoAgentSpeed,
    # AUFGABE 3D - Log-Reduktion
    TomaKing3D_LogMaxSteps,
    TomaKing3D_LogStartIndex,
    TomaKing3D_LogSplitDivisor,
    TomaKing3D_LogSkipMarker,
    # AUFGABE 3D - Logging
    TomaKing3D_LogHeaderTemplate,
    TomaKing3D_LogStepTemplate,
    TomaKing3D_LogSkipLine,
    TomaKing3D_LogPathTemplate,
    TomaKing3D_LogCostTemplate,
    TomaKing3D_LogExpansionsTemplate,
    TomaKing3D_LogNoPathTemplate,
)

## =============================================================================
# ================== AUFGABE 3D - HEURISTIK (MANHATTAN & BFS) ===================
## =============================================================================

# Aktueller Heuristik-Modus (None = Config-Default). Erlaubt Demo-Umschaltung.
_heuristic_override = None
# Setzt den Heuristik-Modus temporär (nur für Demo-Zwecke).
def _set_heuristic_mode(mode: str) -> None:
    global _heuristic_override
    _heuristic_override = mode
# Liefert den aktiven Heuristik-Modus.
def _current_heuristic_mode() -> str:
    return _heuristic_override if _heuristic_override is not None else TomaKing3D_HeuristicMode
# Manhattan-Heuristik (lose, aber zulässig; kennt keine Wände).
def _heuristic_manhattan(graph, node, goal, agent_speed) -> float:
    return manhattan(node, goal) * (TomaKing3A_BaseCost / agent_speed)
# BFS-Heuristik (strammer; kennt Wandtopologie via BFS-Distanz).
def _heuristic_bfs(graph, node, goal, agent_speed) -> float:
    dist = graph.get_bfs_distance(node, goal)
    return dist * (TomaKing3A_BaseCost / agent_speed)
# Dispatcher: wählt die Heuristik anhand des aktiven Modus.
def _heuristic(graph, node, goal, agent_speed) -> float:
    if _current_heuristic_mode() == TomaKing3D_ModeBFS:
        return _heuristic_bfs(graph, node, goal, agent_speed)
    return _heuristic_manhattan(graph, node, goal, agent_speed)

## =============================================================================
# ============================ AUFGABE 3B - A*-SUCHE ============================
## =============================================================================

# Rekonstruiert den Pfad rückwärts über das came_from-Dictionary.
def _reconstruct_path(came_from: dict, current: tuple) -> list:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
# Führt die A*-Suche auf dem Graphen aus. Liefert (Pfad, Kosten, Schritte).
def a_star(graph, start, goal, agent_speed):
    h_start = _heuristic(graph, start, goal, agent_speed) # 3D
    open_list = [(h_start, TomaKing3B_InitialCost, start)]
    came_from = {}
    g_score = {start: TomaKing3B_InitialCost}
    closed_set = set()
    steps = []
    while open_list:
        f, g, current = heapq.heappop(open_list)
        if current in closed_set:
            continue
        closed_set.add(current)
        steps.append((current, f, g, len(open_list), len(closed_set)))
        if current == goal:
            path = _reconstruct_path(came_from, current)
            return path, g, steps
        for neighbor in graph.get_neighbors(current[0], current[1]):
            tentative_g = g + graph.get_edge_cost(current, neighbor, agent_speed)
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                h = _heuristic(graph, neighbor, goal, agent_speed) # 3D
                heapq.heappush(open_list, (tentative_g + h, tentative_g, neighbor))
    return None, None, steps

## =============================================================================
# ============ AUFGABE 3D - DEMO-TESTLAUF (HEURISTIK-VERGLEICH) =================
## =============================================================================

# Wählt bis zu TomaKing3D_LogMaxSteps repräsentative Schritte (Anfang + Ende).
def _select_steps(steps: list) -> list:
    total = len(steps)
    if total <= TomaKing3D_LogMaxSteps:
        return list(enumerate(steps, start=TomaKing3D_LogStartIndex))
    half = TomaKing3D_LogMaxSteps // TomaKing3D_LogSplitDivisor
    first = list(enumerate(steps[:half], start=TomaKing3D_LogStartIndex))
    last_start = total - (TomaKing3D_LogMaxSteps - half) + TomaKing3D_LogStartIndex
    last = [(i, steps[i - TomaKing3D_LogStartIndex]) for i in range(last_start, total + TomaKing3D_LogStartIndex)]
    return first + [TomaKing3D_LogSkipMarker] + last
# Gibt einen reduzierten A*-Lauf mit Heuristik-Kennzeichnung aus.
def _log_run(mode, start, goal, agent_speed, path, cost, steps) -> None:
    sep = TomaKingGUI_LogSeparatorCharLine * TomaKingGUI_LogSeparatorLength
    print(TomaKing3D_LogHeaderTemplate.format(mode, start, goal, agent_speed))
    print(sep)
    for item in _select_steps(steps):
        if item is TomaKing3D_LogSkipMarker:
            print(TomaKing3D_LogSkipLine)
            continue
        idx, (node, f, g, open_count, closed_count) = item
        print(TomaKing3D_LogStepTemplate.format(idx, node, f, g, open_count, closed_count))
    print(sep)
    if path is not None:
        print(TomaKing3D_LogPathTemplate.format(len(path), path))
        print(TomaKing3D_LogCostTemplate.format(cost))
        print(TomaKing3D_LogExpansionsTemplate.format(len(steps)))
    else:
        print(TomaKing3D_LogNoPathTemplate)
    print(sep)
# main-Block initialisierung
if __name__ == "__main__":
    from map import Map
    from graph import Graph
    map_instance = Map()
    graph = Graph(map_instance)
    for mode in (TomaKing3D_ModeManhattan, TomaKing3D_ModeBFS):
        _set_heuristic_mode(mode)
        path, cost, steps = a_star(graph, TomaKing3D_DemoStart, TomaKing3D_DemoGoal,
                                   TomaKing3D_DemoAgentSpeed)
        _log_run(mode, TomaKing3D_DemoStart, TomaKing3D_DemoGoal,
                 TomaKing3D_DemoAgentSpeed, path, cost, steps)