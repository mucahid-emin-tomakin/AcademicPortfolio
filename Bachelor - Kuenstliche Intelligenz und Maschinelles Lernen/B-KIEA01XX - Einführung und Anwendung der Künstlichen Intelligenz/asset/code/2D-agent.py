# !/usr/bin/env python
# -*- coding: utf-8 -*-
# agent.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import random
from message import Message # 1C
from geometry import manhattan # 2C
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
    def try_move(self, map_instance, dx: int, dy: int) -> bool:
        nx, ny = self.x + dx, self.y + dy
        if map_instance.is_walkable(nx, ny):
            self.x, self.y = nx, ny
            return True
        return False
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
    # Kapselt die Planung der nächsten Aktion (in 1c: zufällige Richtung). # 1C
    def decide_action(self, map_instance) -> tuple:
        return random.choice(TomaKing1A_Directions)
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
# ======================= AUFGABE 1B - AGENT-FABRIK =============================
## =============================================================================

# Erzeugt alle Agenten an zufälligen, unterschiedlichen freien Zellen der übergebenen Karte.
def create_agents(map_instance) -> list[Agent]:
    total = TomaKing1B_CountStandard + TomaKing1B_CountExpress
    free_cells = map_instance.get_free_cells()
    if len(free_cells) < total:
        raise ValueError(TomaKing1B_ErrorNotEnoughCellsForAgents.format(total))
    random.seed(TomaKing1B_Seed)
    selected = random.sample(free_cells, total)
    agents: list[Agent] = []
    standard_cells = selected[:TomaKing1B_CountStandard]
    for aid, (x, y) in enumerate(standard_cells, start=TomaKing1B_StartAgentId):
        agents.append(Agent(aid, TomaKing1B_TypeStandard, x, y))
    express_start = TomaKing1B_StartAgentId + TomaKing1B_CountStandard
    express_cells = selected[TomaKing1B_CountStandard:total]
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