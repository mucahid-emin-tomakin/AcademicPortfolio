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
TomaKingGUI_InfoSeparator               = " │ "
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
TomaKingGUI_LogSeparatorCharEqual       = "="
TomaKingGUI_LogSeparatorCharLine        = "-"
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
# ==================== AUFGABE 1B - AGENTEN-KONFIGURATION =======================
## =============================================================================

# ------------------------------- Agententypen --------------------------------
TomaKing1B_TypeStandard                 = "Standard"
TomaKing1B_TypeExpress                  = "Express"
# ---------------------------- Agenten-ID-Vergabe -----------------------------
TomaKing1B_StartAgentId                 = 0
# ---------------------------------- Anzahl -----------------------------------
TomaKing1B_CountStandard                = 2
TomaKing1B_CountExpress                 = 2
TomaKing1B_Seed                         = TomaKing1A_Seed
# ------------------------------ Geschwindigkeit ------------------------------
TomaKing1B_SpeedStandard                = 1
TomaKing1B_SpeedExpress                 = 2
# --------------------------------- Kapazität ---------------------------------
TomaKing1B_CapacityStandard             = 5
TomaKing1B_CapacityExpress              = 3
TomaKing1B_InitialCargo                 = 0
# ------------------------------- Batteriestand -------------------------------
TomaKing1B_BatteryStandard              = 100
TomaKing1B_BatteryExpress               = 120
# ---------------------------------- Symbole ----------------------------------
TomaKing1B_SymbolStandard               = "S"
TomaKing1B_SymbolExpress                = "E"
# ---------------------------------- Farben -----------------------------------
TomaKing1B_ColorStandard                = "#403104"
TomaKing1B_ColorExpress                 = "#A07C0B"
TomaKing1B_RadiusFactor                 = 0.4
# ------------------------------- Anzeigetexte --------------------------------
TomaKing1B_LabelAgents                  = "Agenten: "
TomaKing1B_LabelStandard                = "S"
TomaKing1B_LabelExpress                 = "E"
TomaKing1B_LabelAgentParts              = "({}: {})"
# -------------------------------- Statistics ---------------------------------
TomaKing1B_StatKeyAgentCount            = "agent_count"
TomaKing1B_StatKeyStandardCount         = "standard_count"
TomaKing1B_StatKeyExpressCount          = "express_count"
TomaKing1B_StatKeyAgents                = "agents"
# ------------------------------- Repr-Template -------------------------------
TomaKing1B_ReprTemplate                 = "Agent(id={}, type={}, pos=({}, {}))"
# ---------------------------------- Logging ----------------------------------
TomaKing1B_LogColumnFormat              = " {:<5} | {:<9} | {:<11} | {:<7} | {:<10} | {:<9} | {:<7}"
TomaKing1B_LogAgentsHeaderLabels        = ("Agent", "Typ", "Position", "Speed", "Kapazität", "Batterie", "Ladung")
TomaKing1B_LogAgentPosition             = "({}, {})"
TomaKing1B_LogAgentBattery              = "{}/{}"
# ------------------------------ Error Handling -------------------------------
TomaKing1B_ErrorUnknownType             = "Unbekannter Agententyp: {}"
TomaKing1B_ErrorNotEnoughCellsForAgents = "Nicht genug freie Zellen für {} Agenten!"

## =============================================================================
# ==================== AUFGABE 1C - SIMULATIONS-KONFIGURATION ===================
## =============================================================================

# ----------------------------------- Seed ------------------------------------
TomaKing1C_Seed                         = TomaKing1A_Seed
# ------------------------------- Zeitsteuerung -------------------------------
TomaKing1C_StepDelay                    = 100
# --------------------------------- Batterie ----------------------------------
TomaKing1C_BatteryMoveBase              = 1
TomaKing1C_BatteryStandstill            = 0
# ------------------------------ Step-Log-Format ------------------------------
TomaKing1C_LogStepHeaderTemplate        = "--- Step {} ---"
# ------------------------------- Button-Texte --------------------------------
TomaKing1C_ButtonStepText               = "Step"
TomaKing1C_ButtonAutoRunText            = "AutoRun"
TomaKing1C_ButtonStopText               = "Stop"
# ------------------------------- Button-Layout -------------------------------
TomaKing1C_ButtonFramePady              = 22
TomaKing1C_ButtonPaddingX               = 11
TomaKing1C_ButtonFont                   = TomaKingGUI_InfoFont
TomaKing1C_ButtonFontSize               = TomaKingGUI_InfoSize
# ------------------------------- Button-Farben -------------------------------
TomaKing1C_ColorButtonBg                = "#000000"
TomaKing1C_ColorButtonFg                = "#2CFF05"
TomaKing1C_ColorButtonActiveBg          = "#2CFF05"
TomaKing1C_ColorButtonActiveFg          = "#000000"
TomaKing1C_ColorButtonDisabledFg        = "#404040"
# ---------------------------------- Labels -----------------------------------
TomaKing1C_LabelStep                    = "Step: "
# -------------------------------- Statistics ---------------------------------
TomaKing1C_StatKeyStepCount             = "step_count"
# ---------------------------------- Logging ----------------------------------
TomaKing1C_LogSendTemplate              = "[SEND]    Agent {} -> Agent {} ({})"
TomaKing1C_LogReadTemplate              = "[READ]    Agent {} <- {} Message"
TomaKing1C_LogPickUpTemplate            = "[PICKUP]  Agent {} nimmt Paket {} auf (cargo {}->{})"
TomaKing1C_LogDeliverTemplate           = "[DELIVER] Agent {} liefert Paket {} ab (cargo {}->{})"
# ------------------------------ Error Handling -------------------------------
TomaKing1C_ErrorInvalidMessage          = "Ungültige Nachricht: Empfänger {} existiert nicht!"

## =============================================================================
# ================= AUFGABE 2A - KOMMUNIKATIONS-KONFIGURATION ===================
## =============================================================================

# ----------------------------- Nachrichtentypen ------------------------------
TomaKing2A_MsgAnnounce                  = "ANNOUNCE"
TomaKing2A_MsgBid                       = "BID"
TomaKing2A_MsgAward                     = "AWARD"
# ----------------------------- Payload-Schlüssel -----------------------------
TomaKing2A_KeyTaskId                    = "task_id"
TomaKing2A_KeyDestination               = "destination"
TomaKing2A_KeyDeadline                  = "deadline"
TomaKing2A_KeyAgentId                   = "agent_id"
TomaKing2A_KeyCost                      = "cost"
TomaKing2A_KeyAgent                     = "agent"
# ------------------------------- Depot-IDs -----------------------------------
TomaKing2A_StartDepotId                 = -1
TomaKing2A_DepotIdStep                  = -1
# ---------------------------- Depot-Repr-Template ----------------------------
TomaKing2A_ReprTemplate                 = "Depot(id={}, pos=({}, {}))"
# ---------------------------------- Logging ----------------------------------
TomaKing2A_LogAnnounceTemplate          = "[ANNOUNCE] Depot {} -> Agent {} (task={}, dest={}, deadline={})"  # 2C
TomaKing2A_LogBidTemplate               = "[BID]      Agent {} -> Depot {} (task={}, cost={})"
TomaKing2A_LogAwardTemplate             = "[AWARD]    Depot {} -> Agent {} (task={})"
TomaKing2A_LogDepotReadTemplate         = "[READ]    Depot {} <- {} Message"  # 2C
# ------------------------------ Error Handling -------------------------------
TomaKing2A_ErrorUnknownMessageType      = "Unbekannter Nachrichtentyp: {}"
TomaKing2A_ErrorDepotNotFound           = "Depot mit ID {} existiert nicht!"

## =============================================================================
# ===================== AUFGABE 2B - PAKET-KONFIGURATION ========================
## =============================================================================

# --------------------------------- Parameter ---------------------------------
TomaKing2B_PackageInterval              = 5
TomaKing2B_DeadlineDefault              = 15
# -------------------------------- Package-IDs --------------------------------
TomaKing2B_StartPackageId               = 0
TomaKing2B_PackageIdStep                = 1
# ------------------------------- Status-Werte --------------------------------
TomaKing2B_StatusPending                = "PENDING"
TomaKing2B_StatusAssigned               = "ASSIGNED"
TomaKing2B_StatusDelivered              = "DELIVERED"
TomaKing2B_StatusExpired                = "EXPIRED"
# --------------------------- Package-Repr-Template ---------------------------
TomaKing2B_ReprTemplate                 = "Package(id={}, depot={}, target={}, deadline={}, status={})"
# ---------------------------------- Logging ----------------------------------
TomaKing2B_LogGenerationTemplate        = "[PKG]      Paket {} erzeugt (depot={}, target={}, deadline={})"
# ------------------------------ Error Handling -------------------------------
TomaKing2B_ErrorNoDepots                = "Keine Depots vorhanden - Paketgenerierung nicht möglich!"
TomaKing2B_ErrorNoTargets               = "Keine Ziele vorhanden - Paketgenerierung nicht möglich!"

## =============================================================================
# ===================== AUFGABE 2C - BIETLOGIK-KONFIGURATION ====================
## =============================================================================

# ---------------------------------- Logging ----------------------------------
TomaKing2C_LogUnknownDepot              = "[WARN]     ANNOUNCE von unbekanntem Depot {} ignoriert"

## =============================================================================
# ==================== AUFGABE 2D - ZUSCHLAGS-KONFIGURATION =====================
## =============================================================================

# ---------------------------------- Logging ----------------------------------
TomaKing2D_LogAuctionTemplate           = "[AUCTION] Depot {} (Task {}): {} Bieter, Gewinner Agent {} (Kosten {})"
TomaKing2D_LogNoBidsTemplate            = "[AUCTION] Depot {} (Task {}): keine Bieter"

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
        'TomaKingGUI_LogSeparatorCharEqual','TomaKingGUI_LogSeparatorCharLine',
        'TomaKingGUI_LogSeparatorLength',
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
        # ---------- AUFGABE 1B - AGENTEN-KONFIGURATION - Agententypen ----------
        'TomaKing1B_TypeStandard','TomaKing1B_TypeExpress',
        # ------- AUFGABE 1B - AGENTEN-KONFIGURATION - Agenten-ID-Vergabe -------
        'TomaKing1B_StartAgentId',
        # ------------- AUFGABE 1B - AGENTEN-KONFIGURATION - Anzahl -------------
        'TomaKing1B_CountStandard','TomaKing1B_CountExpress','TomaKing1B_Seed',
        # -------- AUFGABE 1B - AGENTEN-KONFIGURATION - Geschwindigkeit ---------
        'TomaKing1B_SpeedStandard','TomaKing1B_SpeedExpress',
        # ----------- AUFGABE 1B - AGENTEN-KONFIGURATION - Kapazität ------------
        'TomaKing1B_CapacityStandard','TomaKing1B_CapacityExpress',
        'TomaKing1B_InitialCargo',
        # --------- AUFGABE 1B - AGENTEN-KONFIGURATION - Batteriestand ----------
        'TomaKing1B_BatteryStandard','TomaKing1B_BatteryExpress',
        # ------------ AUFGABE 1B - AGENTEN-KONFIGURATION - Symbole -------------
        'TomaKing1B_SymbolStandard','TomaKing1B_SymbolExpress',
        # ------------- AUFGABE 1B - AGENTEN-KONFIGURATION - Farben -------------
        'TomaKing1B_ColorStandard','TomaKing1B_ColorExpress',
        'TomaKing1B_RadiusFactor',
        # ---------- AUFGABE 1B - AGENTEN-KONFIGURATION - Anzeigetexte ----------
        'TomaKing1B_LabelAgents','TomaKing1B_LabelStandard',
        'TomaKing1B_LabelExpress','TomaKing1B_LabelAgentParts',
        # ----------- AUFGABE 1B - AGENTEN-KONFIGURATION - Statistics -----------
        'TomaKing1B_StatKeyAgentCount','TomaKing1B_StatKeyStandardCount',
        'TomaKing1B_StatKeyExpressCount','TomaKing1B_StatKeyAgents',
        # --------- AUFGABE 1B - AGENTEN-KONFIGURATION - Repr-Template ----------
        'TomaKing1B_ReprTemplate',
        # ------------ AUFGABE 1B - AGENTEN-KONFIGURATION - Logging -------------
        'TomaKing1B_LogColumnFormat','TomaKing1B_LogAgentsHeaderLabels',
        'TomaKing1B_LogAgentPosition','TomaKing1B_LogAgentBattery',
        # --------- AUFGABE 1B - AGENTEN-KONFIGURATION - Error Handling ---------
        'TomaKing1B_ErrorUnknownType','TomaKing1B_ErrorNotEnoughCellsForAgents',
        # ------------ AUFGABE 1C - SIMULATIONS-KONFIGURATION - Seed ------------
        'TomaKing1C_Seed',
        # ------- AUFGABE 1C - SIMULATIONS-KONFIGURATION - Zeitsteuerung --------
        'TomaKing1C_StepDelay',
        # ---------- AUFGABE 1C - SIMULATIONS-KONFIGURATION - Batterie ----------
        'TomaKing1C_BatteryMoveBase','TomaKing1C_BatteryStandstill',
        # ------ AUFGABE 1C - SIMULATIONS-KONFIGURATION - Step-Log-Format -------
        'TomaKing1C_LogStepHeaderTemplate',
        # -------- AUFGABE 1C - SIMULATIONS-KONFIGURATION - Button-Texte --------
        'TomaKing1C_ButtonStepText','TomaKing1C_ButtonAutoRunText',
        'TomaKing1C_ButtonStopText',
        # ------- AUFGABE 1C - SIMULATIONS-KONFIGURATION - Button-Layout --------
        'TomaKing1C_ButtonFramePady','TomaKing1C_ButtonPaddingX',
        'TomaKing1C_ButtonFont','TomaKing1C_ButtonFontSize',
        # ------- AUFGABE 1C - SIMULATIONS-KONFIGURATION - Button-Farben --------
        'TomaKing1C_ColorButtonBg','TomaKing1C_ColorButtonFg',
        'TomaKing1C_ColorButtonActiveBg','TomaKing1C_ColorButtonActiveFg',
        'TomaKing1C_ColorButtonDisabledFg',
        # ----------- AUFGABE 1C - SIMULATIONS-KONFIGURATION - Labels -----------
        'TomaKing1C_LabelStep',
        # --------- AUFGABE 1C - SIMULATIONS-KONFIGURATION - Statistics ---------
        'TomaKing1C_StatKeyStepCount',
        # ---------- AUFGABE 1C - SIMULATIONS-KONFIGURATION - Logging -----------
        'TomaKing1C_LogSendTemplate','TomaKing1C_LogReadTemplate',
        'TomaKing1C_LogPickUpTemplate','TomaKing1C_LogDeliverTemplate',
        # ------- AUFGABE 1C - SIMULATIONS-KONFIGURATION - Error Handling -------
        'TomaKing1C_ErrorInvalidMessage',
        # ---- AUFGABE 2A - KOMMUNIKATIONS-KONFIGURATION - Nachrichtentypen -----
        'TomaKing2A_MsgAnnounce','TomaKing2A_MsgBid','TomaKing2A_MsgAward',
        # ---- AUFGABE 2A - KOMMUNIKATIONS-KONFIGURATION - Payload-Schlüssel ----
        'TomaKing2A_KeyTaskId','TomaKing2A_KeyDestination','TomaKing2A_KeyDeadline',
        'TomaKing2A_KeyAgentId','TomaKing2A_KeyCost','TomaKing2A_KeyAgent',
        # -------- AUFGABE 2A - KOMMUNIKATIONS-KONFIGURATION - Depot-IDs --------
        'TomaKing2A_StartDepotId','TomaKing2A_DepotIdStep',
        # --- AUFGABE 2A - KOMMUNIKATIONS-KONFIGURATION - Depot-Repr-Template ---
        'TomaKing2A_ReprTemplate',
        # --------- AUFGABE 2A - KOMMUNIKATIONS-KONFIGURATION - Logging ---------
        'TomaKing2A_LogAnnounceTemplate','TomaKing2A_LogBidTemplate',
        'TomaKing2A_LogAwardTemplate','TomaKing2A_LogDepotReadTemplate',#2C
        # ----- AUFGABE 2A - KOMMUNIKATIONS-KONFIGURATION - Error Handling ------
        'TomaKing2A_ErrorUnknownMessageType','TomaKing2A_ErrorDepotNotFound',
        # ------------ AUFGABE 2B - PAKET-KONFIGURATION - Parameter -------------
        'TomaKing2B_PackageInterval','TomaKing2B_DeadlineDefault',
        # ----------- AUFGABE 2B - PAKET-KONFIGURATION - Package-IDs ------------
        'TomaKing2B_StartPackageId','TomaKing2B_PackageIdStep',
        # ----------- AUFGABE 2B - PAKET-KONFIGURATION - Status-Werte -----------
        'TomaKing2B_StatusPending','TomaKing2B_StatusAssigned',
        'TomaKing2B_StatusDelivered','TomaKing2B_StatusExpired',
        # -------AUFGABE 2B - PAKET-KONFIGURATION - Package-Repr-Template -------
        'TomaKing2B_ReprTemplate',
        # ------------- AUFGABE 2B - PAKET-KONFIGURATION - Logging --------------
        'TomaKing2B_LogGenerationTemplate',
        # ---------- AUFGABE 2B - PAKET-KONFIGURATION - Error Handling ----------
        'TomaKing2B_ErrorNoDepots','TomaKing2B_ErrorNoTargets',
        # ---------- AUFGABE 2C - BIETLOGIK-KONFIGURATION - Logging -------------
        'TomaKing2C_LogUnknownDepot',
        # -------- AUFGABE 2D - ZUSCHLAGS-KONFIGURATION - Logging ---------------
        'TomaKing2D_LogAuctionTemplate','TomaKing2D_LogNoBidsTemplate',
    ]
    for v in required:
        if v not in globals():
            raise ValueError(f"Config fehlt: {v}")
validate_config()