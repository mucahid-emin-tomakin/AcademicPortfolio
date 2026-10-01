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
    # AUFGABE 3B - Demo
    TomaKing3B_DemoStart,
    TomaKing3B_DemoGoal,
    TomaKing3B_DemoAgentSpeed,
    TomaKing3B_LogMaxSteps,
    # AUFGABE 3B - Algorithmus
    TomaKing3B_InitialCost,
    TomaKing3B_LogStartIndex,
    TomaKing3B_LogSplitDivisor,
    TomaKing3B_LogSkipMarker,
    # AUFGABE 3B - Logging
    TomaKing3B_LogStartTemplate,
    TomaKing3B_LogStepTemplate,
    TomaKing3B_LogSkipLine,
    TomaKing3B_LogPathTemplate,
    TomaKing3B_LogCostTemplate,
    TomaKing3B_LogNoPathTemplate,
)

## =============================================================================
# ============================ AUFGABE 3B - A*-SUCHE ============================
## =============================================================================

# Berechnet die zulässige Heuristik (Manhattan-Distanz x minimale Kantenkosten).
def _heuristic(node, goal, agent_speed) -> float:
    return manhattan(node, goal) * (TomaKing3A_BaseCost / agent_speed)
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
    h_start = _heuristic(start, goal, agent_speed)
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
                h = _heuristic(neighbor, goal, agent_speed)
                heapq.heappush(open_list, (tentative_g + h, tentative_g, neighbor))
    return None, None, steps

## =============================================================================
# ========================= AUFGABE 3B - LOG-AUSGABE ============================
## =============================================================================

# Wählt bis zu TomaKing3B_LogMaxSteps repräsentative Schritte (Anfang + Ende).
def _select_steps(steps: list) -> list:
    total = len(steps)
    if total <= TomaKing3B_LogMaxSteps:
        return list(enumerate(steps, start=TomaKing3B_LogStartIndex))
    half = TomaKing3B_LogMaxSteps // TomaKing3B_LogSplitDivisor
    first = list(enumerate(steps[:half], start=TomaKing3B_LogStartIndex))
    last_start = total - (TomaKing3B_LogMaxSteps - half) + TomaKing3B_LogStartIndex
    last = [(i, steps[i - TomaKing3B_LogStartIndex]) for i in range(last_start, total + TomaKing3B_LogStartIndex)]
    return first + [TomaKing3B_LogSkipMarker] + last
# Gibt einen reduzierten A*-Lauf auf der Konsole aus.
def log_run(start, goal, agent_speed, path, cost, steps) -> None:
    sep = TomaKingGUI_LogSeparatorCharLine * TomaKingGUI_LogSeparatorLength
    print(sep)
    print(TomaKing3B_LogStartTemplate.format(start, goal, agent_speed))
    print(sep)
    for item in _select_steps(steps):
        if item is TomaKing3B_LogSkipMarker:
            print(TomaKing3B_LogSkipLine)
            continue
        idx, (node, f, g, open_count, closed_count) = item
        print(TomaKing3B_LogStepTemplate.format(idx, node, f, g, open_count, closed_count))
    print(sep)
    if path is not None:
        print(TomaKing3B_LogPathTemplate.format(len(path), path))
        print(TomaKing3B_LogCostTemplate.format(cost))
    else:
        print(TomaKing3B_LogNoPathTemplate)
    print(sep)

## =============================================================================
# ========================= AUFGABE 3B - DEMO-TESTLAUF ==========================
## =============================================================================

if __name__ == "__main__":
    from map import Map
    from graph import Graph
    map_instance = Map()
    graph = Graph(map_instance)
    path, cost, steps = a_star(graph, TomaKing3B_DemoStart, TomaKing3B_DemoGoal, TomaKing3B_DemoAgentSpeed)
    log_run(TomaKing3B_DemoStart, TomaKing3B_DemoGoal, TomaKing3B_DemoAgentSpeed, path, cost, steps)