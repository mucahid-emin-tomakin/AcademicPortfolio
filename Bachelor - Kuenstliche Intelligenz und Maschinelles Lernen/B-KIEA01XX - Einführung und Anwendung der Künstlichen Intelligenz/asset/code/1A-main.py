# !/usr/bin/env python
# -*- coding: utf-8 -*-
# main.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import tkinter as tk
from gui import MapGUI

## =============================================================================
# ==================================== MAIN =====================================
## =============================================================================

# Einstiegspunkt: Fenster erzeugen, GUI aufbauen, Ereignisschleife starten.
def main():
    root = tk.Tk()
    MapGUI(root)
    root.mainloop()
# Nur bei direkter Ausführung starten, nicht beim Import.
if __name__ == "__main__":
    main()