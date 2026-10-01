# !/usr/bin/env python
# -*- coding: utf-8 -*-
# prolog.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

from pathlib import Path
from query import run_goal_with_consult, is_true, is_false, parse_int_list # 4C
from config import (
    # GUI - Logging
    TomaKingGUI_LogSeparatorCharEqual,
    TomaKingGUI_LogSeparatorLength,
    # AUFGABE 1A - Karten-Symbole und -Richtungen
    TomaKing1A_Wall,
    TomaKing1A_Directions,
    # AUFGABE 2A - Depot-IDs
    TomaKing2A_StartDepotId,
    TomaKing2A_DepotIdStep,
    # AUFGABE 3A - Kosten-Modell
    TomaKing3A_BaseCost,
    TomaKing3A_BottleneckMaxNeighbors,
    TomaKing3A_BottleneckPenalty,
    # AUFGABE 4A - Wissensbasis-Datei
    TomaKing4A_FactsPath,
    # AUFGABE 4A - Ziel-IDs
    TomaKing4A_StartTargetId,
    TomaKing4A_TargetIdStep,
    # AUFGABE 4A - Datei-Header
    TomaKing4A_ShebangLine,
    TomaKing4A_ModeLine,
    TomaKing4A_FactsTitle,
    TomaKing4A_FactsFilename,
    TomaKing4A_SeparatorLineTemplate,
    TomaKing4A_TitleLineTemplate,
    TomaKing4A_FilenameLineTemplate,
    # AUFGABE 4A - Abschnitts-Header
    TomaKing4A_HeaderDirections,
    TomaKing4A_HeaderCostParameters,
    TomaKing4A_HeaderRoad,
    TomaKing4A_HeaderWall,
    TomaKing4A_HeaderDepot,
    TomaKing4A_HeaderTarget,
    # AUFGABE 4A - Fakten-Templates
    TomaKing4A_FactDirectionTemplate,
    TomaKing4A_FactBaseCostTemplate,
    TomaKing4A_FactBottleneckPenaltyT,
    TomaKing4A_FactBottleneckMaxNeighborsT,
    TomaKing4A_FactRoadTemplate,
    TomaKing4A_FactWallTemplate,
    TomaKing4A_FactDepotTemplate,
    TomaKing4A_FactTargetTemplate,
    # AUFGABE 4A - Logging
    TomaKing4A_LogExportTemplate,
    TomaKing4A_LogRoadCountTemplate,
    TomaKing4A_LogWallCountTemplate,
    TomaKing4A_LogDepotCountTemplate,
    TomaKing4A_LogTargetCountTemplate,
    # AUFGABE 4C - Dateien # 4C
    TomaKing4C_AgentsPath,
    # AUFGABE 4C - PROLOG-Goal-Templates # 4C
    TomaKing4C_GoalReachableTemplate,
    TomaKing4C_GoalCandidatesTemplate,
    TomaKing4C_FactAgentTemplate,
    # AUFGABE 4C - Logging # 4C
    TomaKing4C_LogExportAgentsTemplate,
)

## =============================================================================
# ==================== AUFGABE 4A - PROLOG-FAKTEN-GENERATOR =====================
## =============================================================================

# Projekt-Root unabhängig vom aktuellen Arbeitsverzeichnis.
_PROJECT_ROOT = Path(__file__).resolve().parent
# Erzeugt den vollständigen Fakten-Text der PROLOG-Wissensbasis aus der Karte.
def build_facts(map_instance) -> str:
    sep_line = TomaKingGUI_LogSeparatorCharEqual * TomaKingGUI_LogSeparatorLength
    title_line = TomaKing4A_FactsTitle.center(
        TomaKingGUI_LogSeparatorLength,
        TomaKingGUI_LogSeparatorCharEqual
    )
    lines = []
    lines.append(TomaKing4A_ShebangLine)
    lines.append(TomaKing4A_ModeLine)
    lines.append(TomaKing4A_FilenameLineTemplate.format(TomaKing4A_FactsFilename))
    lines.append("")
    lines.append(TomaKing4A_SeparatorLineTemplate.format(sep_line))
    lines.append(TomaKing4A_TitleLineTemplate.format(title_line))
    lines.append(TomaKing4A_SeparatorLineTemplate.format(sep_line))
    lines.append("")
    lines.append(TomaKing4A_HeaderDirections)
    for (dx, dy) in TomaKing1A_Directions:
        lines.append(TomaKing4A_FactDirectionTemplate.format(dx, dy))
    lines.append(TomaKing4A_HeaderCostParameters)
    lines.append(TomaKing4A_FactBaseCostTemplate.format(TomaKing3A_BaseCost))
    lines.append(TomaKing4A_FactBottleneckPenaltyT.format(TomaKing3A_BottleneckPenalty))
    lines.append(TomaKing4A_FactBottleneckMaxNeighborsT.format(TomaKing3A_BottleneckMaxNeighbors))
    lines.append(TomaKing4A_HeaderRoad)
    road_count = 0
    for y in range(map_instance.height):
        for x in range(map_instance.width):
            if map_instance.get_cell(x, y) != TomaKing1A_Wall:
                lines.append(TomaKing4A_FactRoadTemplate.format(x, y))
                road_count += 1
    lines.append(TomaKing4A_HeaderWall)
    wall_count = 0
    for y in range(map_instance.height):
        for x in range(map_instance.width):
            if map_instance.get_cell(x, y) == TomaKing1A_Wall:
                lines.append(TomaKing4A_FactWallTemplate.format(x, y))
                wall_count += 1
    lines.append(TomaKing4A_HeaderDepot)
    depot_count = 0
    depot_id = TomaKing2A_StartDepotId
    for (x, y) in map_instance.get_depots():
        lines.append(TomaKing4A_FactDepotTemplate.format(depot_id, x, y))
        depot_id += TomaKing2A_DepotIdStep
        depot_count += 1
    lines.append(TomaKing4A_HeaderTarget)
    target_count = 0
    target_id = TomaKing4A_StartTargetId
    for (x, y) in map_instance.get_targets():
        lines.append(TomaKing4A_FactTargetTemplate.format(target_id, x, y))
        target_id += TomaKing4A_TargetIdStep
        target_count += 1
    return "\n".join(lines), road_count, wall_count, depot_count, target_count
# Schreibt die Fakten als .pl-Datei und gibt Zählungen auf der Konsole aus.
def export_facts(map_instance) -> None:
    content, road_count, wall_count, depot_count, target_count = build_facts(map_instance)
    facts_path = _PROJECT_ROOT / TomaKing4A_FactsPath
    with open(facts_path, "w", encoding="utf-8") as file:
        file.write(content)
    line_count = content.count("\n") + 1
    print(TomaKingGUI_LogSeparatorCharEqual * TomaKingGUI_LogSeparatorLength)
    print(TomaKing4A_LogExportTemplate.format(TomaKing4A_FactsPath, line_count))
    print(TomaKing4A_LogRoadCountTemplate.format(road_count))
    print(TomaKing4A_LogWallCountTemplate.format(wall_count))
    print(TomaKing4A_LogDepotCountTemplate.format(depot_count))
    print(TomaKing4A_LogTargetCountTemplate.format(target_count))

## =============================================================================
# ==================== AUFGABE 4C - AGENTEN-EXPORT ==============================
## =============================================================================

# Schreibt die aktuellen Agentendaten als PROLOG-Fakten nach agents.pl.
def export_agents(agents) -> int:
    lines = []
    for agent in agents:
        x, y = agent.get_position()
        lines.append(TomaKing4C_FactAgentTemplate.format(
            agent.agent_id, x, y, agent.speed,
            agent.capacity, agent.battery, agent.cargo))
    content = "\n".join(lines)
    path = _PROJECT_ROOT / TomaKing4C_AgentsPath
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    return len(agents)

## =============================================================================
# ==================== AUFGABE 4C - PROLOG-ABFRAGEN =============================
## =============================================================================

# Prueft via PROLOG, ob zwei Positionen verbunden sind.
def query_reachable(from_pos, to_pos) -> bool:
    goal = TomaKing4C_GoalReachableTemplate.format(
        from_pos[0], from_pos[1], to_pos[0], to_pos[1])
    answer = run_goal_with_consult(goal)
    if answer is None:
        return True
    if is_true(answer):
        return True
    if is_false(answer):
        return False
    return True
# Liefert die Liste aller fuer eine Aufgabe geeigneten Agenten.
def query_candidate_agents(depot_pos, target_pos, all_agent_ids) -> list[int]:
    goal = TomaKing4C_GoalCandidatesTemplate.format(
        depot_pos[0], depot_pos[1], target_pos[0], target_pos[1])
    answer = run_goal_with_consult(goal)
    if answer is None:
        return all_agent_ids
    try:
        return parse_int_list(answer)
    except ValueError:
        return all_agent_ids