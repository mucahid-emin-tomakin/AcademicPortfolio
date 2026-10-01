# !/usr/bin/env python
# -*- coding: utf-8 -*-
# simulation.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import random
import statistics # 5B
from package import create_package # 2B
from prolog import query_reachable, export_agents # 4C
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
    # AUFGABE 2B - Status-Werte # 5A
    TomaKing2B_StatusDelivered,
    TomaKing2B_StatusExpired,
    # AUFGABE 2B - Logging
    TomaKing2B_LogGenerationTemplate,
    # AUFGABE 2B - Error Handling
    TomaKing2B_ErrorNoDepots,
    TomaKing2B_ErrorNoTargets,
    # AUFGABE 4C - Logging # 4C
    TomaKing4C_LogReachableOKTemplate,
    TomaKing4C_LogReachableFailTemplate,
    TomaKing4C_LogExportAgentsTemplate,
    # AUFGABE 5A - Experimente # 5A
    TomaKing5A_VerboseDefault,
    TomaKing5A_BatteryRegen,
    # AUFGABE 5A - Statistics # 5A
    TomaKing5A_StatKeyAvgDeliveryTime,
    TomaKing5A_StatKeySuccessRate,
    TomaKing5A_StatKeyAvgPathLength,
    TomaKing5A_StatKeyTotalPackages,
    TomaKing5A_StatKeyDelivered,
    TomaKing5A_StatKeyExpired,
    # AUFGABE 5B - Statistics # 5B
    TomaKing5B_StatKeyCallCount,
    TomaKing5B_StatKeyExpandedAvg,
    TomaKing5B_StatKeyExpandedMin,
    TomaKing5B_StatKeyExpandedMax,
    TomaKing5B_StatKeyExpandedMedian,
    TomaKing5B_StatKeyTimeAvgMs,
    TomaKing5B_StatKeyTimeMaxMs,
    TomaKing5B_StatKeyTimeMedianMs,
    # AUFGABE 5B - Metric-Keys (intern) # 5B
    TomaKing5B_MetricKeyExpanded,
    TomaKing5B_MetricKeyTimeMs,
    TomaKing5B_MetricKeyGoal,
    TomaKing5B_MetricKeyTaskId,
    TomaKing5B_MetricKeyStep,
    # AUFGABE 2A - Nachrichtentypen # 5C
    TomaKing2A_MsgBid,
    # AUFGABE 2A - Payload-Schlüssel # 5C
    TomaKing2A_KeyTaskId,
    # AUFGABE 5C - Metric-Keys (intern) # 5C
    TomaKing5C_MetricKeyTaskId,
    TomaKing5C_MetricKeyMsgType,
    TomaKing5C_MetricKeySender,
    TomaKing5C_MetricKeyReceiver,
    TomaKing5C_MetricKeyStep,
    # AUFGABE 5C - Statistics # 5C
    TomaKing5C_StatKeyMsgPerTaskAvg,
    TomaKing5C_StatKeyBiddersPerAucAvg,
    TomaKing5C_StatKeyTotalMessages,
    TomaKing5C_StatKeyTotalTasks,
    TomaKing5C_StatKeyTotalAuctions,
)

## =============================================================================
# ======================== AUFGABE 1C - SIMULATION CLASS ========================
## =============================================================================

class Simulation:
    # Initialisiert die Simulation mit Karte, Agenten, Nachrichten-Bus und Step-Zähler.
    def __init__(self, map_instance, agents: list, depots: list, graph,
                 verbose: bool = TomaKing5A_VerboseDefault): # 2A # 3C # 5A
        self.map = map_instance
        self.agents = agents
        self.depots = depots # 2A
        self.graph = graph # 3C
        self.packages: list = [] # 2B
        self._next_package_id = TomaKing2B_StartPackageId # 2B
        self.message_bus: list = []
        self.step_count = 0
        self._event_log: list = []
        self.astar_metrics: list = [] # 5B
        self.message_metrics: list = [] # 5C
        self.verbose = verbose # 5A
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
        if message.payload and TomaKing2A_KeyTaskId in message.payload: # 5C
            self.message_metrics.append({ # 5C
                TomaKing5C_MetricKeyTaskId:   message.payload[TomaKing2A_KeyTaskId], # 5C
                TomaKing5C_MetricKeyMsgType:  message.msg_type, # 5C
                TomaKing5C_MetricKeySender:   message.sender_id, # 5C
                TomaKing5C_MetricKeyReceiver: message.receiver_id, # 5C
                TomaKing5C_MetricKeyStep:     self.step_count, # 5C
            }) # 5C
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
        self._check_deadlines() # 5A
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
        if not agent.current_route and agent.task_phase is None: # 5A
            if agent.assigned_tasks: # 5A
                agent._try_start_next_task(self) # 5A
            if not agent.current_route: # 5A
                agent.battery = min(agent.battery_max, # 5A
                                    agent.battery + TomaKing5A_BatteryRegen) # 5A
                return # 5A
        for _ in range(agent.speed):
            if agent.battery <= 0:
                break
            dx, dy = agent.decide_action(self.map, self) # 3C
            if (dx, dy) == (0, 0): # 3C
                break # 3C
            if agent.try_move(self.map, dx, dy, self): # 5A
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
        if not query_reachable(depot.get_position(), target): # 4C
            self.log_event(TomaKing4C_LogReachableFailTemplate.format( # 4C
                depot.get_position(), target)) # 4C
            return # 4C
        self.log_event(TomaKing4C_LogReachableOKTemplate.format( # 4C
            depot.get_position(), target)) # 4C
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
        agent_count = export_agents(self.agents) # 4C
        self.log_event(TomaKing4C_LogExportAgentsTemplate.format(agent_count)) # 4C
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
        if not self.verbose: # 5A
            return # 5A
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

## =============================================================================
# ======================== AUFGABE 5A - DEADLINE EXPIRED ========================
## =============================================================================

    # Prueft, ob Pakete die Deadline ueberschritten haben, und markiert sie als EXPIRED.
    def _check_deadlines(self) -> None:
        for package in self.packages:
            if package.status not in (TomaKing2B_StatusDelivered, TomaKing2B_StatusExpired) \
               and self.step_count > package.deadline:
                package.mark_expired(self.step_count)
                for agent in self.agents:
                    if package.package_id in agent.assigned_tasks:
                        agent._abandon_current_task(self)
                        break

## =============================================================================
# =========================== AUFGABE 5A - STATISTIK ============================
## =============================================================================

    # Liefert die drei Leistungskennzahlen aus 5A.
    def get_statistics(self) -> dict:
        delivered = [p for p in self.packages if p.status == TomaKing2B_StatusDelivered]
        expired = [p for p in self.packages if p.status == TomaKing2B_StatusExpired]
        total = len(self.packages)
        avg_delivery = (
            sum(p.delivered_step - p.created_step for p in delivered) / len(delivered)
            if delivered else 0.0
        )
        success_rate = (len(delivered) / total * 100.0) if total > 0 else 0.0
        avg_path = (
            sum(p.delivery_path_length for p in delivered
                if p.delivery_path_length is not None) / len(delivered)
            if delivered else 0.0
        )
        return {
            TomaKing5A_StatKeyAvgDeliveryTime: avg_delivery,
            TomaKing5A_StatKeySuccessRate:     success_rate,
            TomaKing5A_StatKeyAvgPathLength:   avg_path,
            TomaKing5A_StatKeyTotalPackages:   total,
            TomaKing5A_StatKeyDelivered:       len(delivered),
            TomaKing5A_StatKeyExpired:         len(expired),
        }

## =============================================================================
# ================== AUFGABE 5B - A*-METRIKEN-TRACKING ==========================
## =============================================================================

    # Zeichnet einen einzelnen A*-Aufruf mit Expansionszahl und Laufzeit auf.
    def record_planning(self, expanded: int, time_ms: float,
                        goal: tuple, task_id: int | None) -> None:
        self.astar_metrics.append({
            TomaKing5B_MetricKeyExpanded: expanded,
            TomaKing5B_MetricKeyTimeMs:   time_ms,
            TomaKing5B_MetricKeyGoal:     goal,
            TomaKing5B_MetricKeyTaskId:   task_id,
            TomaKing5B_MetricKeyStep:     self.step_count,
        })
    # Gibt die aggregierten A*-Kennzahlen zurueck.
    def get_astar_statistics(self) -> dict:
        if not self.astar_metrics:
            return {
                TomaKing5B_StatKeyCallCount:      0,
                TomaKing5B_StatKeyExpandedAvg:    0.0,
                TomaKing5B_StatKeyExpandedMin:    0,
                TomaKing5B_StatKeyExpandedMax:    0,
                TomaKing5B_StatKeyExpandedMedian: 0.0,
                TomaKing5B_StatKeyTimeAvgMs:      0.0,
                TomaKing5B_StatKeyTimeMaxMs:      0.0,
                TomaKing5B_StatKeyTimeMedianMs:   0.0,
            }
        expanded_vals = [m[TomaKing5B_MetricKeyExpanded] for m in self.astar_metrics]
        time_vals     = [m[TomaKing5B_MetricKeyTimeMs]   for m in self.astar_metrics]
        return {
            TomaKing5B_StatKeyCallCount:      len(self.astar_metrics),
            TomaKing5B_StatKeyExpandedAvg:    statistics.mean(expanded_vals),
            TomaKing5B_StatKeyExpandedMin:    min(expanded_vals),
            TomaKing5B_StatKeyExpandedMax:    max(expanded_vals),
            TomaKing5B_StatKeyExpandedMedian: statistics.median(expanded_vals),
            TomaKing5B_StatKeyTimeAvgMs:      statistics.mean(time_vals),
            TomaKing5B_StatKeyTimeMaxMs:      max(time_vals),
            TomaKing5B_StatKeyTimeMedianMs:   statistics.median(time_vals),
        }
    # Liefert die rohen A*-Messwerte (Kopie, fuer Histogramme/Boxplots).
    def get_astar_metrics_raw(self) -> list:
        return list(self.astar_metrics)

## =============================================================================
# ============= AUFGABE 5C - KOMMUNIKATIONS-METRIKEN ============================
## =============================================================================

    # Gibt die aggregierten Kommunikationskennzahlen zurueck.
    def get_communication_statistics(self) -> dict:
        if not self.message_metrics:
            return {
                TomaKing5C_StatKeyMsgPerTaskAvg:    0.0,
                TomaKing5C_StatKeyBiddersPerAucAvg: 0.0,
                TomaKing5C_StatKeyTotalMessages:    0,
                TomaKing5C_StatKeyTotalTasks:       0,
                TomaKing5C_StatKeyTotalAuctions:    0,
            }
        per_task = {}
        for m in self.message_metrics:
            tid = m[TomaKing5C_MetricKeyTaskId]
            per_task.setdefault(tid, []).append(m)
        bidders_per_auction = []
        for msgs in per_task.values():
            n_bids = sum(1 for m in msgs
                         if m[TomaKing5C_MetricKeyMsgType] == TomaKing2A_MsgBid)
            bidders_per_auction.append(n_bids)
        msg_per_task = [len(msgs) for msgs in per_task.values()]
        return {
            TomaKing5C_StatKeyMsgPerTaskAvg:    statistics.mean(msg_per_task),
            TomaKing5C_StatKeyBiddersPerAucAvg: statistics.mean(bidders_per_auction),
            TomaKing5C_StatKeyTotalMessages:    len(self.message_metrics),
            TomaKing5C_StatKeyTotalTasks:       len(per_task),
            TomaKing5C_StatKeyTotalAuctions:    len(per_task),
        }
    # Liefert die rohen Nachrichten-Metriken (Kopie, fuer Histogramme).
    def get_message_metrics_raw(self) -> list:
        return list(self.message_metrics)