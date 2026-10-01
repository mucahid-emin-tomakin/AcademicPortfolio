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
TomaKing1B_BatteryStandard              = 300 # 5A (erhöht von 100 auf 300)
TomaKing1B_BatteryExpress               = 400 # 5A (erhöht von 120 auf 400)
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
TomaKing2B_PackageInterval              = 10 # 5A (erhöht von 5 auf 10)
TomaKing2B_DeadlineDefault              = 100 # 5A (erhöht von 15 auf 100)
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
# ==================== AUFGABE 3A - GRAPH-KONFIGURATION =========================
## =============================================================================

# ------------------------------- Kosten-Modell -------------------------------
TomaKing3A_BaseCost                     = 1.0
# ---------------------------------- Engpass ----------------------------------
TomaKing3A_BottleneckMaxNeighbors       = 2
TomaKing3A_BottleneckPenalty            = 0.5
# ---------------------------------- Sample -----------------------------------
TomaKing3A_SampleSize                   = 3
# ---------------------------------- Logging ----------------------------------
TomaKing3A_LogNodeCountTemplate         = "[GRAPH]    Knoten:              {}"
TomaKing3A_LogEdgeCountTemplate         = "[GRAPH]    Kanten:              {}"
TomaKing3A_LogBottleneckCountTemplate   = "[GRAPH]    Engpässe:            {}"
TomaKing3A_LogSampleHeader              = "[GRAPH]    Beispiel-Nachbarschaften:"
TomaKing3A_LogSampleNodeTemplate        = "[GRAPH]      Knoten {}:"
TomaKing3A_LogSampleEdgeTemplate        = "[GRAPH]        -> {}: Standard {:.2f}, Express {:.2f}"

## =============================================================================
# ==================== AUFGABE 3B - A*-KONFIGURATION ============================
## =============================================================================

# -------------------------- Algorithmus-Parameter ----------------------------
TomaKing3B_InitialCost                  = 0.0

## =============================================================================
# ==================== AUFGABE 3C - AGENTEN-INTEGRATION =========================
## =============================================================================

# ---------------------------------- Phasen -----------------------------------
TomaKing3C_PhaseToDepot                 = "TO_DEPOT"
TomaKing3C_PhaseToTarget                = "TO_TARGET"
# ---------------------------------- Logging ----------------------------------
TomaKing3C_LogPlanDepotTemplate         = "[PLAN]      Agent {} -> Depot {} ({} Schritte, Kosten {:.1f})"
TomaKing3C_LogPlanTargetTemplate        = "[PLAN]      Agent {} -> Ziel {} ({} Schritte, Kosten {:.1f})"
TomaKing3C_LogReplanTemplate            = "[REPLAN]    Agent {} von {} nach {}"
TomaKing3C_LogNoPathTemplate            = "[PATH FAIL] Agent {}: kein Pfad zu {} - Task {} aufgegeben"
TomaKing3C_LogTaskCompleteTemplate      = "[DONE]      Agent {} hat Task {} abgeschlossen"

## =============================================================================
# ============ AUFGABE 3D - BEWEGLICHE HINDERNISSE & HEURISTIK =================
## =============================================================================

# ------------------------------ Heuristik-Modus ------------------------------
TomaKing3D_HeuristicMode                = "bfs"   # "manhattan" | "bfs"
TomaKing3D_ModeManhattan                = "manhattan"
TomaKing3D_ModeBFS                      = "bfs"

## =============================================================================
# ================= AUFGABE 4A - PROLOG-WISSENSBASIS ============================
## =============================================================================

# ---------------------------- Wissensbasis-Datei -----------------------------
TomaKing4A_RulesPath                    = "rules.pl"
TomaKing4A_FactsPath                    = "facts.pl"
# --------------------------------- Ziel-IDs ----------------------------------
TomaKing4A_StartTargetId                = 0
TomaKing4A_TargetIdStep                 = 1
# ----------------------------- Datei-Header ----------------------------------
TomaKing4A_ShebangLine                  = "% !/usr/bin/env swipl"
TomaKing4A_ModeLine                     = "% -*- mode: prolog -*-"
TomaKing4A_FactsTitle                   = " AUFGABE 4A - FAKTEN "
TomaKing4A_FactsFilename                = "facts.pl"
TomaKing4A_SeparatorLineTemplate        = "% {}"
TomaKing4A_TitleLineTemplate            = "% {}="
TomaKing4A_FilenameLineTemplate         = "% {}"
# ---------------------------- Abschnitts-Header ------------------------------
TomaKing4A_HeaderDirections             = "% --- Richtungen (4-Nachbarschaft) ---"
TomaKing4A_HeaderCostParameters         = "% --- Kosten-Parameter ---"
TomaKing4A_HeaderRoad                   = "% --- Befahrbare Felder ---"
TomaKing4A_HeaderWall                   = "% --- Waende ---"
TomaKing4A_HeaderDepot                  = "% --- Depots ---"
TomaKing4A_HeaderTarget                 = "% --- Ziele ---"
# ---------------------------- Fakten-Templates -------------------------------
TomaKing4A_FactDirectionTemplate        = "direction({}, {})."
TomaKing4A_FactBaseCostTemplate         = "base_cost({})."
TomaKing4A_FactBottleneckPenaltyT       = "bottleneck_penalty({})."
TomaKing4A_FactBottleneckMaxNeighborsT  = "bottleneck_max_neighbors({})."
TomaKing4A_FactRoadTemplate             = "road({}, {})."
TomaKing4A_FactWallTemplate             = "wall({}, {})."
TomaKing4A_FactDepotTemplate            = "depot({}, {}, {})."
TomaKing4A_FactTargetTemplate           = "target({}, {}, {})."
# ---------------------------------- Logging ----------------------------------
TomaKing4A_LogExportTemplate            = "[PROLOG]   Wissensbasis exportiert: {} ({} Zeilen)"
TomaKing4A_LogRoadCountTemplate         = "[PROLOG]   road/2:   {} Fakten"
TomaKing4A_LogWallCountTemplate         = "[PROLOG]   wall/2:   {} Fakten"
TomaKing4A_LogDepotCountTemplate        = "[PROLOG]   depot/3:  {} Fakten"
TomaKing4A_LogTargetCountTemplate       = "[PROLOG]   target/3: {} Fakten"

## =============================================================================
# ==================== AUFGABE 4C - PROLOG-BRUECKE ==============================
## =============================================================================

# ----------------------------- SWI-Prolog-Aufruf -----------------------------
TomaKing4C_SWIPrologPath            = "swipl"
TomaKing4C_SubprocessTimeout        = 5
TomaKing4C_SWIPrologArgsTemplate    = ["-g", "{}", "-t", "halt", "-q"]
# ------------------------- Wissensbasis-Vorbereitung -------------------------
TomaKing4C_ConsultRulesGoal         = "consult('rules.pl')"
TomaKing4C_ConsultAgentsGoal        = "consult('agents.pl')"
TomaKing4C_GoalSeparator            = ", "
# ---------------------------------- Dateien ----------------------------------
TomaKing4C_AgentsPath               = "agents.pl"
# --------------------------- PROLOG-Goal-Templates ---------------------------
TomaKing4C_GoalReachableTemplate    = "reachable(({},{}),({},{}))"
TomaKing4C_GoalCandidatesTemplate   = "candidate_agents(task(({},{}),({},{})),L)"
TomaKing4C_FactAgentTemplate        = "agent({},{},{},{},{},{},{})."
# ------------------------------ Antwort-Parsing ------------------------------
TomaKing4C_PrologAnswerTrue         = "true"
TomaKing4C_PrologAnswerFalse        = "false"
TomaKing4C_PrologListPrefix         = "L = ["
TomaKing4C_PrologListSuffix         = "]"
TomaKing4C_PrologListSeparator      = ","
# ---------------------------------- Logging ----------------------------------
TomaKing4C_LogReachableOKTemplate   = "[PROLOG]   reachable({}, {}) = true"
TomaKing4C_LogReachableFailTemplate = "[PROLOG]   reachable({}, {}) = false -> Paket verworfen"
TomaKing4C_LogCandidateQueryT       = "[PROLOG]   candidate_agents(task({}, {}), L) = {}"
TomaKing4C_LogNoCandidatesTemplate  = "[PROLOG]   Depot {}: keine Kandidaten fuer Task {}"
TomaKing4C_LogFallbackTemplate      = "[PROLOG]   Fallback auf Python-Logik (PROLOG-Aufruf fehlgeschlagen)"
TomaKing4C_LogExportAgentsTemplate  = "[PROLOG]   agents.pl exportiert: {} Agenten"
# ------------------------------ Error Handling -------------------------------
TomaKing4C_ErrorInvalidAnswer       = "Ungueltige PROLOG-Antwort: {}"

## =============================================================================
# ==================== AUFGABE 5A - LEISTUNGSKENNZAHLEN =========================
## =============================================================================

# ------------------------------ Experimente ----------------------------------
TomaKing5A_RunCount                 = 5
TomaKing5A_StepCount                = 200
TomaKing5A_StartSeed                = 42
TomaKing5A_BatteryRegen             = 2
TomaKing5A_VerboseDefault           = True
TomaKing5A_VerboseExperimental      = False
# -------------------------- Agenten-Konfigurationen --------------------------
# Liste von Dicts: {Agententyp: Anzahl}. Reihenfolge = Reihenfolge der Läufe.
TomaKing5A_AgentConfigs             = [
    {TomaKing1B_TypeStandard: 1, TomaKing1B_TypeExpress: 2},   # 3 Agenten
    {TomaKing1B_TypeStandard: 2, TomaKing1B_TypeExpress: 3},   # 5 Agenten
    {TomaKing1B_TypeStandard: 5, TomaKing1B_TypeExpress: 5},   # 10 Agenten
]
# -------------------------------- Ergebnis-Pfade -----------------------------
TomaKing5A_ResultCsvPath            = "asset/results/5A-Results.csv"
TomaKing5A_PlotLieferzeitPath       = "asset/image/5A-Lieferzeit.png"
TomaKing5A_PlotErfolgsquotePath     = "asset/image/5A-Erfolgsquote.png"
TomaKing5A_PlotPfadlaengePath       = "asset/image/5A-Pfadlaenge.png"
TomaKing5A_ResultDir                = "asset/results"
TomaKing5A_ImageDir                 = "asset/image"
# --------------------------------- Statistics ---------------------------------
TomaKing5A_StatKeyAvgDeliveryTime   = "avg_delivery_time"
TomaKing5A_StatKeySuccessRate       = "success_rate"
TomaKing5A_StatKeyAvgPathLength     = "avg_path_length"
TomaKing5A_StatKeyTotalPackages     = "total_packages"
TomaKing5A_StatKeyDelivered         = "delivered"
TomaKing5A_StatKeyExpired           = "expired"
TomaKing5A_StatKeyStdDelivery       = "std_delivery"
TomaKing5A_StatKeyStdSuccess        = "std_success"
TomaKing5A_StatKeyStdPath           = "std_path"
# ------------------------------------ CSV -------------------------------------
TomaKing5A_CsvHeaderLabels          = [
    "agents_standard", "agents_express", "run", "seed",
    "avg_delivery_time", "success_rate", "avg_path_length",
    "total_packages", "delivered", "expired",
]
TomaKing5A_CsvAgentStandardKey      = "agents_standard"
TomaKing5A_CsvAgentExpressKey       = "agents_express"
TomaKing5A_CsvRunKey                = "run"
TomaKing5A_CsvSeedKey               = "seed"
TomaKing5A_CsvDelimiter             = ";"
# ---------------------------------- Plots -------------------------------------
TomaKing5A_PlotBackend              = "Agg"
TomaKing5A_PlotBarColor             = "#2CFF05"
TomaKing5A_PlotBarWidth             = 0.6
TomaKing5A_PlotBarEdgeColor         = "#000000"
TomaKing5A_PlotErrorBarCapSize      = 5
TomaKing5A_PlotErrorBarColor        = "#404040"
TomaKing5A_PlotLineWidth            = 1.5
TomaKing5A_PlotGridAlpha            = 0.3
TomaKing5A_PlotFigureSize           = (8, 5)
TomaKing5A_PlotDpi                  = 150
TomaKing5A_PlotTitleLieferzeit      = "Durchschnittliche Lieferzeit"
TomaKing5A_PlotTitleErfolgsquote    = "Erfolgsquote"
TomaKing5A_PlotTitlePfadlaenge      = "Durchschnittliche Pfadlaenge pro Auftrag"
TomaKing5A_PlotXLabel               = "Anzahl Agenten"
TomaKing5A_PlotYLabelLieferzeit     = "Steps"
TomaKing5A_PlotYLabelErfolgsquote   = "Prozent"
TomaKing5A_PlotYLabelPfadlaenge     = "Zellen"
TomaKing5A_PlotXLabels              = ["3", "5", "10"]
# ---------------------------------- Logging ----------------------------------
TomaKing5A_LogRunHeaderTemplate     = "--- Run {}/{} | {} Agenten (S:{}, E:{}) | Seed: {} ---"
TomaKing5A_LogResultHeader          = "Konfig   | Lieferzeit | Erfolgsquote | Pfadlaenge"
TomaKing5A_LogResultRowTemplate     = "{:>4}S/{:<3}E | {:>10.1f} | {:>11.1f}% | {:>9.1f}"
TomaKing5A_LogAggregateHeaderTemplate = "--- Aggregierte Ergebnisse (Mittel ueber {} Runs) ---"
TomaKing5A_LogPlotSavedTemplate     = "[5A]      Plot gespeichert: {}"
TomaKing5A_LogCsvSavedTemplate      = "[5A]      CSV gespeichert: {}"
TomaKing5A_LogSepTemplate           = "{}"
TomaKing5A_LogSeparatorChar         = "-"
TomaKing5A_LogSeparatorLength       = 60

## =============================================================================
# ==================== AUFGABE 5B - A*-EIGENSCHAFTEN ============================
## =============================================================================

# -------------------------------- Histogramme --------------------------------
TomaKing5B_HistogramBins            = 30
TomaKing5B_HistogramColor           = "#2CFF05"
TomaKing5B_HistogramEdgeColor       = "#000000"
TomaKing5B_HistogramAlpha           = 0.75
TomaKing5B_BoxplotColor             = "#2CFF05"
TomaKing5B_BoxplotEdgeColor         = "#000000"
TomaKing5B_BoxplotMedianColor       = "#FE0000"
# ------------------------------ Ergebnis-Pfade -------------------------------
TomaKing5B_ResultCsvPath            = "asset/results/5B-Results.csv"
TomaKing5B_PlotExpandedHistoPath    = "asset/image/5B-ExpandedHistogram.png"
TomaKing5B_PlotExpandedBoxPath      = "asset/image/5B-ExpandedBoxplot.png"
TomaKing5B_PlotTimeHistoPath        = "asset/image/5B-TimeHistogram.png"
TomaKing5B_PlotTimeBoxPath          = "asset/image/5B-TimeBoxplot.png"
TomaKing5B_PlotTimeMaxPath          = "asset/image/5B-TimeMax.png"
# -------------------------------- Statistics ---------------------------------
TomaKing5B_StatKeyCallCount         = "astar_call_count"
TomaKing5B_StatKeyExpandedAvg       = "astar_expanded_avg"
TomaKing5B_StatKeyExpandedMin       = "astar_expanded_min"
TomaKing5B_StatKeyExpandedMax       = "astar_expanded_max"
TomaKing5B_StatKeyExpandedMedian    = "astar_expanded_median"
TomaKing5B_StatKeyTimeAvgMs         = "astar_time_avg_ms"
TomaKing5B_StatKeyTimeMaxMs         = "astar_time_max_ms"
TomaKing5B_StatKeyTimeMedianMs      = "astar_time_median_ms"
# ---------------------------- Metric-Keys (intern) ----------------------------
TomaKing5B_MetricKeyExpanded        = "expanded"
TomaKing5B_MetricKeyTimeMs          = "time_ms"
TomaKing5B_MetricKeyGoal            = "goal"
TomaKing5B_MetricKeyTaskId          = "task_id"
TomaKing5B_MetricKeyStep            = "step"
TomaKing5B_RawAstarKey              = "_raw_astar"
# ------------------------------- Zeiteinheiten --------------------------------
TomaKing5B_MsPerSecond              = 1000.0
# ------------------------------------ CSV ------------------------------------
TomaKing5B_CsvHeaderLabels          = [
    "agents_standard", "agents_express", "run", "seed",
    "astar_call_count", "astar_expanded_avg", "astar_expanded_max",
    "astar_time_avg_ms", "astar_time_max_ms",
]
# ----------------------------------- Plots -----------------------------------
TomaKing5B_PlotTitleExpandedHisto   = "Verteilung der expandierten Knoten"
TomaKing5B_PlotTitleExpandedBox     = "Expandierte Knoten pro Konfiguration"
TomaKing5B_PlotTitleTimeHisto       = "Verteilung der Planungszeit"
TomaKing5B_PlotTitleTimeBox         = "Planungszeit pro Konfiguration"
TomaKing5B_PlotTitleTimeMax         = "Maximale Planungszeit pro Konfiguration"
TomaKing5B_PlotXLabelExpanded       = "Expandierte Knoten"
TomaKing5B_PlotXLabelTime           = "Planungszeit [ms]"
TomaKing5B_PlotYLabelFrequency      = "Haeufigkeit"
TomaKing5B_PlotYLabelMaxTime        = "Max. Planungszeit [ms]"
# ---------------------------------- Logging ----------------------------------
TomaKing5B_LogCsvSavedTemplate      = "[5B]      CSV gespeichert: {}"
TomaKing5B_LogPlotSavedTemplate     = "[5B]      Plot gespeichert: {}"
TomaKing5B_LogResultHeader          = "Konfig   | Calls | Exp.Avg | Exp.Max | Zeit Avg | Zeit Max"
TomaKing5B_LogResultRowTemplate     = "{:>4}S/{:<3}E | {:>5} | {:>7.1f} | {:>7} | {:>7.3f}ms | {:>7.3f}ms"
TomaKing5B_LogAggregateHeaderT      = "--- A*-Metriken (Mittel ueber {} Runs) ---"

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
        # --------- AUFGABE 3A - GRAPH-KONFIGURATION - Kosten-Modell ------------
        'TomaKing3A_BaseCost',
        # --------- AUFGABE 3A - GRAPH-KONFIGURATION - Engpass -----------------
        'TomaKing3A_BottleneckMaxNeighbors','TomaKing3A_BottleneckPenalty',
        # --------- AUFGABE 3A - GRAPH-KONFIGURATION - Sample ------------------
        'TomaKing3A_SampleSize',
        # --------- AUFGABE 3A - GRAPH-KONFIGURATION - Logging -----------------
        'TomaKing3A_LogNodeCountTemplate','TomaKing3A_LogEdgeCountTemplate',
        'TomaKing3A_LogBottleneckCountTemplate','TomaKing3A_LogSampleHeader',
        'TomaKing3A_LogSampleNodeTemplate','TomaKing3A_LogSampleEdgeTemplate',
        # ----------- AUFGABE 3B - A*-KONFIGURATION - Algorithmus --------------
        'TomaKing3B_InitialCost',
        # ------------- AUFGABE 3C - AGENTEN-INTEGRATION - Phasen --------------
        'TomaKing3C_PhaseToDepot','TomaKing3C_PhaseToTarget',
        # ------------- AUFGABE 3C - AGENTEN-INTEGRATION - Logging -------------
        'TomaKing3C_LogPlanDepotTemplate','TomaKing3C_LogPlanTargetTemplate',
        'TomaKing3C_LogReplanTemplate','TomaKing3C_LogNoPathTemplate',
        'TomaKing3C_LogTaskCompleteTemplate',
        # -------------- AUFGABE 3D - HEURISTIK - Heuristik-Modus --------------
        'TomaKing3D_HeuristicMode','TomaKing3D_ModeManhattan','TomaKing3D_ModeBFS',
        # ------- AUFGABE 4A - PROLOG-WISSENSBASIS - Wissensbasis-Datei --------
        'TomaKing4A_RulesPath','TomaKing4A_FactsPath',
        # ------------ AUFGABE 4A - PROLOG-WISSENSBASIS - Ziel-IDs -------------
        'TomaKing4A_StartTargetId','TomaKing4A_TargetIdStep',
        # ------- AUFGABE 4A - PROLOG-WISSENSBASIS - Datei-Header --------------
        'TomaKing4A_ShebangLine','TomaKing4A_ModeLine',
        'TomaKing4A_FactsTitle','TomaKing4A_FactsFilename',
        'TomaKing4A_SeparatorLineTemplate','TomaKing4A_TitleLineTemplate',
        'TomaKing4A_FilenameLineTemplate',
        # ------- AUFGABE 4A - PROLOG-WISSENSBASIS - Abschnitts-Header ---------
        'TomaKing4A_HeaderDirections','TomaKing4A_HeaderCostParameters',
        'TomaKing4A_HeaderRoad','TomaKing4A_HeaderWall',
        'TomaKing4A_HeaderDepot','TomaKing4A_HeaderTarget',
        # ------- AUFGABE 4A - PROLOG-WISSENSBASIS - Fakten-Templates ----------
        'TomaKing4A_FactDirectionTemplate','TomaKing4A_FactBaseCostTemplate',
        'TomaKing4A_FactBottleneckPenaltyT',
        'TomaKing4A_FactBottleneckMaxNeighborsT',
        'TomaKing4A_FactRoadTemplate','TomaKing4A_FactWallTemplate',
        'TomaKing4A_FactDepotTemplate','TomaKing4A_FactTargetTemplate',
        # ------------- AUFGABE 4A - PROLOG-WISSENSBASIS - Logging -------------
        'TomaKing4A_LogExportTemplate','TomaKing4A_LogRoadCountTemplate',
        'TomaKing4A_LogWallCountTemplate','TomaKing4A_LogDepotCountTemplate',
        'TomaKing4A_LogTargetCountTemplate',
        # ---------- AUFGABE 4C - PROLOG-BRUECKE - SWI-Prolog-Aufruf -----------
        'TomaKing4C_SWIPrologPath','TomaKing4C_SubprocessTimeout',
        'TomaKing4C_SWIPrologArgsTemplate',
        # ------ AUFGABE 4C - PROLOG-BRUECKE - Wissensbasis-Vorbereitung -------
        'TomaKing4C_ConsultRulesGoal','TomaKing4C_ConsultAgentsGoal',
        'TomaKing4C_GoalSeparator',
        # --------------- AUFGABE 4C - PROLOG-BRUECKE - Dateien ----------------
        'TomaKing4C_AgentsPath',
        # -------- AUFGABE 4C - PROLOG-BRUECKE - PROLOG-Goal-Templates ---------
        'TomaKing4C_GoalReachableTemplate','TomaKing4C_GoalCandidatesTemplate',
        'TomaKing4C_FactAgentTemplate',
        # ----------- AUFGABE 4C - PROLOG-BRUECKE - Antwort-Parsing ------------
        'TomaKing4C_PrologAnswerTrue','TomaKing4C_PrologAnswerFalse',
        'TomaKing4C_PrologListPrefix','TomaKing4C_PrologListSuffix',
        'TomaKing4C_PrologListSeparator',
        # --------------- AUFGABE 4C - PROLOG-BRUECKE - Logging ----------------
        'TomaKing4C_LogReachableOKTemplate','TomaKing4C_LogReachableFailTemplate',
        'TomaKing4C_LogCandidateQueryT','TomaKing4C_LogNoCandidatesTemplate',
        'TomaKing4C_LogFallbackTemplate','TomaKing4C_LogExportAgentsTemplate',
        # ------------ AUFGABE 4C - PROLOG-BRUECKE - Error Handling ------------
        'TomaKing4C_ErrorInvalidAnswer',
        # ----------- AUFGABE 5A - LEISTUNGSKENNZAHLEN - Experimente -----------
        'TomaKing5A_RunCount','TomaKing5A_StepCount','TomaKing5A_StartSeed',
        'TomaKing5A_BatteryRegen','TomaKing5A_VerboseDefault',
        'TomaKing5A_VerboseExperimental',
        # ----- AUFGABE 5A - LEISTUNGSKENNZAHLEN - Agenten-Konfigurationen -----
        'TomaKing5A_AgentConfigs',
        # --------- AUFGABE 5A - LEISTUNGSKENNZAHLEN - Ergebnis-Pfade ----------
        'TomaKing5A_ResultCsvPath','TomaKing5A_PlotLieferzeitPath',
        'TomaKing5A_PlotErfolgsquotePath','TomaKing5A_PlotPfadlaengePath',
        'TomaKing5A_ResultDir','TomaKing5A_ImageDir',
        # ----------- AUFGABE 5A - LEISTUNGSKENNZAHLEN - Statistics ------------
        'TomaKing5A_StatKeyAvgDeliveryTime','TomaKing5A_StatKeySuccessRate',
        'TomaKing5A_StatKeyAvgPathLength','TomaKing5A_StatKeyTotalPackages',
        'TomaKing5A_StatKeyDelivered','TomaKing5A_StatKeyExpired',
        'TomaKing5A_StatKeyStdDelivery','TomaKing5A_StatKeyStdSuccess',
        'TomaKing5A_StatKeyStdPath',
        # --------------- AUFGABE 5A - LEISTUNGSKENNZAHLEN - CSV ---------------
        'TomaKing5A_CsvHeaderLabels','TomaKing5A_CsvAgentStandardKey',
        'TomaKing5A_CsvAgentExpressKey','TomaKing5A_CsvRunKey',
        'TomaKing5A_CsvSeedKey','TomaKing5A_CsvDelimiter',
        # -------------- AUFGABE 5A - LEISTUNGSKENNZAHLEN - Plots --------------
        'TomaKing5A_PlotBackend','TomaKing5A_PlotBarColor',
        'TomaKing5A_PlotBarWidth','TomaKing5A_PlotBarEdgeColor',
        'TomaKing5A_PlotErrorBarCapSize','TomaKing5A_PlotErrorBarColor',
        'TomaKing5A_PlotLineWidth','TomaKing5A_PlotGridAlpha',
        'TomaKing5A_PlotFigureSize','TomaKing5A_PlotDpi',
        'TomaKing5A_PlotTitleLieferzeit','TomaKing5A_PlotTitleErfolgsquote',
        'TomaKing5A_PlotTitlePfadlaenge','TomaKing5A_PlotXLabel',
        'TomaKing5A_PlotYLabelLieferzeit','TomaKing5A_PlotYLabelErfolgsquote',
        'TomaKing5A_PlotYLabelPfadlaenge','TomaKing5A_PlotXLabels',
        # ------------- AUFGABE 5A - LEISTUNGSKENNZAHLEN - Logging -------------
        'TomaKing5A_LogRunHeaderTemplate','TomaKing5A_LogResultHeader',
        'TomaKing5A_LogResultRowTemplate','TomaKing5A_LogAggregateHeaderTemplate',
        'TomaKing5A_LogPlotSavedTemplate','TomaKing5A_LogCsvSavedTemplate',
        'TomaKing5A_LogSepTemplate','TomaKing5A_LogSeparatorChar',
        'TomaKing5A_LogSeparatorLength',
        # ------------- AUFGABE 5B - A*-EIGENSCHAFTEN - Histogramme ------------
        'TomaKing5B_HistogramBins','TomaKing5B_HistogramColor',
        'TomaKing5B_HistogramEdgeColor','TomaKing5B_HistogramAlpha',
        'TomaKing5B_BoxplotColor','TomaKing5B_BoxplotEdgeColor',
        'TomaKing5B_BoxplotMedianColor',
        # ----------- AUFGABE 5B - A*-EIGENSCHAFTEN - Ergebnis-Pfade -----------
        'TomaKing5B_ResultCsvPath','TomaKing5B_PlotExpandedHistoPath',
        'TomaKing5B_PlotExpandedBoxPath','TomaKing5B_PlotTimeHistoPath',
        'TomaKing5B_PlotTimeBoxPath','TomaKing5B_PlotTimeMaxPath',
        # ------------- AUFGABE 5B - A*-EIGENSCHAFTEN - Statistics -------------
        'TomaKing5B_StatKeyCallCount','TomaKing5B_StatKeyExpandedAvg',
        'TomaKing5B_StatKeyExpandedMin','TomaKing5B_StatKeyExpandedMax',
        'TomaKing5B_StatKeyExpandedMedian','TomaKing5B_StatKeyTimeAvgMs',
        'TomaKing5B_StatKeyTimeMaxMs','TomaKing5B_StatKeyTimeMedianMs',
        # -------- AUFGABE 5B - A*-EIGENSCHAFTEN - Metric-Keys (intern) --------
        'TomaKing5B_MetricKeyExpanded','TomaKing5B_MetricKeyTimeMs',
        'TomaKing5B_MetricKeyGoal','TomaKing5B_MetricKeyTaskId',
        'TomaKing5B_MetricKeyStep','TomaKing5B_RawAstarKey',
        # ----------- AUFGABE 5B - A*-EIGENSCHAFTEN - Zeiteinheiten ------------
        'TomaKing5B_MsPerSecond',
        # ---------------- AUFGABE 5B - A*-EIGENSCHAFTEN - CSV -----------------
        'TomaKing5B_CsvHeaderLabels',
        # --------------- AUFGABE 5B - A*-EIGENSCHAFTEN - Plots ----------------
        'TomaKing5B_PlotTitleExpandedHisto','TomaKing5B_PlotTitleExpandedBox',
        'TomaKing5B_PlotTitleTimeHisto','TomaKing5B_PlotTitleTimeBox',
        'TomaKing5B_PlotTitleTimeMax',
        'TomaKing5B_PlotXLabelExpanded','TomaKing5B_PlotXLabelTime',
        'TomaKing5B_PlotYLabelFrequency','TomaKing5B_PlotYLabelMaxTime',
        # -------------- AUFGABE 5B - A*-EIGENSCHAFTEN - Logging ---------------
        'TomaKing5B_LogCsvSavedTemplate','TomaKing5B_LogPlotSavedTemplate',
        'TomaKing5B_LogResultHeader','TomaKing5B_LogResultRowTemplate',
        'TomaKing5B_LogAggregateHeaderT',
    ]
    for v in required:
        if v not in globals():
            raise ValueError(f"Config fehlt: {v}")
validate_config()