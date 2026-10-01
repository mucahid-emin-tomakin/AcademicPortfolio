# !/usr/bin/env python
# -*- coding: utf-8 -*-
# config.py

## =============================================================================
# ===================================== GUI =====================================
## =============================================================================

# ---------------------------------- Fenster ----------------------------------
TomaKingGUI_OverrideRedirect            = True
TomaKingGUI_WindowTitle                 = "B-KIEA01-XX2-N01"
TomaKingGUI_EscapeKey                   = "<Escape>"
TomaKingGUI_WindowState                 = "zoomed"
TomaKingGUI_ConfigureEvent              = "<Configure>"
# ---------------------------- Schriften & Größen -----------------------------
TomaKingGUI_TitleFont                   = "BlackChancery"
TomaKingGUI_TitleSize                   = 44
TomaKingGUI_TitleFontWeight             = "bold"
TomaKingGUI_InfoFont                    = "BlackChancery"
TomaKingGUI_InfoSize                    = 22
TomaKingGUI_CellFont                    = "BlackChancery"
TomaKingGUI_CellFontMinSize             = 8
TomaKingGUI_CellFontWeight              = "bold"
TomaKingGUI_CellFontSizeDivisor         = 3
# ----------------------------- Layout & Padding ------------------------------
TomaKingGUI_WindowPadding               = 10
TomaKingGUI_CellSize                    = 10
TomaKingGUI_MinCellSize                 = 5
TomaKingGUI_MaxCellSize                 = 80
TomaKingGUI_MinAvailableSize            = 10
TomaKingGUI_CanvasPadding               = 10
TomaKingGUI_CellOutlineWidth            = 0.5
TomaKingGUI_CanvasHighlightThickness    = 0
TomaKingGUI_CanvasRelief                = "sunken"
TomaKingGUI_CanvasTagAll                = "all"
TomaKingGUI_CanvasFillTransparent       = ""
TomaKingGUI_MainFramePadding            = 10
TomaKingGUI_CanvasBorder                = 2
# ------------------------------- Layout-Helfer -------------------------------
TomaKingGUI_SizeSeparator               = " x "
TomaKingGUI_SidesCount                  = 2
TomaKingGUI_CenterDivisor               = 2
# ---------------------------- Grid-Konfiguration -----------------------------
TomaKingGUI_MainFrameRowWeights         = (1, 0, 1)
TomaKingGUI_MainFrameColumnWeights      = (1,)
TomaKingGUI_ContainerGridRow            = 1
TomaKingGUI_ContainerGridColumn         = 0
# ------------------------------ pack-Parameter -------------------------------
TomaKingGUI_MainFrameFill               = "both"
TomaKingGUI_MainFrameExpand             = True
TomaKingGUI_TitlePadyTop                = 0
TomaKingGUI_TitlePadyBottom             = 10
TomaKingGUI_InfoFrameFill               = "x"
TomaKingGUI_InfoFramePady               = 5
# -------------------------------- Anzeigetexte -------------------------------
TomaKingGUI_TitleLabelText              = "Einführung und Anwendung der Künstlichen Intelligenz"
TomaKingGUI_InfoSeparator               = " I "
# ---------------------------------- Farben -----------------------------------
TomaKingGUI_ColorWindowBg               = "#000000"
TomaKingGUI_ColorFrameBg                = "#000000"
TomaKingGUI_ColorCanvasBg               = "#000000"
TomaKingGUI_ColorCanvasBorder           = "#2CFF05"
TomaKingGUI_ColorCellOutline            = "#2CFF05"
TomaKingGUI_ColorTitleBg                = "#000000"
TomaKingGUI_ColorTitleText              = "#2CFF05"
TomaKingGUI_ColorInfoBg                 = "#000000"
TomaKingGUI_ColorInfoText               = "#2CFF05"
# ---------------------------------- Logging ----------------------------------
TomaKingGUI_LogSeparatorChar            = "="
TomaKingGUI_LogSeparatorLength          = 77

## =============================================================================
# ====================== AUFGABE 1A - KARTEN-KONFIGURATION ======================
## =============================================================================

# --------------------------------- ASCII-Art ---------------------------------
TomaKing1A_ASCIIArt                     = [
    " ##       ####     ###       ###     ###         ###  ###",
    "##############     ####     #####    #####       ###  ###",
    "########   ###    ######   ######    ########    ###  ###",
    "###              #### ####### ####   ###  #####  ###  ###      ###",
    "###              ###   #####   ###   ###    ########  #############",
    "##############  ####    ###    ####  ###       #####  ########  ###",
    "##############          ###          ###         ###  ###       ###",
    "####       ###          ###          ###              ###       ###",
    "###        ###          ###          ###              ###       ###",
    "###        ###          ###          ###              ###       ###",
    " ##         ##          ###           ##              ##         ##",
]
# ---------------------------------- Symbole ----------------------------------
TomaKing1A_Wall                         = "#"
TomaKing1A_Empty                        = " "
TomaKing1A_Depot                        = "D"
TomaKing1A_Target                       = "Z"
# --------------------------------- Parameter ---------------------------------
TomaKing1A_DepotCount                   = 2
TomaKing1A_TargetCount                  = 4
TomaKing1A_Seed                         = 42
TomaKing1A_BorderSize                   = 2
TomaKing1A_Directions                   = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# ---------------------------- Rand & Koordinaten -----------------------------
TomaKing1A_BorderOffset                 = TomaKing1A_BorderSize
TomaKing1A_StartDepotIndex              = 0
TomaKing1A_MinCoordinate                = 0
TomaKing1A_SidesCount                   = 2
# ---------------------------------- Farben -----------------------------------
TomaKing1A_ColorEmpty                   = "#000000"
TomaKing1A_ColorWall                    = "#FFFFFF"
TomaKing1A_ColorDepot                   = "#FE0000"
TomaKing1A_ColorTarget                  = "#011EFE"
TomaKing1A_ColorText                    = "#FFFFFF"
# ------------------------------- Anzeigetexte --------------------------------
TomaKing1A_LabelDepots                  = "Depots: "
TomaKing1A_LabelTargets                 = "Ziele: "
TomaKing1A_LabelWalls                   = "Wände: "
TomaKing1A_LabelEmpty                   = "Freie Zellen: "
TomaKing1A_LabelMapSize                 = "Kartengröße: "
# -------------------------------- Statistics ---------------------------------
TomaKing1A_StatKeyWidth                 = "width"
TomaKing1A_StatKeyHeight                = "height"
TomaKing1A_StatKeyDepotCount            = "depot_count"
TomaKing1A_StatKeyTargetCount           = "target_count"
TomaKing1A_StatKeyWallCount             = "wall_count"
TomaKing1A_StatKeyEmptyCount            = "empty_count"
TomaKing1A_StatKeyDepots                = "depots"
TomaKing1A_StatKeyTargets               = "targets"
# ---------------------------------- Logging ----------------------------------
TomaKing1A_LogMapSize                   = "Kartengröße:           {}x{}"
TomaKing1A_LogDepots                    = "Depots:                {} -> {}"
TomaKing1A_LogTargets                   = "Ziele:                 {} -> {}"
TomaKing1A_LogWalls                     = "Wände:                 {}"
TomaKing1A_LogEmpty                     = "Freie Zellen:          {}"
TomaKing1A_LogMapASCII                  = "Karte (ASCII):"
# ------------------------------ Error Handling -------------------------------
TomaKing1A_ErrorNotEnoughCells          = "Nicht genug freie Zellen für {} Depots und {} Ziele!"
TomaKing1A_ErrorNoFreeCells             = "Keine freien Zellen auf der Karte!"
TomaKing1A_ErrorNotConnected            = "Nicht alle Depots und Ziele sind von Depot 1 aus erreichbar!"

## =============================================================================
# ============================ CONFIG - VALIDIERUNG =============================
## =============================================================================

def validate_config():
    required = [
        # ---------------------------- GUI - Fenster ----------------------------
        'TomaKingGUI_OverrideRedirect','TomaKingGUI_WindowTitle',
        'TomaKingGUI_EscapeKey','TomaKingGUI_WindowState',
        'TomaKingGUI_ConfigureEvent',
        # ---------------------- GUI - Schriften & Größen -----------------------
        'TomaKingGUI_TitleFont','TomaKingGUI_TitleSize',
        'TomaKingGUI_TitleFontWeight','TomaKingGUI_InfoFont',
        'TomaKingGUI_InfoSize','TomaKingGUI_CellFont',
        'TomaKingGUI_CellFontMinSize','TomaKingGUI_CellFontWeight',
        'TomaKingGUI_CellFontSizeDivisor',
        # ----------------------- GUI - Layout & Padding ------------------------
        'TomaKingGUI_WindowPadding','TomaKingGUI_CellSize',
        'TomaKingGUI_MinCellSize','TomaKingGUI_MaxCellSize',
        'TomaKingGUI_MinAvailableSize','TomaKingGUI_CanvasPadding',
        'TomaKingGUI_CellOutlineWidth','TomaKingGUI_CanvasHighlightThickness',
        'TomaKingGUI_CanvasRelief','TomaKingGUI_CanvasTagAll',
        'TomaKingGUI_CanvasFillTransparent','TomaKingGUI_MainFramePadding',
        'TomaKingGUI_CanvasBorder',
        # ------------------------- GUI - Layout-Helfer -------------------------
        'TomaKingGUI_SizeSeparator','TomaKingGUI_SidesCount',
        'TomaKingGUI_CenterDivisor',
        # ---------------------- GUI - Grid-Konfiguration -----------------------
        'TomaKingGUI_MainFrameRowWeights','TomaKingGUI_MainFrameColumnWeights',
        'TomaKingGUI_ContainerGridRow','TomaKingGUI_ContainerGridColumn',
        # ------------------------ GUI - pack-Parameter -------------------------
        'TomaKingGUI_MainFrameFill','TomaKingGUI_MainFrameExpand',
        'TomaKingGUI_TitlePadyTop','TomaKingGUI_TitlePadyBottom',
        'TomaKingGUI_InfoFrameFill','TomaKingGUI_InfoFramePady',
        # -------------------------- GUI - Anzeigetexte -------------------------
        'TomaKingGUI_TitleLabelText','TomaKingGUI_InfoSeparator',
        # ---------------------------- GUI - Farben -----------------------------
        'TomaKingGUI_ColorWindowBg','TomaKingGUI_ColorFrameBg',
        'TomaKingGUI_ColorCanvasBg','TomaKingGUI_ColorCanvasBorder',
        'TomaKingGUI_ColorCellOutline','TomaKingGUI_ColorTitleBg',
        'TomaKingGUI_ColorTitleText','TomaKingGUI_ColorInfoBg',
        'TomaKingGUI_ColorInfoText',
        # ---------------------------- GUI - Logging ----------------------------
        'TomaKingGUI_LogSeparatorChar','TomaKingGUI_LogSeparatorLength',
        # ------------ AUFGABE 1A - KARTEN-KONFIGURATION - ASCII-Art ------------
        'TomaKing1A_ASCIIArt',
        # ------------- AUFGABE 1A - KARTEN-KONFIGURATION - Symbole -------------
        'TomaKing1A_Wall','TomaKing1A_Empty','TomaKing1A_Depot',
        'TomaKing1A_Target',
        # ------------- AUFGABE 1A - KARTEN-KONFIGURATION - Parameter -----------
        'TomaKing1A_DepotCount','TomaKing1A_TargetCount','TomaKing1A_Seed',
        'TomaKing1A_BorderSize','TomaKing1A_Directions',
        # ------- AUFGABE 1A - KARTEN-KONFIGURATION - Rand & Koordinaten --------
        'TomaKing1A_BorderOffset','TomaKing1A_StartDepotIndex',
        'TomaKing1A_MinCoordinate','TomaKing1A_SidesCount',
        # ------------- AUFGABE 1A - KARTEN-KONFIGURATION - Farben --------------
        'TomaKing1A_ColorEmpty','TomaKing1A_ColorWall',
        'TomaKing1A_ColorDepot','TomaKing1A_ColorTarget',
        'TomaKing1A_ColorText',
        # ---------- AUFGABE 1A - KARTEN-KONFIGURATION - Anzeigetexte -----------
        'TomaKing1A_LabelDepots','TomaKing1A_LabelTargets',
        'TomaKing1A_LabelWalls','TomaKing1A_LabelEmpty',
        'TomaKing1A_LabelMapSize',
        # ----------- AUFGABE 1A - KARTEN-KONFIGURATION - Statistics ------------
        'TomaKing1A_StatKeyWidth','TomaKing1A_StatKeyHeight',
        'TomaKing1A_StatKeyDepotCount','TomaKing1A_StatKeyTargetCount',
        'TomaKing1A_StatKeyWallCount','TomaKing1A_StatKeyEmptyCount',
        'TomaKing1A_StatKeyDepots','TomaKing1A_StatKeyTargets',
        # ------------- AUFGABE 1A - KARTEN-KONFIGURATION - Logging -------------
        'TomaKing1A_LogMapSize','TomaKing1A_LogDepots','TomaKing1A_LogTargets',
        'TomaKing1A_LogWalls','TomaKing1A_LogEmpty','TomaKing1A_LogMapASCII',
        # --------- AUFGABE 1A - KARTEN-KONFIGURATION - Error Handling ----------
        'TomaKing1A_ErrorNotEnoughCells','TomaKing1A_ErrorNoFreeCells',
        'TomaKing1A_ErrorNotConnected',
    ]
    for v in required:
        if v not in globals():
            raise ValueError(f"Config fehlt: {v}")
validate_config()