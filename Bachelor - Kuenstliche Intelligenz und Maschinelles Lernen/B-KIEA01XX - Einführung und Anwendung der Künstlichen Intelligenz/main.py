# !/usr/bin/env python
# -*- coding: utf-8 -*-
# main.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import tkinter as tk
from map import Map # 1C
from agent import create_agents # 1C
from depot import create_depots # 2A
from prolog import export_facts # 4A
from graph import Graph # 3A
from simulation import Simulation # 1C
from gui import MapGUI

## =============================================================================
# ==================================== MAIN =====================================
## =============================================================================

# Einstiegspunkt: Fenster erzeugen, GUI aufbauen, Ereignisschleife starten.
def main():
    root = tk.Tk()
    map_instance = Map() # 1C
    export_facts(map_instance) # 4A
    agents = create_agents(map_instance) # 1C
    depots = create_depots(map_instance) # 2A
    graph = Graph(map_instance) # 3A
    simulation = Simulation(map_instance, agents, depots, graph) # 1C, # 2A, # 3C
    MapGUI(root, simulation) # 1C
    root.mainloop()
# Nur bei direkter Ausführung starten, nicht beim Import.
if __name__ == "__main__":
    main()