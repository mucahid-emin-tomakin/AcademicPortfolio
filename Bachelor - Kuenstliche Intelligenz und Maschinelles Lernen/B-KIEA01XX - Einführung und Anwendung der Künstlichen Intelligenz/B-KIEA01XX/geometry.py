# !/usr/bin/env python
# -*- coding: utf-8 -*-
# geometry.py

## =============================================================================
# ============================ AUFGABE 2C - GEOMETRIE ===========================
## =============================================================================

# Berechnet die Manhattan-Distanz zwischen zwei Punkten im 2D-Gitter.
def manhattan(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])