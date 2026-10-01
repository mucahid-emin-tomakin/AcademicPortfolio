# !/usr/bin/env python
# -*- coding: utf-8 -*-
# simulation.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import random
from config import (
    # GUI - Logging
    TomaKingGUI_LogSeparatorCharLine,
    TomaKingGUI_LogSeparatorLength,
    # AUFGABE 1C - Seed
    TomaKing1C_Seed,
    # AUFGABE 1C - Batterie
    TomaKing1C_BatteryMoveBase,
    TomaKing1C_BatteryStandstill,
    # AUFGABE 1C - Step-Log-Format
    TomaKing1C_LogStepHeaderTemplate,
    # AUFGABE 1C - Message
    TomaKing1C_MessageInterval,
    TomaKing1C_MessageTypeTest,
)

## =============================================================================
# ======================== AUFGABE 1C - SIMULATION CLASS ========================
## =============================================================================

class Simulation:
    # Initialisiert die Simulation mit Karte, Agenten, Nachrichten-Bus und Step-Zähler.
    def __init__(self, map_instance, agents: list, depots: list): # 2A
        self.map = map_instance
        self.agents = agents
        self.depots = depots # 2A
        self.message_bus: list = []
        self.step_count = 0
        self._event_log: list = []
        random.seed(TomaKing1C_Seed)
    # Nimmt ein Event vom Agenten entgegen und puffert es für die Step-Ausgabe.
    def log_event(self, message: str) -> None:
        self._event_log.append(message)
    # Gibt den Agenten mit der angegebenen ID zurück (oder None). # 2A
    def get_agent_by_id(self, agent_id: int):
        for agent in self.agents:
            if agent.agent_id == agent_id:
                return agent
        return None

## =============================================================================
# ======================= AUFGABE 1C - NACHRICHTEN-BUS ==========================
## =============================================================================

    # Legt eine neue Nachricht auf den Bus.
    def send_message(self, message) -> None:
        self.message_bus.append(message)
    # Liest alle Nachrichten für einen Agenten aus dem Bus und entfernt sie.
    def read_messages_for(self, agent_id: int) -> list:
        received = [m for m in self.message_bus if m.receiver_id == agent_id]
        self.message_bus = [m for m in self.message_bus if m.receiver_id != agent_id]
        return received

## =============================================================================
# ========================= AUFGABE 1C - HAUPTSCHLEIFE ==========================
## =============================================================================

    # Führt einen Simulationsschritt aus.
    def step(self) -> None:
        self._event_log = []
        prev_positions = {a.agent_id: a.get_position() for a in self.agents}
        for agent in self.agents:
            self._agent_step(agent)
        self._resolve_collisions(prev_positions)
        self.step_count += 1
        self._log_step()
    # Führt die Handlungen eines einzelnen Agenten für einen Schritt aus.
    def _agent_step(self, agent) -> None:
        agent.read_messages(self)
        if self.step_count % TomaKing1C_MessageInterval == 0:
            self._dispatch_message(agent)
        if agent.battery <= 0:
            return
        for _ in range(agent.speed):
            if agent.battery <= 0:
                break
            dx, dy = agent.decide_action(self.map)
            if agent.try_move(self.map, dx, dy):
                agent.battery -= (TomaKing1C_BatteryMoveBase + agent.cargo)
            else:
                agent.battery -= TomaKing1C_BatteryStandstill
    # Sendet eine Testnachricht an einen zufälligen anderen Agenten.
    def _dispatch_message(self, agent) -> None:
        others = [a for a in self.agents if a.agent_id != agent.agent_id]
        if not others:
            return
        receiver = random.choice(others)
        agent.send_message(self, TomaKing1C_MessageTypeTest, receiver.agent_id)

## =============================================================================
# ====================== AUFGABE 1C - KOLLISIONS-AUFLÖSUNG ======================
## =============================================================================

    # Setzt alle Agenten, die auf derselben Zelle stehen, auf ihre Vorposition zurück.
    def _resolve_collisions(self, prev_positions: dict) -> None:
        pos_count: dict = {}
        for agent in self.agents:
            pos = agent.get_position()
            pos_count[pos] = pos_count.get(pos, 0) + 1
        for agent in self.agents:
            if pos_count[agent.get_position()] > 1:
                px, py = prev_positions[agent.agent_id]
                agent.x, agent.y = px, py

## =============================================================================
# ========================= AUFGABE 1C - STEP-LOGGING ===========================
## =============================================================================

    # Protokolliert den aktuellen Schritt (Header, Agentenliste, Trennlinien).
    def _log_step(self) -> None:
        header = TomaKing1C_LogStepHeaderTemplate.format(self.step_count)
        print(header.center(TomaKingGUI_LogSeparatorLength))
        print(TomaKingGUI_LogSeparatorCharLine * TomaKingGUI_LogSeparatorLength)
        if self._event_log:
            for event in self._event_log:
                print(event)
            print(TomaKingGUI_LogSeparatorCharLine * TomaKingGUI_LogSeparatorLength)
        for agent in self.agents:
            print(agent.to_string())
        print(TomaKingGUI_LogSeparatorCharLine * TomaKingGUI_LogSeparatorLength)