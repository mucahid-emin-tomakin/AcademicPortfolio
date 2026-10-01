# !/usr/bin/env python
# -*- coding: utf-8 -*-
# depot.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

from message import Message
from config import (
    # AUFGABE 1C - Logging
    TomaKing1C_LogSendTemplate,
    TomaKing1C_LogReadTemplate,
    # AUFGABE 2A - Nachrichtentypen # 2B
    TomaKing2A_MsgAnnounce,
    # AUFGABE 2A - Payload-Schlüssel # 2B
    TomaKing2A_KeyTaskId,
    TomaKing2A_KeyDestination,
    TomaKing2A_KeyDeadline,
    # AUFGABE 2A - Depot-IDs
    TomaKing2A_StartDepotId,
    TomaKing2A_DepotIdStep,
    # AUFGABE 2A - Repr-Template
    TomaKing2A_ReprTemplate,
)

## =============================================================================
# =========================== AUFGABE 2A - DEPOT CLASS ==========================
## =============================================================================

class Depot:
    # Initialisiert ein Depot an einer festen Position.
    def __init__(self, depot_id: int, x: int, y: int):
        self.depot_id = depot_id
        self.x = x
        self.y = y
    # Gibt die Position des Depots als Tupel zurück.
    def get_position(self) -> tuple[int, int]:
        return (self.x, self.y)
    # Liest alle Nachrichten für dieses Depot aus dem Bus (über die Simulation).
    def read_messages(self, simulation) -> list:
        received = simulation.read_messages_for(self.depot_id)
        if received:
            simulation.log_event(
                TomaKing1C_LogReadTemplate.format(self.depot_id, len(received)))
        return received
    # Sendet eine Nachricht über den Simulations-Bus.
    def send_message(self, simulation, msg_type, receiver_id, payload=None) -> Message:
        msg = Message(self.depot_id, receiver_id, msg_type, payload)
        simulation.send_message(msg)
        simulation.log_event(
            TomaKing1C_LogSendTemplate.format(self.depot_id, receiver_id, msg_type))
        return msg
    # Schreibt eine neue Aufgabe aus (Task Announcement) und sendet sie an alle Agenten. # 2B
    def announce_task(self, simulation, package) -> None:
        payload = {
            TomaKing2A_KeyTaskId:      package.package_id,
            TomaKing2A_KeyDestination: package.target,
            TomaKing2A_KeyDeadline:    package.deadline,
        }
        for agent in simulation.agents:
            self.send_message(simulation, TomaKing2A_MsgAnnounce, agent.agent_id, payload)
    # Wird von print() verwendet.
    def __str__(self) -> str:
        return TomaKing2A_ReprTemplate.format(self.depot_id, self.x, self.y)
    # Eindeutige Repräsentation für Debugging.
    def __repr__(self) -> str:
        return TomaKing2A_ReprTemplate.format(self.depot_id, self.x, self.y)

## =============================================================================
# ========================= AUFGABE 2A - DEPOT-FABRIK ===========================
## =============================================================================

# Erzeugt alle Depots aus den von der Karte gelieferten Positionen.
def create_depots(map_instance) -> list[Depot]:
    positions = map_instance.get_depots()
    depots: list[Depot] = []
    depot_id = TomaKing2A_StartDepotId
    for (x, y) in positions:
        depots.append(Depot(depot_id, x, y))
        depot_id += TomaKing2A_DepotIdStep
    return depots