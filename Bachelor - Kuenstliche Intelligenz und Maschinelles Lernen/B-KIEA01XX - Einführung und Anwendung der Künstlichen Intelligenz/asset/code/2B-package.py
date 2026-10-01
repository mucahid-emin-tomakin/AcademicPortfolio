# !/usr/bin/env python
# -*- coding: utf-8 -*-
# package.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

from config import ( # 2B
    # AUFGABE 2B - Status-Werte # 2B
    TomaKing2B_StatusPending,
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
    # Eindeutige Repräsentation für Debugging.
    def __repr__(self) -> str:
        return TomaKing2B_ReprTemplate.format( # 2B
            self.package_id, self.depot, self.target, # 2B
            self.deadline, self.status # 2B
        ) # 2B

## =============================================================================
# ========================= AUFGABE 2B - PACKAGE-FABRIK =========================
## =============================================================================

# Erzeugt ein neues Paket im Status PENDING mit den übergebenen Werten.
def create_package(package_id, depot_position, target_position,
                   current_step, deadline):
    package = Package(package_id, depot_position, target_position, current_step, deadline)
    package.status = TomaKing2B_StatusPending
    return package