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
from depot import create_depots # 2A
from config import (
    TomaKing2A_MsgAnnounce,
    TomaKing2A_MsgBid,
    TomaKing2A_MsgAward,
    TomaKing2A_KeyTaskId,
    TomaKing2A_KeyDestination,
    TomaKing2A_KeyDeadline,
    TomaKing2A_KeyAgentId,
    TomaKing2A_KeyCost,
    TomaKing2A_KeyAgent,
)

## =============================================================================
# ==================================== MAIN =====================================
## =============================================================================

# Einstiegspunkt: Fenster erzeugen, GUI aufbauen, Ereignisschleife starten.
def main():
    root = tk.Tk()
    map_instance = Map() # 1C
    agents = create_agents(map_instance) # 1C
    depots = create_depots(map_instance) # 2A
    simulation = Simulation(map_instance, agents, depots) # 1C, # 2A
    # TEMP-TEST 2A - nach Prüfung entfernen
    depot = depots[0]
    agent = agents[0]
    depot.send_message(
        simulation,
        TomaKing2A_MsgAnnounce,
        agent.agent_id,
        {
            TomaKing2A_KeyTaskId:      0,
            TomaKing2A_KeyDestination: (10, 10),
            TomaKing2A_KeyDeadline:    15,
        }
    )
    agent.read_messages(simulation)
    agent.send_message(
        simulation,
        TomaKing2A_MsgBid,
        depot.depot_id,
        {
            TomaKing2A_KeyAgentId: agent.agent_id,
            TomaKing2A_KeyTaskId:  0,
            TomaKing2A_KeyCost:    5,
        }
    )
    depot.read_messages(simulation)
    depot.send_message(
        simulation,
        TomaKing2A_MsgAward,
        agent.agent_id,
        {
            TomaKing2A_KeyTaskId: 0,
            TomaKing2A_KeyAgent:  agent.agent_id,
        }
    )
    agent.read_messages(simulation)
    for event in simulation._event_log:
        print(event)
    MapGUI(root, simulation) # 1C
    root.mainloop()
# Nur bei direkter Ausführung starten, nicht beim Import.
if __name__ == "__main__":
    main()