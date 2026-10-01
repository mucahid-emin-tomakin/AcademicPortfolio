# !/usr/bin/env python
# -*- coding: utf-8 -*-
# agent.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import random
import time # 5B
from message import Message # 1C
from geometry import manhattan # 2C
from astar import a_star # 3C
from config import (
    # GUI - Logging
    TomaKingGUI_LogSeparatorCharEqual,
    TomaKingGUI_LogSeparatorCharLine,
    TomaKingGUI_LogSeparatorLength,
    # AUFGABE 1A - Parameter # 1C
    TomaKing1A_Directions, # 1C
    # AUFGABE 1B - Agententypen
    TomaKing1B_TypeStandard,
    TomaKing1B_TypeExpress,
    # AUFGABE 1B - Agenten-ID-Vergabe
    TomaKing1B_StartAgentId,
    # AUFGABE 1B - Anzahl
    TomaKing1B_CountStandard,
    TomaKing1B_CountExpress,
    TomaKing1B_Seed,
    # AUFGABE 1B - Geschwindigkeit
    TomaKing1B_SpeedStandard,
    TomaKing1B_SpeedExpress,
    # AUFGABE 1B - Kapazität
    TomaKing1B_CapacityStandard,
    TomaKing1B_CapacityExpress,
    TomaKing1B_InitialCargo,
    # AUFGABE 1B - Batteriestand
    TomaKing1B_BatteryStandard,
    TomaKing1B_BatteryExpress,
    # AUFGABE 1B - Statistics
    TomaKing1B_StatKeyAgentCount,
    TomaKing1B_StatKeyStandardCount,
    TomaKing1B_StatKeyExpressCount,
    TomaKing1B_StatKeyAgents,
    # AUFGABE 1B - Repr-Template
    TomaKing1B_ReprTemplate,
    # AUFGABE 1B - Logging
    TomaKing1B_LogColumnFormat,
    TomaKing1B_LogAgentsHeaderLabels,
    TomaKing1B_LogAgentPosition,
    TomaKing1B_LogAgentBattery,
    # AUFGABE 1B - Error Handling
    TomaKing1B_ErrorUnknownType,
    TomaKing1B_ErrorNotEnoughCellsForAgents,
    # AUFGABE 1C - Logging
    TomaKing1C_LogReadTemplate, # 1C
    TomaKing1C_LogPickUpTemplate, # 1C
    TomaKing1C_LogDeliverTemplate, # 1C
    # AUFGABE 2A - Nachrichtentypen
    TomaKing2A_MsgAnnounce, # 2C
    TomaKing2A_MsgBid, # 2C
    TomaKing2A_MsgAward, # 2D
    # AUFGABE 2A - Payload-Schlüssel
    TomaKing2A_KeyTaskId, # 2C
    TomaKing2A_KeyDestination, # 2C
    TomaKing2A_KeyAgentId, # 2C
    TomaKing2A_KeyCost, # 2C
    # AUFGABE 2A - Log-Templates
    TomaKing2A_LogBidTemplate, # 2C
    # AUFGABE 2C - Log-Warnungen
    TomaKing2C_LogUnknownDepot, # 2C
    # AUFGABE 3C - Phasen
    TomaKing3C_PhaseToDepot, # 3C
    TomaKing3C_PhaseToTarget, # 3C
    # AUFGABE 3C - Logging
    TomaKing3C_LogPlanDepotTemplate, # 3C
    TomaKing3C_LogPlanTargetTemplate, # 3C
    TomaKing3C_LogReplanTemplate, # 3C
    TomaKing3C_LogNoPathTemplate, # 3C
    TomaKing3C_LogTaskCompleteTemplate, # 3C
    # AUFGABE 5B - Zeiteinheiten
    TomaKing5B_MsPerSecond, # 5B
)

## =============================================================================
# ========================= AUFGABE 1B - AGENT CLASS ============================
## =============================================================================

class Agent:
    # Initialisiert einen Agenten mit Typ-spezifischen Eigenschaften aus dem Profil-Lookup.
    def __init__(self, agent_id: int, agent_type: str, x: int, y: int):
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.x = x
        self.y = y
        if agent_type == TomaKing1B_TypeStandard:
            self.speed    = TomaKing1B_SpeedStandard
            self.capacity = TomaKing1B_CapacityStandard
            self.battery  = TomaKing1B_BatteryStandard
        elif agent_type == TomaKing1B_TypeExpress:
            self.speed    = TomaKing1B_SpeedExpress
            self.capacity = TomaKing1B_CapacityExpress
            self.battery  = TomaKing1B_BatteryExpress
        else:
            raise ValueError(TomaKing1B_ErrorUnknownType.format(agent_type))
        self.battery_max = self.battery
        self.cargo = TomaKing1B_InitialCargo
        self.pending_announcements: list = [] # 2C
        self.assigned_tasks: list = [] # 2D
        self.current_route: list = [] # 3C
        self.task_phase: str | None = None # 3C
        self.current_task_id: int | None = None # 3C
        self.path_length_current_task = 0 # 5A
        self.path_length_total = 0 # 5A
    # Gibt die aktuelle Position als Tupel zurück.
    def get_position(self) -> tuple[int, int]:
        return (self.x, self.y)
    # Erzeugt eine kompakte String-Repräsentation des Agenten.
    def to_string(self) -> str:
        position = TomaKing1B_LogAgentPosition.format(self.x, self.y)
        battery  = TomaKing1B_LogAgentBattery.format(self.battery, self.battery_max)
        return TomaKing1B_LogColumnFormat.format(
            self.agent_id, self.agent_type, position,
            self.speed, self.capacity, battery, self.cargo
        )
    # Wird von print() verwendet.
    def __str__(self) -> str:
        return self.to_string()
    # Eindeutige Repräsentation für Debugging.
    def __repr__(self) -> str:
        return TomaKing1B_ReprTemplate.format(
            self.agent_id, self.agent_type, self.x, self.y
        )
    # Versucht, sich um (dx, dy) zu bewegen. Gibt True zurück, wenn erfolgreich. # 1C
    def try_move(self, map_instance, dx: int, dy: int, simulation=None) -> bool: # 5A
        nx, ny = self.x + dx, self.y + dy
        if not map_instance.is_walkable(nx, ny): # 5A
            return False # 5A
        if simulation is not None: # 5A
            for other in simulation.agents: # 5A
                if other.agent_id != self.agent_id and other.get_position() == (nx, ny): # 5A
                    simulation.record_collision(self.agent_id, (nx, ny)) # 5D
                    return False
        self.x, self.y = nx, ny
        self.path_length_current_task += 1 # 5A
        self.path_length_total += 1 # 5A
        return True
    # Liest alle Nachrichten für diesen Agenten aus dem Bus (über die Simulation). # 1C
    def read_messages(self, simulation) -> list:
        received = simulation.read_messages_for(self.agent_id)
        if received:
            simulation.log_event(
                TomaKing1C_LogReadTemplate.format(self.agent_id, len(received)))
        for msg in received: # 2C
            if msg.msg_type == TomaKing2A_MsgAnnounce: # 2C
                self.pending_announcements.append(msg) # 2C
            elif msg.msg_type == TomaKing2A_MsgAward: # 2D
                self.assigned_tasks.append(msg.payload[TomaKing2A_KeyTaskId]) # 2D
        return received
    # Sendet eine Nachricht an einen anderen Agenten über den Simulations-Bus. # 1C
    def send_message(self, simulation, msg_type, receiver_id, payload=None) -> Message:
        msg = Message(self.agent_id, receiver_id, msg_type, payload)
        simulation.send_message(msg)  # 2C (Log entfernt)
        return msg
    # Kapselt die Planung der nächsten Aktion (# 1c: zufällige Richtung) (# 3C: Routenverfolgung via A*)
    def decide_action(self, map_instance, simulation) -> tuple: # 3C
        if self.task_phase is None and self.assigned_tasks: # 3C
            self._try_start_next_task(simulation) # 3C
        if len(self.current_route) < 2: # 5A
            return (0, 0) # 5A
        if not self.current_route: # 3C
            return (0, 0) # 3C
        if self._is_next_cell_blocked(simulation): # 3C
            self._replan(simulation) # 3C
            if not self.current_route: # 3C
                return (0, 0) # 3C
        nx, ny = self.current_route[1] # 3C
        return (nx - self.x, ny - self.y) # 3C
    # Versucht, ein Paket aufzunehmen (Kapazitätsprüfung). # 1C
    def pick_up(self, package, simulation) -> bool:
        if self.cargo + package.size > self.capacity:
            return False
        before = self.cargo
        self.cargo += package.size
        simulation.log_event(TomaKing1C_LogPickUpTemplate.format(
            self.agent_id, package.package_id, before, self.cargo))
        return True
    # Versucht, ein Paket abzuliefern (Ladungsprüfung). # 1C
    def deliver(self, package, simulation) -> bool:
        if self.cargo < package.size:
            return False
        before = self.cargo
        self.cargo -= package.size
        package.mark_delivered(simulation.step_count, self.path_length_current_task) # 5A
        simulation.log_event(TomaKing1C_LogDeliverTemplate.format(
            self.agent_id, package.package_id, before, self.cargo))
        return True
    # Verarbeitet alle gepufferten Announcements und sendet je ein BID pro Aufgabe. # 2C
    def process_announcements(self, simulation) -> None:
        for announce in self.pending_announcements:
            self._bid_for_task(simulation, announce)
        self.pending_announcements = []
    # Sendet ein BID für eine einzelne Announcement-Nachricht. # 2C
    def _bid_for_task(self, simulation, announce) -> None:
        depot = simulation.get_depot_by_id(announce.sender_id)
        if depot is None:
            simulation.log_event(
                TomaKing2C_LogUnknownDepot.format(announce.sender_id))
            return
        depot_pos  = depot.get_position()
        target_pos = announce.payload[TomaKing2A_KeyDestination]
        cost = self._estimate_cost(depot_pos, target_pos)
        payload = {
            TomaKing2A_KeyAgentId: self.agent_id,
            TomaKing2A_KeyTaskId:  announce.payload[TomaKing2A_KeyTaskId],
            TomaKing2A_KeyCost:    cost,
        }
        self.send_message(simulation, TomaKing2A_MsgBid,
                          depot.depot_id, payload)
        simulation.log_event(TomaKing2A_LogBidTemplate.format(
            self.agent_id, depot.depot_id,
            announce.payload[TomaKing2A_KeyTaskId], cost))
    # Schätzt die Kosten für die Bearbeitung einer Aufgabe (Manhattan-Distanz). # 2C
    def _estimate_cost(self, depot_pos, target_pos) -> int:
        return (manhattan(self.get_position(), depot_pos)
                + manhattan(depot_pos, target_pos))

## =============================================================================
# ==================== AUFGABE 3C - ROUTENPLANUNG & TASK ========================
## =============================================================================

    # Startet den nächsten Task aus der FIFO-Liste und plant den Weg zum Depot.
    def _try_start_next_task(self, simulation) -> None:
        task_id = self.assigned_tasks[0]
        package = simulation.get_package_by_id(task_id)
        if package is None:
            self.assigned_tasks.pop(0)
            return
        self.current_task_id = task_id
        self.task_phase = TomaKing3C_PhaseToDepot
        self.path_length_current_task = 0 # 5A
        self._plan(simulation, package.depot, is_depot=True)
    # Plant eine Route zu einem Zielknoten und aktualisiert current_route.
    def _plan(self, simulation, goal: tuple, is_depot: bool) -> None:
        t0 = time.perf_counter() # 5B
        path, cost, steps = a_star(simulation.graph, self.get_position(), goal, self.speed)
        t1 = time.perf_counter() # 5B
        simulation.record_planning( # 5B
            expanded=len(steps), # 5B
            time_ms=(t1 - t0) * TomaKing5B_MsPerSecond, # 5B
            goal=goal, # 5B
            task_id=self.current_task_id, # 5B
        ) # 5B
        if path is None:
            simulation.log_event(TomaKing3C_LogNoPathTemplate.format(
                self.agent_id, goal, self.current_task_id))
            self._abandon_current_task(simulation)
            return
        self.current_route = path
        template = TomaKing3C_LogPlanDepotTemplate if is_depot else TomaKing3C_LogPlanTargetTemplate
        simulation.log_event(template.format(self.agent_id, goal, len(path), cost))
    # Plant von der aktuellen Position neu (nach Kollision oder Blockade).
    def _replan(self, simulation) -> None:
        if self.task_phase is None or self.current_task_id is None:
            return
        package = simulation.get_package_by_id(self.current_task_id)
        if package is None:
            self._abandon_current_task(simulation)
            return
        goal = package.depot if self.task_phase == TomaKing3C_PhaseToDepot else package.target
        simulation.record_replan(self.agent_id, goal) # 5D
        t0 = time.perf_counter() # 5B
        path, cost, steps = a_star(simulation.graph, self.get_position(), goal, self.speed) # 5B
        t1 = time.perf_counter() # 5B
        simulation.record_planning( # 5B
            expanded=len(steps), # 5B
            time_ms=(t1 - t0) * TomaKing5B_MsPerSecond, # 5B
            goal=goal, # 5B
            task_id=self.current_task_id, # 5B
        ) # 5B
        if path is None:
            simulation.log_event(TomaKing3C_LogNoPathTemplate.format(
                self.agent_id, goal, self.current_task_id))
            self._abandon_current_task(simulation)
            return
        if path == self.current_route: # 5A
            return # 5A
        simulation.log_event(TomaKing3C_LogReplanTemplate.format(
            self.agent_id, self.get_position(), goal))
        self.current_route = path
    # Schiebt die Route um eine Position vor und prüft Phasenwechsel (PICKUP / DELIVER).
    def _advance_along_route(self, simulation) -> None:
        if not self.current_route:
            return
        self.current_route.pop(0)
        if self.task_phase is None:
            return
        package = simulation.get_package_by_id(self.current_task_id)
        if package is None:
            self._abandon_current_task(simulation)
            return
        if self.task_phase == TomaKing3C_PhaseToDepot and self.get_position() == package.depot:
            if self.pick_up(package, simulation):
                self.task_phase = TomaKing3C_PhaseToTarget
                self._plan(simulation, package.target, is_depot=False)
        elif self.task_phase == TomaKing3C_PhaseToTarget and self.get_position() == package.target:
            if self.deliver(package, simulation):
                simulation.log_event(TomaKing3C_LogTaskCompleteTemplate.format(
                    self.agent_id, self.current_task_id))
                self._finish_current_task()
    # Prüft, ob die nächste Zelle der Route durch einen anderen Agenten belegt ist.
    def _is_next_cell_blocked(self, simulation) -> bool:
        if len(self.current_route) < 2:
            return False
        next_pos = self.current_route[1]
        for other in simulation.agents:
            if other.agent_id != self.agent_id and other.get_position() == next_pos:
                return True
        return False
    # Schließt den aktuellen Task ab (Task-ID aus der FIFO-Liste entfernen, Zustand zurücksetzen).
    def _finish_current_task(self) -> None:
        if self.current_task_id in self.assigned_tasks:
            self.assigned_tasks.remove(self.current_task_id)
        self.current_task_id = None
        self.task_phase = None
        self.current_route = []
    # Bricht den aktuellen Task ab (z. B. kein Pfad gefunden).
    def _abandon_current_task(self, simulation) -> None:
        if self.current_task_id is not None and self.current_task_id in self.assigned_tasks:
            self.assigned_tasks.remove(self.current_task_id)
        self.current_task_id = None
        self.task_phase = None
        self.current_route = []

## =============================================================================
# ======================= AUFGABE 1B - AGENT-FABRIK =============================
## =============================================================================

# Erzeugt alle Agenten an zufälligen, unterschiedlichen freien Zellen der übergebenen Karte.
def create_agents(map_instance, # 5A
                  n_standard: int = TomaKing1B_CountStandard, # 5A
                  n_express: int = TomaKing1B_CountExpress, # 5A
                  seed: int = TomaKing1B_Seed) -> list[Agent]: # 5A
    total = n_standard + n_express # 5A
    free_cells = map_instance.get_free_cells()
    if len(free_cells) < total:
        raise ValueError(TomaKing1B_ErrorNotEnoughCellsForAgents.format(total))
    random.seed(seed) # 5A
    selected = random.sample(free_cells, total)
    agents: list[Agent] = []
    standard_cells = selected[:n_standard] # 5A
    for aid, (x, y) in enumerate(standard_cells, start=TomaKing1B_StartAgentId):
        agents.append(Agent(aid, TomaKing1B_TypeStandard, x, y))
    express_start = TomaKing1B_StartAgentId + n_standard # 5A
    express_cells = selected[n_standard:total] # 5A
    for aid, (x, y) in enumerate(express_cells, start=express_start):
        agents.append(Agent(aid, TomaKing1B_TypeExpress, x, y))
    _log_agents(agents)
    return agents

## =============================================================================
# =================== AUFGABE 1B - STATISTIKEN & LOGGING =======================
## =============================================================================

# Liefert ein Dictionary mit den Agenten-Kennzahlen für die GUI-Info-Zeile.
def get_agent_statistics(agents: list[Agent]) -> dict:
    standard_count = sum(1 for a in agents if a.agent_type == TomaKing1B_TypeStandard)
    express_count = sum(1 for a in agents if a.agent_type == TomaKing1B_TypeExpress)
    return {
        TomaKing1B_StatKeyAgentCount:    len(agents),
        TomaKing1B_StatKeyStandardCount: standard_count,
        TomaKing1B_StatKeyExpressCount:  express_count,
        TomaKing1B_StatKeyAgents:        agents,
    }
# Gibt alle Agenten mit ihren vollständigen Attributen auf der Konsole aus (einmalig bei Erzeugung).
def _log_agents(agents: list[Agent]) -> None:
    print(TomaKingGUI_LogSeparatorCharEqual * TomaKingGUI_LogSeparatorLength)
    print(TomaKing1B_LogColumnFormat.format(*TomaKing1B_LogAgentsHeaderLabels))
    print(TomaKingGUI_LogSeparatorCharLine * TomaKingGUI_LogSeparatorLength)
    for agent in agents:
        print(agent.to_string())
    print(TomaKingGUI_LogSeparatorCharEqual * TomaKingGUI_LogSeparatorLength)