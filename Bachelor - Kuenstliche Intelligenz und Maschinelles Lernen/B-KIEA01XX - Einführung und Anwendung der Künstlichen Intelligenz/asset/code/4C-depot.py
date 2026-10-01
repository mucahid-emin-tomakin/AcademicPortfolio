# !/usr/bin/env python
# -*- coding: utf-8 -*-
# depot.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

from message import Message
from prolog import query_candidate_agents  # 4C
from config import (
    # AUFGABE 2A - Nachrichtentypen # 2B
    TomaKing2A_MsgAnnounce,
    TomaKing2A_MsgBid, # 2D
    TomaKing2A_MsgAward, # 2D
    # AUFGABE 2A - Payload-Schlüssel # 2B
    TomaKing2A_KeyTaskId,
    TomaKing2A_KeyDestination,
    TomaKing2A_KeyDeadline,
    TomaKing2A_KeyAgentId, # 2D
    TomaKing2A_KeyCost, # 2D
    # AUFGABE 2A - Depot-IDs
    TomaKing2A_StartDepotId,
    TomaKing2A_DepotIdStep,
    # AUFGABE 2A - Repr-Template
    TomaKing2A_ReprTemplate,
    # AUFGABE 2A - Logging # 2C
    TomaKing2A_LogAnnounceTemplate,
    TomaKing2A_LogAwardTemplate, # 2D
    TomaKing2A_LogDepotReadTemplate,
    # AUFGABE 2D - Logging
    TomaKing2D_LogAuctionTemplate,
    TomaKing2D_LogNoBidsTemplate,
    # AUFGABE 4C - Logging  # 4C
    TomaKing4C_LogCandidateQueryT,
    TomaKing4C_LogNoCandidatesTemplate,
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
        self.pending_bids: dict = {} # 2D
    # Gibt die Position des Depots als Tupel zurück.
    def get_position(self) -> tuple[int, int]:
        return (self.x, self.y)
    # Liest alle Nachrichten für dieses Depot aus dem Bus (über die Simulation).
    def read_messages(self, simulation) -> list:
        received = simulation.read_messages_for(self.depot_id)
        if received:
            simulation.log_event(
                TomaKing2A_LogDepotReadTemplate.format(self.depot_id, len(received))) # 2C
        for msg in received: # 2D
            if msg.msg_type == TomaKing2A_MsgBid: # 2D
                task_id = msg.payload[TomaKing2A_KeyTaskId] # 2D
                self.pending_bids.setdefault(task_id, []).append(msg) # 2D
        return received
    # Sendet eine Nachricht über den Simulations-Bus.
    def send_message(self, simulation, msg_type, receiver_id, payload=None) -> Message:
        msg = Message(self.depot_id, receiver_id, msg_type, payload)
        simulation.send_message(msg) # 2C (Log entfernt)
        return msg
    # Schreibt eine neue Aufgabe aus (Task Announcement) und sendet sie an alle Agenten. # 2B
    def announce_task(self, simulation, package) -> None:
        eligible_ids = query_candidate_agents(  # 4C
            self.get_position(), package.target, [a.agent_id for a in simulation.agents])  # 4C
        simulation.log_event(TomaKing4C_LogCandidateQueryT.format(  # 4C
            self.get_position(), package.target, eligible_ids))  # 4C
        if not eligible_ids:  # 4C
            simulation.log_event(TomaKing4C_LogNoCandidatesTemplate.format(  # 4C
                self.depot_id, package.package_id))  # 4C
            return  # 4C
        payload = {
            TomaKing2A_KeyTaskId:      package.package_id,
            TomaKing2A_KeyDestination: package.target,
            TomaKing2A_KeyDeadline:    package.deadline,
        }
        for agent in simulation.agents:
            if agent.agent_id not in eligible_ids:  # 4C
                continue  # 4C
            self.send_message(simulation, TomaKing2A_MsgAnnounce, agent.agent_id, payload) # 2C
            simulation.log_event(TomaKing2A_LogAnnounceTemplate.format( # 2C
                self.depot_id, agent.agent_id, package.package_id, package.target, package.deadline)) # 2C
    # Wertet alle gepufferten BIDs pro Task aus und erteilt Zuschläge. # 2D
    def process_bids(self, simulation) -> None:
        for task_id, bids in list(self.pending_bids.items()):
            if not bids:
                simulation.log_event(
                    TomaKing2D_LogNoBidsTemplate.format(self.depot_id, task_id))
                continue
            winner = self._select_winner(bids)
            winner_id = winner.payload[TomaKing2A_KeyAgentId]
            cost      = winner.payload[TomaKing2A_KeyCost]
            simulation.log_event(TomaKing2D_LogAuctionTemplate.format(
                self.depot_id, task_id, len(bids), winner_id, cost))
            self._award_task(simulation, task_id, winner_id)
        self.pending_bids = {}
    # Wählt deterministisch den Gewinner: niedrigste Kosten, bei Gleichstand niedrigste Agent-ID. # 2D
    @staticmethod
    def _select_winner(bids: list):
        return min(bids, key=lambda msg: (
            msg.payload[TomaKing2A_KeyCost],
            msg.payload[TomaKing2A_KeyAgentId],
        ))
    # Sendet eine AWARD-Nachricht an den Gewinner und markiert das Paket als ASSIGNED. # 2D
    def _award_task(self, simulation, task_id: int, winner_id: int) -> None:
        payload = {
            TomaKing2A_KeyTaskId:  task_id,
            TomaKing2A_KeyAgentId: winner_id,
        }
        self.send_message(simulation, TomaKing2A_MsgAward, winner_id, payload)
        simulation.log_event(TomaKing2A_LogAwardTemplate.format(
            self.depot_id, winner_id, task_id))
        package = simulation.get_package_by_id(task_id)
        if package is not None:
            package.mark_assigned(winner_id)
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