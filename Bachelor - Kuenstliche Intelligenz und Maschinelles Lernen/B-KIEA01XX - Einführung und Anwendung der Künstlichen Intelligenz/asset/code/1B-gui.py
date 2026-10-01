# !/usr/bin/env python
# -*- coding: utf-8 -*-
# gui.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import tkinter as tk
from map import Map
from agent import create_agents, get_agent_statistics # 1B
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
)

## =============================================================================
# ============================== GUI - HAUPTKLASSE ==============================
## =============================================================================

class MapGUI:
    # Initialisiert das Hauptfenster, die Karte und berechnet alle Größen.
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.configure(bg=TomaKingGUI_ColorWindowBg)
        self.root.overrideredirect(TomaKingGUI_OverrideRedirect)
        self.root.bind(TomaKingGUI_EscapeKey, lambda e: self.root.quit())
        self.root.title(TomaKingGUI_WindowTitle)
        self.root.state(TomaKingGUI_WindowState)
        self.map = Map()
        self.agents = create_agents(self.map) # 1B
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
        # --- Info-Frame ---
        info_frame = tk.Frame(container, bg=TomaKingGUI_ColorInfoBg)
        info_frame.pack(fill=TomaKingGUI_InfoFrameFill, pady=TomaKingGUI_InfoFramePady)
        # 1A
        stats = self.map.get_statistics()
        info_text = (
            f"{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1A_LabelDepots}{stats[TomaKing1A_StatKeyDepotCount]}{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1A_LabelTargets}{stats[TomaKing1A_StatKeyTargetCount]}{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1A_LabelWalls}{stats[TomaKing1A_StatKeyWallCount]}{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1A_LabelEmpty}{stats[TomaKing1A_StatKeyEmptyCount]}{TomaKingGUI_InfoSeparator}"
            f"{TomaKing1A_LabelMapSize}"
            f"{stats[TomaKing1A_StatKeyWidth]}{TomaKingGUI_SizeSeparator}{stats[TomaKing1A_StatKeyHeight]}"
            f"{TomaKingGUI_InfoSeparator}"
        )
        # 1B
        agent_stats = get_agent_statistics(self.agents)
        info_text = info_text + (
            f"{TomaKing1B_LabelAgents}"
            f"{agent_stats[TomaKing1B_StatKeyAgentCount]} "
            f"{TomaKing1B_LabelAgentParts.format(TomaKing1B_LabelStandard, agent_stats[TomaKing1B_StatKeyStandardCount])} "
            f"{TomaKing1B_LabelAgentParts.format(TomaKing1B_LabelExpress, agent_stats[TomaKing1B_StatKeyExpressCount])}"
            f"{TomaKingGUI_InfoSeparator}"
        )
        tk.Label(
            info_frame,
            text=info_text,
            font=(TomaKingGUI_InfoFont, TomaKingGUI_InfoSize),
            bg=TomaKingGUI_ColorInfoBg,
            fg=TomaKingGUI_ColorInfoText
        ).pack()
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