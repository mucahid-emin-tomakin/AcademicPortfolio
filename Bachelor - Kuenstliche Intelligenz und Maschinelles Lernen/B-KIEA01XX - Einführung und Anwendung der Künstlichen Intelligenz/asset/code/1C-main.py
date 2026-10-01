# !/usr/bin/env python
# -*- coding: utf-8 -*-
# main.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import tkinter as tk
from map import Map # 1C
from agent import create_agents # 1C
from simulation import Simulation # 1C
from gui import MapGUI

## =============================================================================
# ==================================== MAIN =====================================
## =============================================================================

# Einstiegspunkt: Fenster erzeugen, GUI aufbauen, Ereignisschleife starten.
def main():
    root = tk.Tk()
    map_instance = Map() # 1C
    agents = create_agents(map_instance) # 1C
    simulation = Simulation(map_instance, agents) # 1C
    MapGUI(root, simulation) # 1C
    root.mainloop()
# Nur bei direkter Ausführung starten, nicht beim Import.
if __name__ == "__main__":
    main()