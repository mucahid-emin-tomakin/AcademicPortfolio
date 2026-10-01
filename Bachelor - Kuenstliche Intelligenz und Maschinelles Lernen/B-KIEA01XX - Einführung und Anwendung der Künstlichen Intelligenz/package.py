# !/usr/bin/env python
# -*- coding: utf-8 -*-
# package.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

from config import ( # 2B
    # AUFGABE 2B - Status-Werte # 2B
    TomaKing2B_StatusPending,
    TomaKing2B_StatusAssigned, # 2D
    TomaKing2B_StatusDelivered, # 5A
    TomaKing2B_StatusExpired, # 5A
    # AUFGABE 2B - Repr-Template # 2B
    TomaKing2B_ReprTemplate,
)

## =============================================================================
# =========================== AUFGABE 1C - PACKAGE CLASS ========================
## =============================================================================

class Package:
    # Kapselt ein Lieferpaket mit Ziel, Deadline und Status.
    def __init__(self, package_id, depot, target, current_step, deadline, size=1):
        self.package_id = package_id
        self.depot = depot
        self.target = target
        self.created_step = current_step
        self.deadline = deadline
        self.size = size
        self.status = None
        self.assigned_agent_id = None
        self.delivered_step = None # 5A
        self.expired_step = None # 5A
        self.delivery_path_length = None # 5A
    # Eindeutige Repräsentation für Debugging.
    def __repr__(self) -> str:
        return TomaKing2B_ReprTemplate.format( # 2B
            self.package_id, self.depot, self.target, # 2B
            self.deadline, self.status # 2B
        ) # 2B
    # Markiert das Paket als einem Agenten zugewiesen (PENDING -> ASSIGNED). # 2D
    def mark_assigned(self, agent_id: int) -> None:
        self.status = TomaKing2B_StatusAssigned
        self.assigned_agent_id = agent_id
    # Markiert das Paket als zugestellt. # 5A
    def mark_delivered(self, step: int, path_length: int = None) -> None:
        self.status = TomaKing2B_StatusDelivered
        self.delivered_step = step
        self.delivery_path_length = path_length
    # Markiert das Paket als abgelaufen. # 5A
    def mark_expired(self, step: int) -> None:
        self.status = TomaKing2B_StatusExpired
        self.expired_step = step

## =============================================================================
# ========================= AUFGABE 2B - PACKAGE-FABRIK =========================
## =============================================================================

# Erzeugt ein neues Paket im Status PENDING mit den übergebenen Werten.
def create_package(package_id, depot_position, target_position,
                   current_step, deadline):
    package = Package(package_id, depot_position, target_position, current_step, deadline)
    package.status = TomaKing2B_StatusPending
    return package