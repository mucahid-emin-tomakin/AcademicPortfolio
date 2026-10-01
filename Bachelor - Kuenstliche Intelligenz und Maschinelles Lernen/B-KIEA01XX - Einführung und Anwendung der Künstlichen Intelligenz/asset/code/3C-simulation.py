# !/usr/bin/env python
# -*- coding: utf-8 -*-
# simulation.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import random
from package import create_package # 2B
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
    # AUFGABE 2B - Parameter
    TomaKing2B_PackageInterval,
    TomaKing2B_DeadlineDefault,
    # AUFGABE 2B - Package-IDs
    TomaKing2B_StartPackageId,
    TomaKing2B_PackageIdStep,
    # AUFGABE 2B - Logging
    TomaKing2B_LogGenerationTemplate,
    # AUFGABE 2B - Error Handling
    TomaKing2B_ErrorNoDepots,
    TomaKing2B_ErrorNoTargets,
)

## =============================================================================
# ======================== AUFGABE 1C - SIMULATION CLASS ========================
## =============================================================================

class Simulation:
    # Initialisiert die Simulation mit Karte, Agenten, Nachrichten-Bus und Step-Zähler.
    def __init__(self, map_instance, agents: list, depots: list, graph): # 2A # 3C
        self.graph = graph # 3C
        self.map = map_instance
        self.agents = agents
        self.depots = depots # 2A
        self.packages: list = [] # 2B
        self._next_package_id = TomaKing2B_StartPackageId # 2B
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
    # Gibt das Depot mit der angegebenen ID zurück (oder None). # 2C
    def get_depot_by_id(self, depot_id: int):
        for depot in self.depots:
            if depot.depot_id == depot_id:
                return depot
        return None
    # Gibt das Paket mit der angegebenen ID zurück (oder None). # 2D
    def get_package_by_id(self, package_id: int):
        for package in self.packages:
            if package.package_id == package_id:
                return package
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
        self.step_count += 1
        if self.step_count % TomaKing2B_PackageInterval == 0: # 2B
            self._generate_package() # 2B
        prev_positions = {a.agent_id: a.get_position() for a in self.agents}
        for agent in self.agents:
            self._agent_step(agent)
        self._resolve_collisions(prev_positions)
        for depot in self.depots: # 2C
            depot.read_messages(self) # 2C
        for depot in self.depots: # 2D
            depot.process_bids(self) # 2D
        self._log_step()
    # Führt die Handlungen eines einzelnen Agenten für einen Schritt aus.
    def _agent_step(self, agent) -> None:
        agent.read_messages(self)
        agent.process_announcements(self) # 2C
        if agent.battery <= 0:
            return
        for _ in range(agent.speed):
            if agent.battery <= 0:
                break
            dx, dy = agent.decide_action(self.map, self) # 3C
            if (dx, dy) == (0, 0): # 3C
                break # 3C
            if agent.try_move(self.map, dx, dy):
                agent._advance_along_route(self) # 3C
                agent.battery -= (TomaKing1C_BatteryMoveBase + agent.cargo)
            else:
                agent.battery -= TomaKing1C_BatteryStandstill

## =============================================================================
# ====================== AUFGABE 2B - PAKETGENERIERUNG ==========================
## =============================================================================

    # Erzeugt neues Paket an Depot mit zufälligem Ziel -> ANNOUNCE-Nachricht an alle Agenten
    def _generate_package(self) -> None:
        if not self.depots:
            raise ValueError(TomaKing2B_ErrorNoDepots)
        targets = self.map.get_targets()
        if not targets:
            raise ValueError(TomaKing2B_ErrorNoTargets)
        depot  = random.choice(self.depots)
        target = random.choice(targets)
        package = create_package(
            self._next_package_id,
            depot.get_position(),
            target,
            self.step_count,
            self.step_count + TomaKing2B_DeadlineDefault,
        )
        self.packages.append(package)
        self._next_package_id += TomaKing2B_PackageIdStep
        self.log_event(TomaKing2B_LogGenerationTemplate.format(
            package.package_id, package.depot,
            package.target, package.deadline))
        depot.announce_task(self, package)

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
                agent._replan(self) # 3C

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