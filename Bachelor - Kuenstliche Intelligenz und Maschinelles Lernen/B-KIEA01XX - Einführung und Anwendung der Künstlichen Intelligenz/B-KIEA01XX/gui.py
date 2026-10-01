# !/usr/bin/env python
# -*- coding: utf-8 -*-
# gui.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import tkinter as tk
from map import Map
from agent import get_agent_statistics # 1B / 1C create_agents in main
from simulation import Simulation # 1C
from config import (
    # GUI - Fenster
    TomaKingGUI_OverrideRedirect,
    TomaKingGUI_WindowTitle,
    TomaKingGUI_EscapeKey,
    TomaKingGUI_WindowState,
    TomaKingGUI_ConfigureEvent,
    # GUI - Schriften & Größen
    TomaKingGUI_TitleFont,
    TomaKingGUI_TitleSize,
    TomaKingGUI_TitleFontWeight,
    TomaKingGUI_InfoFont,
    TomaKingGUI_InfoSize,
    TomaKingGUI_CellFont,
    TomaKingGUI_CellFontMinSize,
    TomaKingGUI_CellFontWeight,
    TomaKingGUI_CellFontSizeDivisor,
    # GUI - Layout & Padding
    TomaKingGUI_WindowPadding,
    TomaKingGUI_CellSize,
    TomaKingGUI_MinCellSize,
    TomaKingGUI_MaxCellSize,
    TomaKingGUI_MinAvailableSize,
    TomaKingGUI_CanvasPadding,
    TomaKingGUI_CellOutlineWidth,
    TomaKingGUI_CanvasHighlightThickness,
    TomaKingGUI_CanvasRelief,
    TomaKingGUI_CanvasTagAll,
    TomaKingGUI_CanvasFillTransparent,
    TomaKingGUI_MainFramePadding,
    TomaKingGUI_CanvasBorder,
    # GUI - Layout-Helfer
    TomaKingGUI_SizeSeparator,
    TomaKingGUI_SidesCount,
    TomaKingGUI_CenterDivisor,
    # GUI - Grid-Konfiguration
    TomaKingGUI_MainFrameRowWeights,
    TomaKingGUI_MainFrameColumnWeights,
    TomaKingGUI_ContainerGridRow,
    TomaKingGUI_ContainerGridColumn,
    # GUI - pack-Parameter
    TomaKingGUI_MainFrameFill,
    TomaKingGUI_MainFrameExpand,
    TomaKingGUI_TitlePadyTop,
    TomaKingGUI_TitlePadyBottom,
    TomaKingGUI_InfoFrameFill,
    TomaKingGUI_InfoFramePady,
    # GUI - Anzeigetexte
    TomaKingGUI_TitleLabelText,
    TomaKingGUI_InfoSeparator,
    # GUI - Farben
    TomaKingGUI_ColorWindowBg,
    TomaKingGUI_ColorFrameBg,
    TomaKingGUI_ColorCanvasBg,
    TomaKingGUI_ColorCanvasBorder,
    TomaKingGUI_ColorCellOutline,
    TomaKingGUI_ColorTitleBg,
    TomaKingGUI_ColorTitleText,
    TomaKingGUI_ColorInfoBg,
    TomaKingGUI_ColorInfoText,
    # AUFGABE 1A - Symbole
    TomaKing1A_Wall,
    TomaKing1A_Depot,
    TomaKing1A_Target,
    # AUFGABE 1A - Farben
    TomaKing1A_ColorEmpty,
    TomaKing1A_ColorWall,
    TomaKing1A_ColorDepot,
    TomaKing1A_ColorTarget,
    TomaKing1A_ColorText,
    # AUFGABE 1A - Anzeigetexte
    TomaKing1A_LabelDepots,
    TomaKing1A_LabelTargets,
    TomaKing1A_LabelWalls,
    TomaKing1A_LabelEmpty,
    TomaKing1A_LabelMapSize,
    # AUFGABE 1A - Statistics
    TomaKing1A_StatKeyWidth,
    TomaKing1A_StatKeyHeight,
    TomaKing1A_StatKeyDepotCount,
    TomaKing1A_StatKeyTargetCount,
    TomaKing1A_StatKeyWallCount,
    TomaKing1A_StatKeyEmptyCount,
    # AUFGABE 1B - Agententypen
    TomaKing1B_TypeStandard,
    # AUFGABE 1B - Symbole
    TomaKing1B_SymbolStandard,
    TomaKing1B_SymbolExpress,
    # AUFGABE 1B - Farben
    TomaKing1B_ColorStandard,
    TomaKing1B_ColorExpress,
    TomaKing1B_RadiusFactor,
    # AUFGABE 1B - Anzeigetexte
    TomaKing1B_LabelAgents,
    TomaKing1B_LabelStandard,
    TomaKing1B_LabelExpress,
    TomaKing1B_LabelAgentParts,
    # AUFGABE 1B - Statistics
    TomaKing1B_StatKeyAgentCount,
    TomaKing1B_StatKeyStandardCount,
    TomaKing1B_StatKeyExpressCount,
    # AUFGABE 1C - Zeitsteuerung
    TomaKing1C_StepDelay,
    # AUFGABE 1C - Button-Texte
    TomaKing1C_ButtonStepText,
    TomaKing1C_ButtonAutoRunText,
    TomaKing1C_ButtonStopText,
    # AUFGABE 1C - Button-Layout
    TomaKing1C_ButtonFramePady,
    TomaKing1C_ButtonPaddingX,
    TomaKing1C_ButtonFont,
    TomaKing1C_ButtonFontSize,
    # AUFGABE 1C - Button-Farben
    TomaKing1C_ColorButtonBg,
    TomaKing1C_ColorButtonFg,
    TomaKing1C_ColorButtonActiveBg,
    TomaKing1C_ColorButtonActiveFg,
    TomaKing1C_ColorButtonDisabledFg,
    # AUFGABE 1C - Labels
    TomaKing1C_LabelStep,
)

## =============================================================================
# ============================== GUI - HAUPTKLASSE ==============================
## =============================================================================

class MapGUI:
    # Initialisiert das Hauptfenster, die Karte und berechnet alle Größen.
    def __init__(self, root: tk.Tk, simulation: Simulation): # 1C
        self.root = root
        self.simulation = simulation # 1C
        self.map = simulation.map # 1C
        self.agents = simulation.agents # 1C
        self.autorun_active = False # 1C
        self.root.configure(bg=TomaKingGUI_ColorWindowBg)
        self.root.overrideredirect(TomaKingGUI_OverrideRedirect)
        self.root.bind(TomaKingGUI_EscapeKey, lambda e: self.root.quit())
        self.root.title(TomaKingGUI_WindowTitle)
        self.root.state(TomaKingGUI_WindowState)
        self.cell_size = TomaKingGUI_CellSize
        self._create_widgets()
        self._update_layout()
        self.root.bind(TomaKingGUI_ConfigureEvent, self._on_resize)

## =============================================================================
# ============================= GUI - FENSTERGRÖSSE =============================
## =============================================================================

    # Reagiert auf Fenstergrößenänderungen und aktualisiert das Layout.
    def _on_resize(self, event):
        if event.widget == self.root:
            self._update_layout()
    # Berechnet die optimale Zellgröße basierend auf der aktuellen Fenstergröße.
    def _update_layout(self):
        self.root.update_idletasks()
        mf_w = self.main_frame.winfo_width()
        mf_h = self.main_frame.winfo_height()
        avail_w = max(TomaKingGUI_MinAvailableSize, mf_w - TomaKingGUI_SidesCount * TomaKingGUI_WindowPadding)
        avail_h = max(TomaKingGUI_MinAvailableSize, mf_h - TomaKingGUI_SidesCount * TomaKingGUI_WindowPadding)
        cw = avail_w / self.map.width
        ch = avail_h / self.map.height
        new_cs = int(min(cw, ch))
        new_cs = max(TomaKingGUI_MinCellSize, min(TomaKingGUI_MaxCellSize, new_cs))
        if new_cs != self.cell_size:
            self.cell_size = new_cs
            border = TomaKingGUI_CanvasBorder
            cw_px = self.map.width  * self.cell_size + TomaKingGUI_SidesCount * border
            ch_px = self.map.height * self.cell_size + TomaKingGUI_SidesCount * border
            self.canvas.config(width=cw_px, height=ch_px)
            self._draw_map()

## =============================================================================
# ================================ GUI - LAYOUT =================================
## =============================================================================

    # Erstellt alle GUI-Elemente
    def _create_widgets(self):
        # --- Haupt-Frame ---
        self.main_frame = tk.Frame(
            self.root,
            bg=TomaKingGUI_ColorFrameBg,
            padx=TomaKingGUI_MainFramePadding,
            pady=TomaKingGUI_MainFramePadding
        )
        self.main_frame.pack(fill=TomaKingGUI_MainFrameFill, expand=TomaKingGUI_MainFrameExpand)
        # --- Grid-Konfiguration ---
        for i, w in enumerate(TomaKingGUI_MainFrameRowWeights):
            self.main_frame.grid_rowconfigure(i, weight=w)
        for i, w in enumerate(TomaKingGUI_MainFrameColumnWeights):
            self.main_frame.grid_columnconfigure(i, weight=w)
        # --- Container ---
        container = tk.Frame(self.main_frame, bg=TomaKingGUI_ColorFrameBg)
        container.grid(row=TomaKingGUI_ContainerGridRow, column=TomaKingGUI_ContainerGridColumn)
        # --- Titel ---
        title = tk.Label(
            container,
            text=TomaKingGUI_TitleLabelText,
            font=(TomaKingGUI_TitleFont, TomaKingGUI_TitleSize, TomaKingGUI_TitleFontWeight),
            bg=TomaKingGUI_ColorTitleBg,
            fg=TomaKingGUI_ColorTitleText
        )
        title.pack(pady=(TomaKingGUI_TitlePadyTop, TomaKingGUI_TitlePadyBottom))
        # --- Canvas ---
        self.canvas = tk.Canvas(
            container,
            bg=TomaKingGUI_ColorCanvasBg,
            highlightthickness=TomaKingGUI_CanvasHighlightThickness,
            highlightbackground=TomaKingGUI_ColorCanvasBorder,
            bd=TomaKingGUI_CanvasBorder,
            relief=TomaKingGUI_CanvasRelief
        )
        self.canvas.pack(padx=TomaKingGUI_CanvasPadding, pady=TomaKingGUI_CanvasPadding)
        # --- Info-Frame --- # 1C
        info_frame = tk.Frame(container, bg=TomaKingGUI_ColorInfoBg)
        info_frame.pack(fill=TomaKingGUI_InfoFrameFill, pady=TomaKingGUI_InfoFramePady)
        self.info_label = tk.Label(
            info_frame,
            text=self._build_info_text(),
            font=(TomaKingGUI_InfoFont, TomaKingGUI_InfoSize),
            bg=TomaKingGUI_ColorInfoBg,
            fg=TomaKingGUI_ColorInfoText
        )
        self.info_label.pack()
        # --- Button-Frame --- # 1C
        button_frame = tk.Frame(container, bg=TomaKingGUI_ColorFrameBg)
        button_frame.pack(pady=TomaKing1C_ButtonFramePady)
        self.step_button = tk.Button(
            button_frame,
            text=TomaKing1C_ButtonStepText,
            font=(TomaKing1C_ButtonFont, TomaKing1C_ButtonFontSize),
            bg=TomaKing1C_ColorButtonBg,
            fg=TomaKing1C_ColorButtonFg,
            activebackground=TomaKing1C_ColorButtonActiveBg,
            activeforeground=TomaKing1C_ColorButtonActiveFg,
            disabledforeground=TomaKing1C_ColorButtonDisabledFg,
            command=self._on_step
        )
        self.step_button.pack(side=tk.LEFT, padx=TomaKing1C_ButtonPaddingX)
        self.autorun_button = tk.Button(
            button_frame,
            text=TomaKing1C_ButtonAutoRunText,
            font=(TomaKing1C_ButtonFont, TomaKing1C_ButtonFontSize),
            bg=TomaKing1C_ColorButtonBg,
            fg=TomaKing1C_ColorButtonFg,
            activebackground=TomaKing1C_ColorButtonActiveBg,
            activeforeground=TomaKing1C_ColorButtonActiveFg,
            disabledforeground=TomaKing1C_ColorButtonDisabledFg,
            command=self._on_autorun_toggle
        )
        self.autorun_button.pack(side=tk.LEFT, padx=TomaKing1C_ButtonPaddingX)
        self._draw_map()

## =============================================================================
# ============================= AUFGABE 1A - KARTE ==============================
## =============================================================================

    # Zeichnet die Karte auf dem Canvas: Wände, Depots, Ziele und freie Zellen.
    def _draw_map(self):
        self.canvas.delete(TomaKingGUI_CanvasTagAll)
        cs = self.cell_size
        border = TomaKingGUI_CanvasBorder
        for y in range(self.map.height):
            for x in range(self.map.width):
                x1 = border + x * cs
                y1 = border + y * cs
                x2 = border + (x + 1) * cs
                y2 = border + (y + 1) * cs
                cell = self.map.get_cell(x, y)
                if cell == TomaKing1A_Wall:
                    color = TomaKing1A_ColorWall
                elif cell == TomaKing1A_Depot:
                    color = TomaKing1A_ColorDepot
                elif cell == TomaKing1A_Target:
                    color = TomaKing1A_ColorTarget
                else:
                    color = TomaKing1A_ColorEmpty
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline=TomaKingGUI_ColorCellOutline,
                    width=TomaKingGUI_CellOutlineWidth
                )
                if cell in (TomaKing1A_Depot, TomaKing1A_Target):
                    self.canvas.create_text(
                        border + x * cs + cs // TomaKingGUI_CenterDivisor,
                        border + y * cs + cs // TomaKingGUI_CenterDivisor,
                        text=cell,
                        fill=TomaKing1A_ColorText,
                        font=(
                            TomaKingGUI_CellFont,
                            max(TomaKingGUI_CellFontMinSize,
                                cs // TomaKingGUI_CellFontSizeDivisor),
                            TomaKingGUI_CellFontWeight)
                    )
        self.canvas.create_rectangle(
            border, border,
            border + self.map.width * cs,
            border + self.map.height * cs,
            outline=TomaKingGUI_ColorCellOutline,
            width=TomaKingGUI_CellOutlineWidth,
            fill=TomaKingGUI_CanvasFillTransparent
        )
        self._draw_agents() # 1B

## =============================================================================
# ============================ AUFGABE 1B - AGENTEN =============================
## =============================================================================

    # Zeichnet alle Agenten als farbige Kreise mit Symbol (S/E) an ihren Positionen.
    def _draw_agents(self):
        cs = self.cell_size
        border = TomaKingGUI_CanvasBorder
        radius = cs * TomaKing1B_RadiusFactor
        for agent in self.agents:
            x, y = agent.get_position()
            cx = border + x * cs + cs // TomaKingGUI_CenterDivisor
            cy = border + y * cs + cs // TomaKingGUI_CenterDivisor
            if agent.agent_type == TomaKing1B_TypeStandard:
                color = TomaKing1B_ColorStandard
                symbol = TomaKing1B_SymbolStandard
            else:
                color = TomaKing1B_ColorExpress
                symbol = TomaKing1B_SymbolExpress
            self.canvas.create_oval(
                cx - radius, cy - radius,
                cx + radius, cy + radius,
                fill=color,
                outline=TomaKing1A_ColorText,
                width=TomaKingGUI_CellOutlineWidth
            )
            self.canvas.create_text(
                cx, cy,
                text=symbol,
                fill=TomaKing1A_ColorText,
                font=(
                    TomaKingGUI_CellFont,
                    max(TomaKingGUI_CellFontMinSize,
                        cs // TomaKingGUI_CellFontSizeDivisor),
                    TomaKingGUI_CellFontWeight)
            )

## =============================================================================
# =========================== AUFGABE 1C - SIMULATION ===========================
## =============================================================================

    # Baut die vollständige Info-Zeile aus Karten-, Agenten- und Step-Daten zusammen.
    def _build_info_text(self) -> str:
        stats = self.map.get_statistics()
        agent_stats = get_agent_statistics(self.agents)
        return (
            f"{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1A_LabelDepots}{stats[TomaKing1A_StatKeyDepotCount]}{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1A_LabelTargets}{stats[TomaKing1A_StatKeyTargetCount]}{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1A_LabelWalls}{stats[TomaKing1A_StatKeyWallCount]}{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1A_LabelEmpty}{stats[TomaKing1A_StatKeyEmptyCount]}{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1A_LabelMapSize}"
            f"{stats[TomaKing1A_StatKeyWidth]}{TomaKingGUI_SizeSeparator}{stats[TomaKing1A_StatKeyHeight]}"
            f"{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1B_LabelAgents}"
            f"{agent_stats[TomaKing1B_StatKeyAgentCount]} "
            f"{TomaKing1B_LabelAgentParts.format(TomaKing1B_LabelStandard, agent_stats[TomaKing1B_StatKeyStandardCount])} "
            f"{TomaKing1B_LabelAgentParts.format(TomaKing1B_LabelExpress, agent_stats[TomaKing1B_StatKeyExpressCount])}"
            f"{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1C_LabelStep}{self.simulation.step_count}"
            f"{TomaKingGUI_InfoSeparator}"
        )
    # Führt einen einzelnen Simulationsschritt aus und aktualisiert die GUI.
    def _on_step(self):
        self.simulation.step()
        self._draw_map()
        self._update_info()
    # Wechselt zwischen AutoRun (Start) und Stop.
    def _on_autorun_toggle(self):
        if self.autorun_active:
            self.autorun_active = False
            self.autorun_button.config(text=TomaKing1C_ButtonAutoRunText)
            self.step_button.config(state=tk.NORMAL)
        else:
            self.autorun_active = True
            self.autorun_button.config(text=TomaKing1C_ButtonStopText)
            self.step_button.config(state=tk.DISABLED)
            self._autorun_loop()
    # Endlos-Schleife für den AutoRun-Modus (mit konfiguriertem Delay).
    def _autorun_loop(self):
        if not self.autorun_active:
            return
        self._on_step()
        self.root.after(TomaKing1C_StepDelay, self._autorun_loop)
    # Aktualisiert die Info-Zeile (nach jedem Schritt).
    def _update_info(self):
        self.info_label.config(text=self._build_info_text())