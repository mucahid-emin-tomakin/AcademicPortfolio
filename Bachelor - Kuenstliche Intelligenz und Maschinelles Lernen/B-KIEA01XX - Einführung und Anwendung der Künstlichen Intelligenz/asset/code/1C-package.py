# !/usr/bin/env python
# -*- coding: utf-8 -*-
# package.py

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
        return (f"Package(id={self.package_id}, depot={self.depot}, "
                f"target={self.target}, status={self.status})")