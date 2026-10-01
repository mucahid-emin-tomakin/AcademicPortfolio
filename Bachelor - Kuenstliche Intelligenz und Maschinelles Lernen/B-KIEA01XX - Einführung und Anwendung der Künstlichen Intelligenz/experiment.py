# !/usr/bin/env python
# -*- coding: utf-8 -*-
# experiment.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import csv
import io
import os
import contextlib
import statistics
from map import Map
from agent import create_agents
from depot import create_depots
from graph import Graph
from prolog import export_facts
from simulation import Simulation
from config import (
    # AUFGABE 1B - Agententypen # 5A
    TomaKing1B_TypeStandard,
    TomaKing1B_TypeExpress,
    # AUFGABE 2A - Nachrichtentypen # 5C
    TomaKing2A_MsgBid,
    # AUFGABE 5A - Experimente # 5A
    TomaKing5A_RunCount,
    TomaKing5A_StepCount,
    TomaKing5A_StartSeed,
    TomaKing5A_VerboseExperimental,
    # AUFGABE 5A - Agenten-Konfigurationen # 5A
    TomaKing5A_AgentConfigs,
    # AUFGABE 5A - Ergebnis-Pfade # 5A
    TomaKing5A_ResultCsvPath,
    TomaKing5A_PlotLieferzeitPath,
    TomaKing5A_PlotErfolgsquotePath,
    TomaKing5A_PlotPfadlaengePath,
    TomaKing5A_ResultDir,
    TomaKing5A_ImageDir,
    # AUFGABE 5A - Statistics # 5A
    TomaKing5A_StatKeyAvgDeliveryTime,
    TomaKing5A_StatKeySuccessRate,
    TomaKing5A_StatKeyAvgPathLength,
    TomaKing5A_StatKeyTotalPackages,
    TomaKing5A_StatKeyDelivered,
    TomaKing5A_StatKeyExpired,
    TomaKing5A_StatKeyStdDelivery,
    TomaKing5A_StatKeyStdSuccess,
    TomaKing5A_StatKeyStdPath,
    # AUFGABE 5A - CSV # 5A
    TomaKing5A_CsvHeaderLabels,
    TomaKing5A_CsvAgentStandardKey,
    TomaKing5A_CsvAgentExpressKey,
    TomaKing5A_CsvRunKey,
    TomaKing5A_CsvSeedKey,
    TomaKing5A_CsvDelimiter,
    # AUFGABE 5A - Plots # 5A
    TomaKing5A_PlotBackend,
    TomaKing5A_PlotBarColor,
    TomaKing5A_PlotBarWidth,
    TomaKing5A_PlotBarEdgeColor,
    TomaKing5A_PlotErrorBarCapSize,
    TomaKing5A_PlotErrorBarColor,
    TomaKing5A_PlotLineWidth,
    TomaKing5A_PlotGridAlpha,
    TomaKing5A_PlotFigureSize,
    TomaKing5A_PlotDpi,
    TomaKing5A_PlotTitleLieferzeit,
    TomaKing5A_PlotTitleErfolgsquote,
    TomaKing5A_PlotTitlePfadlaenge,
    TomaKing5A_PlotXLabel,
    TomaKing5A_PlotYLabelLieferzeit,
    TomaKing5A_PlotYLabelErfolgsquote,
    TomaKing5A_PlotYLabelPfadlaenge,
    TomaKing5A_PlotXLabels,
    # AUFGABE 5A - Logging # 5A
    TomaKing5A_LogRunHeaderTemplate,
    TomaKing5A_LogResultHeader,
    TomaKing5A_LogResultRowTemplate,
    TomaKing5A_LogAggregateHeaderTemplate,
    TomaKing5A_LogPlotSavedTemplate,
    TomaKing5A_LogCsvSavedTemplate,
    TomaKing5A_LogSepTemplate,
    TomaKing5A_LogSeparatorChar,
    TomaKing5A_LogSeparatorLength,
    # AUFGABE 5B - Histogramme # 5B
    TomaKing5B_HistogramBins,
    TomaKing5B_HistogramColor,
    TomaKing5B_HistogramEdgeColor, 
    TomaKing5B_HistogramAlpha,
    TomaKing5B_BoxplotColor,
    TomaKing5B_BoxplotEdgeColor,
    TomaKing5B_BoxplotMedianColor,
    # AUFGABE 5B - Ergebnis-Pfade # 5B
    TomaKing5B_ResultCsvPath,
    TomaKing5B_PlotExpandedHistoPath,
    TomaKing5B_PlotExpandedBoxPath,
    TomaKing5B_PlotTimeHistoPath,
    TomaKing5B_PlotTimeBoxPath,
    TomaKing5B_PlotTimeMaxPath,
    # AUFGABE 5B - Statistics # 5B
    TomaKing5B_StatKeyCallCount,
    TomaKing5B_StatKeyExpandedAvg,
    TomaKing5B_StatKeyExpandedMax,
    TomaKing5B_StatKeyTimeAvgMs,
    TomaKing5B_StatKeyTimeMaxMs,
    # AUFGABE 5B - Metric-Keys (intern) # 5B
    TomaKing5B_MetricKeyExpanded,
    TomaKing5B_MetricKeyTimeMs,
    TomaKing5B_RawAstarKey,
    # AUFGABE 5B - CSV # 5B
    TomaKing5B_CsvHeaderLabels,
    # AUFGABE 5B - Plots # 5B
    TomaKing5B_PlotTitleExpandedHisto,
    TomaKing5B_PlotTitleExpandedBox,
    TomaKing5B_PlotTitleTimeHisto,
    TomaKing5B_PlotTitleTimeBox,
    TomaKing5B_PlotTitleTimeMax,
    TomaKing5B_PlotXLabelExpanded,
    TomaKing5B_PlotXLabelTime,
    TomaKing5B_PlotYLabelFrequency,
    TomaKing5B_PlotYLabelMaxTime,
    # AUFGABE 5B - Logging # 5B
    TomaKing5B_LogCsvSavedTemplate,
    TomaKing5B_LogPlotSavedTemplate,
    TomaKing5B_LogResultHeader,
    TomaKing5B_LogResultRowTemplate,
    TomaKing5B_LogAggregateHeaderT,
    # AUFGABE 5C - Metric-Keys (intern) # 5C
    TomaKing5C_MetricKeyTaskId,
    TomaKing5C_MetricKeyMsgType,
    TomaKing5C_RawCommKey,
    # AUFGABE 5C - Statistics # 5C
    TomaKing5C_StatKeyMsgPerTaskAvg,
    TomaKing5C_StatKeyBiddersPerAucAvg,
    TomaKing5C_StatKeyTotalMessages,
    TomaKing5C_StatKeyTotalTasks,
    # AUFGABE 5C - CSV # 5C
    TomaKing5C_CsvHeaderLabels,
    # AUFGABE 5C - Ergebnis-Pfade # 5C
    TomaKing5C_ResultCsvPath,
    TomaKing5C_PlotMsgHistoPath,
    TomaKing5C_PlotBidHistoPath,
    TomaKing5C_PlotMsgBarPath,
    TomaKing5C_PlotBidBarPath,
    # AUFGABE 5C - Plots # 5C
    TomaKing5C_PlotTitleMsgHisto,
    TomaKing5C_PlotTitleBidHisto,
    TomaKing5C_PlotTitleMsgBar,
    TomaKing5C_PlotTitleBidBar,
    TomaKing5C_PlotXLabelMsg,
    TomaKing5C_PlotXLabelBid,
    TomaKing5C_PlotYLabelAvg,
    # AUFGABE 5C - Logging # 5C
    TomaKing5C_LogCsvSavedTemplate,
    TomaKing5C_LogPlotSavedTemplate,
    TomaKing5C_LogResultHeader,
    TomaKing5C_LogResultRowTemplate,
    TomaKing5C_LogAggregateHeaderT,
    # AUFGABE 5D - Metric-Keys (intern) # 5D
    TomaKing5D_RawCollisionKey,
    TomaKing5D_RawReplanKey,
    # AUFGABE 5D - Ergebnis-Pfade # 5D
    TomaKing5D_ResultCsvPath,
    TomaKing5D_PlotCollisionsPath,
    TomaKing5D_PlotReplansPath,
    TomaKing5D_PlotCombinedPath,
    # AUFGABE 5D - Statistics # 5D
    TomaKing5D_StatKeyCollisions,
    TomaKing5D_StatKeyReplans,
    TomaKing5D_StatKeyCollisionsPerStep,
    TomaKing5D_StatKeyReplansPerStep,
    # AUFGABE 5D - CSV # 5D
    TomaKing5D_CsvHeaderLabels,
    # AUFGABE 5D - Plots # 5D
    TomaKing5D_SecondSeriesColor,
    TomaKing5D_PlotTitleCollisions,
    TomaKing5D_PlotTitleReplans,
    TomaKing5D_PlotTitleCombined,
    TomaKing5D_PlotYLabelCount,
    TomaKing5D_PlotLegendCollisions,
    TomaKing5D_PlotLegendReplans,
    # AUFGABE 5D - Logging # 5D
    TomaKing5D_LogCsvSavedTemplate,
    TomaKing5D_LogPlotSavedTemplate,
    TomaKing5D_LogResultHeader,
    TomaKing5D_LogResultRowTemplate,
    TomaKing5D_LogAggregateHeaderT,
)
import matplotlib
# Backend nach Import setzen
matplotlib.use(TomaKing5A_PlotBackend)
import matplotlib.pyplot as plt

## =============================================================================
# ==================== AUFGABE 5A - EXPERIMENT-RUNNER ===========================
## =============================================================================

# Fuehrt einen einzelnen Simulationslauf aus und liefert die Statistik.
def _run_single(seed: int, n_standard: int, n_express: int) -> dict:
    with contextlib.redirect_stdout(io.StringIO()):
        map_instance = Map(seed=seed)
        export_facts(map_instance)
        agents = create_agents(map_instance, n_standard, n_express, seed)
        depots = create_depots(map_instance)
        graph = Graph(map_instance)
        simulation = Simulation(map_instance, agents, depots, graph, verbose=TomaKing5A_VerboseExperimental)
        for _ in range(TomaKing5A_StepCount):
            simulation.step()
        stats_5a = simulation.get_statistics() # 5B
        stats_5b = simulation.get_astar_statistics() # 5B
        stats_5c = simulation.get_communication_statistics() # 5C
        stats_5d = simulation.get_conflict_statistics() # 5D
        raw_metrics = simulation.get_astar_metrics_raw() # 5B
        raw_comm  = simulation.get_message_metrics_raw() # 5C
        raw_collisions = simulation.get_collision_events_raw() # 5D
        raw_replans    = simulation.get_replan_events_raw() # 5D
        return {**stats_5a, **stats_5b, **stats_5c, **stats_5d, # 5D
                TomaKing5B_RawAstarKey:     raw_metrics, # 5B
                TomaKing5C_RawCommKey:      raw_comm, # 5C
                TomaKing5D_RawCollisionKey: raw_collisions, # 5D
                TomaKing5D_RawReplanKey:    raw_replans} # 5D
# Fuehrt alle Konfigurationen und Runs aus und sammelt die Ergebnisse.
def run_experiments() -> list[dict]:
    results = []
    for config in TomaKing5A_AgentConfigs:
        n_standard = config[TomaKing1B_TypeStandard]
        n_express  = config[TomaKing1B_TypeExpress]
        for run_index in range(TomaKing5A_RunCount):
            seed = TomaKing5A_StartSeed + run_index
            print(TomaKing5A_LogRunHeaderTemplate.format(
                run_index + 1, TomaKing5A_RunCount,
                n_standard + n_express, n_standard, n_express, seed))
            stats = _run_single(seed, n_standard, n_express)
            results.append({
                TomaKing5A_CsvAgentStandardKey: n_standard,
                TomaKing5A_CsvAgentExpressKey:  n_express,
                TomaKing5A_CsvRunKey:           run_index + 1,
                TomaKing5A_CsvSeedKey:          seed,
                **stats,
            })
    return results
# Aggregiert die Ergebnisse pro Agentenkonfiguration.
def _aggregate(results: list[dict]) -> list[dict]:
    grouped = {}
    for row in results:
        key = (row[TomaKing5A_CsvAgentStandardKey], row[TomaKing5A_CsvAgentExpressKey])
        grouped.setdefault(key, []).append(row)
    aggregated = []
    for (n_std, n_exp), rows in grouped.items():
        agg = {
            TomaKing5A_CsvAgentStandardKey:     n_std,
            TomaKing5A_CsvAgentExpressKey:      n_exp,
            TomaKing5A_StatKeyAvgDeliveryTime:  statistics.mean(r[TomaKing5A_StatKeyAvgDeliveryTime] for r in rows),
            TomaKing5A_StatKeySuccessRate:      statistics.mean(r[TomaKing5A_StatKeySuccessRate] for r in rows),
            TomaKing5A_StatKeyAvgPathLength:    statistics.mean(r[TomaKing5A_StatKeyAvgPathLength] for r in rows),
            TomaKing5A_StatKeyStdDelivery:      statistics.stdev(r[TomaKing5A_StatKeyAvgDeliveryTime] for r in rows) if len(rows) > 1 else 0.0,
            TomaKing5A_StatKeyStdSuccess:       statistics.stdev(r[TomaKing5A_StatKeySuccessRate] for r in rows) if len(rows) > 1 else 0.0,
            TomaKing5A_StatKeyStdPath:          statistics.stdev(r[TomaKing5A_StatKeyAvgPathLength] for r in rows) if len(rows) > 1 else 0.0,
        }
        aggregated.append(agg)
    return aggregated
# Schreibt die Ergebnisse als CSV.
def _write_csv(results: list[dict]) -> None:
    os.makedirs(TomaKing5A_ResultDir, exist_ok=True)
    with open(TomaKing5A_ResultCsvPath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=TomaKing5A_CsvHeaderLabels,
                            delimiter=TomaKing5A_CsvDelimiter)
        writer.writeheader()
        for row in results:
            writer.writerow({k: row[k] for k in TomaKing5A_CsvHeaderLabels})
    print(TomaKing5A_LogCsvSavedTemplate.format(TomaKing5A_ResultCsvPath))
# Erzeugt einen Bar-Chart mit Fehlerbalken.
def _make_plot(aggregated, value_key, std_key, title, ylabel, path) -> None:
    os.makedirs(TomaKing5A_ImageDir, exist_ok=True)
    xs = TomaKing5A_PlotXLabels
    ys = [row[value_key] for row in aggregated]
    errs = [row[std_key] for row in aggregated]
    fig, ax = plt.subplots(figsize=TomaKing5A_PlotFigureSize)
    ax.bar(xs, ys, width=TomaKing5A_PlotBarWidth,
           color=TomaKing5A_PlotBarColor,
           edgecolor=TomaKing5A_PlotBarEdgeColor,
           yerr=errs, capsize=TomaKing5A_PlotErrorBarCapSize,
           error_kw={"ecolor": TomaKing5A_PlotErrorBarColor,
                     "linewidth": TomaKing5A_PlotLineWidth})
    ax.set_title(title)
    ax.set_xlabel(TomaKing5A_PlotXLabel)
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", alpha=TomaKing5A_PlotGridAlpha)
    fig.savefig(path, dpi=TomaKing5A_PlotDpi, bbox_inches="tight")
    plt.close(fig)
    print(TomaKing5A_LogPlotSavedTemplate.format(path))
# Gibt die aggregierten Ergebnisse auf der Konsole aus.
def _print_aggregate(aggregated) -> None:
    sep = TomaKing5A_LogSeparatorChar * TomaKing5A_LogSeparatorLength
    print(TomaKing5A_LogSepTemplate.format(sep))
    print(TomaKing5A_LogAggregateHeaderTemplate.format(TomaKing5A_RunCount))
    print(TomaKing5A_LogSepTemplate.format(sep))
    print(TomaKing5A_LogResultHeader)
    for row in aggregated:
        print(TomaKing5A_LogResultRowTemplate.format(
            row[TomaKing5A_CsvAgentStandardKey],
            row[TomaKing5A_CsvAgentExpressKey],
            row[TomaKing5A_StatKeyAvgDeliveryTime],
            row[TomaKing5A_StatKeySuccessRate],
            row[TomaKing5A_StatKeyAvgPathLength]))
    print(TomaKing5A_LogSepTemplate.format(sep))

## =============================================================================
# ==================== AUFGABE 5B - A*-AUSWERTUNG ===============================
## =============================================================================

# Schreibt die aggregierten A*-Kennzahlen als CSV.
def _write_csv_5b(results: list[dict]) -> None:
    os.makedirs(TomaKing5A_ResultDir, exist_ok=True)
    with open(TomaKing5B_ResultCsvPath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=TomaKing5B_CsvHeaderLabels,
                            delimiter=TomaKing5A_CsvDelimiter)
        writer.writeheader()
        for row in results:
            writer.writerow({k: row[k] for k in TomaKing5B_CsvHeaderLabels})
    print(TomaKing5B_LogCsvSavedTemplate.format(TomaKing5B_ResultCsvPath))
# Aggregiert die A*-Kennzahlen pro Agentenkonfiguration.
def _aggregate_5b(results: list[dict]) -> list[dict]:
    grouped = {}
    for row in results:
        key = (row[TomaKing5A_CsvAgentStandardKey], row[TomaKing5A_CsvAgentExpressKey])
        grouped.setdefault(key, []).append(row)
    aggregated = []
    for (n_std, n_exp), rows in grouped.items():
        aggregated.append({
            TomaKing5A_CsvAgentStandardKey: n_std,
            TomaKing5A_CsvAgentExpressKey:  n_exp,
            TomaKing5B_StatKeyCallCount:    statistics.mean(r[TomaKing5B_StatKeyCallCount] for r in rows),
            TomaKing5B_StatKeyExpandedAvg:  statistics.mean(r[TomaKing5B_StatKeyExpandedAvg] for r in rows),
            TomaKing5B_StatKeyExpandedMax:  max(r[TomaKing5B_StatKeyExpandedMax] for r in rows),
            TomaKing5B_StatKeyTimeAvgMs:    statistics.mean(r[TomaKing5B_StatKeyTimeAvgMs] for r in rows),
            TomaKing5B_StatKeyTimeMaxMs:    max(r[TomaKing5B_StatKeyTimeMaxMs] for r in rows),
        })
    return aggregated
# Sammelt alle Rohwerte fuer Histogramme und Boxplots (pro Konfiguration).
def _collect_5b_raw(results: list[dict]) -> dict:
    all_expanded = []
    all_times = []
    per_config_expanded = []
    per_config_times = []
    config_order = []
    for cfg in TomaKing5A_AgentConfigs:
        total = cfg[TomaKing1B_TypeStandard] + cfg[TomaKing1B_TypeExpress]
        config_order.append(total)
        per_config_expanded.append([])
        per_config_times.append([])
    for row in results:
        total = row[TomaKing5A_CsvAgentStandardKey] + row[TomaKing5A_CsvAgentExpressKey]
        idx = config_order.index(total)
        for m in row[TomaKing5B_RawAstarKey]:
            all_expanded.append(m[TomaKing5B_MetricKeyExpanded])
            all_times.append(m[TomaKing5B_MetricKeyTimeMs])
            per_config_expanded[idx].append(m[TomaKing5B_MetricKeyExpanded])
            per_config_times[idx].append(m[TomaKing5B_MetricKeyTimeMs])
    return {
        "all_expanded": all_expanded,
        "all_times": all_times,
        "per_config_expanded": per_config_expanded,
        "per_config_times": per_config_times,
    }
# Erzeugt ein Histogramm der uebergebenen Werte.
def _make_histogram_5b(values, path, title, xlabel, # 5C
                       log_template=TomaKing5B_LogPlotSavedTemplate) -> None: # 5C
    os.makedirs(TomaKing5A_ImageDir, exist_ok=True)
    fig, ax = plt.subplots(figsize=TomaKing5A_PlotFigureSize)
    ax.hist(values, bins=TomaKing5B_HistogramBins,
            color=TomaKing5B_HistogramColor,
            edgecolor=TomaKing5B_HistogramEdgeColor,
            alpha=TomaKing5B_HistogramAlpha)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(TomaKing5B_PlotYLabelFrequency)
    ax.grid(axis="y", alpha=TomaKing5A_PlotGridAlpha)
    fig.savefig(path, dpi=TomaKing5A_PlotDpi, bbox_inches="tight")
    plt.close(fig)
    print(log_template.format(path)) # 5C
# Erzeugt einen Boxplot pro Agentenkonfiguration.
def _make_boxplot_5b(per_config, path, title, ylabel) -> None:
    os.makedirs(TomaKing5A_ImageDir, exist_ok=True)
    fig, ax = plt.subplots(figsize=TomaKing5A_PlotFigureSize)
    bp = ax.boxplot(per_config, tick_labels=TomaKing5A_PlotXLabels, patch_artist=True)
    for patch in bp["boxes"]:
        patch.set_facecolor(TomaKing5B_BoxplotColor)
        patch.set_edgecolor(TomaKing5B_BoxplotEdgeColor)
    for median in bp["medians"]:
        median.set_color(TomaKing5B_BoxplotMedianColor)
        median.set_linewidth(TomaKing5A_PlotLineWidth)
    ax.set_title(title)
    ax.set_xlabel(TomaKing5A_PlotXLabel)
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", alpha=TomaKing5A_PlotGridAlpha)
    fig.savefig(path, dpi=TomaKing5A_PlotDpi, bbox_inches="tight")
    plt.close(fig)
    print(TomaKing5B_LogPlotSavedTemplate.format(path))
# Erzeugt ein Balkendiagramm der maximalen Planungszeit pro Konfiguration.
def _make_bar_5b(aggregated, path, title, ylabel) -> None:
    os.makedirs(TomaKing5A_ImageDir, exist_ok=True)
    xs = TomaKing5A_PlotXLabels
    ys = [row[TomaKing5B_StatKeyTimeMaxMs] for row in aggregated]
    fig, ax = plt.subplots(figsize=TomaKing5A_PlotFigureSize)
    ax.bar(xs, ys, width=TomaKing5A_PlotBarWidth,
           color=TomaKing5B_HistogramColor,
           edgecolor=TomaKing5A_PlotBarEdgeColor)
    ax.set_title(title)
    ax.set_xlabel(TomaKing5A_PlotXLabel)
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", alpha=TomaKing5A_PlotGridAlpha)
    fig.savefig(path, dpi=TomaKing5A_PlotDpi, bbox_inches="tight")
    plt.close(fig)
    print(TomaKing5B_LogPlotSavedTemplate.format(path))
# Gibt die aggregierten A*-Ergebnisse auf der Konsole aus.
def _print_aggregate_5b(aggregated) -> None:
    sep = TomaKing5A_LogSeparatorChar * TomaKing5A_LogSeparatorLength
    print(TomaKing5A_LogSepTemplate.format(sep))
    print(TomaKing5B_LogAggregateHeaderT.format(TomaKing5A_RunCount))
    print(TomaKing5A_LogSepTemplate.format(sep))
    print(TomaKing5B_LogResultHeader)
    for row in aggregated:
        print(TomaKing5B_LogResultRowTemplate.format(
            row[TomaKing5A_CsvAgentStandardKey],
            row[TomaKing5A_CsvAgentExpressKey],
            row[TomaKing5B_StatKeyCallCount],
            row[TomaKing5B_StatKeyExpandedAvg],
            row[TomaKing5B_StatKeyExpandedMax],
            row[TomaKing5B_StatKeyTimeAvgMs],
            row[TomaKing5B_StatKeyTimeMaxMs]))
    print(TomaKing5A_LogSepTemplate.format(sep))

## =============================================================================
# ============== AUFGABE 5C - KOMMUNIKATIONS-AUSWERTUNG =========================
## =============================================================================

# Schreibt die aggregierten Kommunikationskennzahlen als CSV.
def _write_csv_5c(results: list[dict]) -> None:
    os.makedirs(TomaKing5A_ResultDir, exist_ok=True)
    with open(TomaKing5C_ResultCsvPath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=TomaKing5C_CsvHeaderLabels,
                            delimiter=TomaKing5A_CsvDelimiter)
        writer.writeheader()
        for row in results:
            writer.writerow({k: row[k] for k in TomaKing5C_CsvHeaderLabels})
    print(TomaKing5C_LogCsvSavedTemplate.format(TomaKing5C_ResultCsvPath))
# Aggregiert die Kommunikationskennzahlen pro Agentenkonfiguration.
def _aggregate_5c(results: list[dict]) -> list[dict]:
    grouped = {}
    for row in results:
        key = (row[TomaKing5A_CsvAgentStandardKey], row[TomaKing5A_CsvAgentExpressKey])
        grouped.setdefault(key, []).append(row)
    aggregated = []
    for (n_std, n_exp), rows in grouped.items():
        aggregated.append({
            TomaKing5A_CsvAgentStandardKey:     n_std,
            TomaKing5A_CsvAgentExpressKey:      n_exp,
            TomaKing5C_StatKeyMsgPerTaskAvg:    statistics.mean(r[TomaKing5C_StatKeyMsgPerTaskAvg] for r in rows),
            TomaKing5C_StatKeyBiddersPerAucAvg: statistics.mean(r[TomaKing5C_StatKeyBiddersPerAucAvg] for r in rows),
            TomaKing5C_StatKeyTotalMessages:    statistics.mean(r[TomaKing5C_StatKeyTotalMessages] for r in rows),
            TomaKing5C_StatKeyTotalTasks:       statistics.mean(r[TomaKing5C_StatKeyTotalTasks] for r in rows),
        })
    return aggregated
# Sammelt die Rohwerte fuer Histogramme (Nachrichten und Bieter pro Task).
def _collect_5c_raw(results: list[dict]) -> dict:
    msgs_per_task = []
    bids_per_auction = []
    per_config_msgs = []
    per_config_bids = []
    config_order = []
    for cfg in TomaKing5A_AgentConfigs:
        total = cfg[TomaKing1B_TypeStandard] + cfg[TomaKing1B_TypeExpress]
        config_order.append(total)
        per_config_msgs.append([])
        per_config_bids.append([])
    for row in results:
        total = row[TomaKing5A_CsvAgentStandardKey] + row[TomaKing5A_CsvAgentExpressKey]
        idx = config_order.index(total)
        per_task = {}
        for m in row[TomaKing5C_RawCommKey]:
            tid = m[TomaKing5C_MetricKeyTaskId]
            per_task.setdefault(tid, []).append(m)
        for msgs in per_task.values():
            n_total = len(msgs)
            n_bids = sum(1 for m in msgs
                         if m[TomaKing5C_MetricKeyMsgType] == TomaKing2A_MsgBid)
            msgs_per_task.append(n_total)
            bids_per_auction.append(n_bids)
            per_config_msgs[idx].append(n_total)
            per_config_bids[idx].append(n_bids)
    return {
        "all_msgs": msgs_per_task,
        "all_bids": bids_per_auction,
        "per_config_msgs": per_config_msgs,
        "per_config_bids": per_config_bids,
    }
# Erzeugt ein Balkendiagramm fuer eine Kommunikationskennzahl.
def _make_bar_5c(aggregated, value_key, path, title, ylabel) -> None:
    os.makedirs(TomaKing5A_ImageDir, exist_ok=True)
    xs = TomaKing5A_PlotXLabels
    ys = [row[value_key] for row in aggregated]
    fig, ax = plt.subplots(figsize=TomaKing5A_PlotFigureSize)
    ax.bar(xs, ys, width=TomaKing5A_PlotBarWidth,
           color=TomaKing5B_HistogramColor,
           edgecolor=TomaKing5A_PlotBarEdgeColor)
    ax.set_title(title)
    ax.set_xlabel(TomaKing5A_PlotXLabel)
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", alpha=TomaKing5A_PlotGridAlpha)
    fig.savefig(path, dpi=TomaKing5A_PlotDpi, bbox_inches="tight")
    plt.close(fig)
    print(TomaKing5C_LogPlotSavedTemplate.format(path))
# Gibt die aggregierten Kommunikationsmetriken auf der Konsole aus.
def _print_aggregate_5c(aggregated) -> None:
    sep = TomaKing5A_LogSeparatorChar * TomaKing5A_LogSeparatorLength
    print(TomaKing5A_LogSepTemplate.format(sep))
    print(TomaKing5C_LogAggregateHeaderT.format(TomaKing5A_RunCount))
    print(TomaKing5A_LogSepTemplate.format(sep))
    print(TomaKing5C_LogResultHeader)
    for row in aggregated:
        print(TomaKing5C_LogResultRowTemplate.format(
            row[TomaKing5A_CsvAgentStandardKey],
            row[TomaKing5A_CsvAgentExpressKey],
            row[TomaKing5C_StatKeyMsgPerTaskAvg],
            row[TomaKing5C_StatKeyBiddersPerAucAvg],
            row[TomaKing5C_StatKeyTotalMessages],
            row[TomaKing5C_StatKeyTotalTasks]))
    print(TomaKing5A_LogSepTemplate.format(sep))

## =============================================================================
# ==================== AUFGABE 5D - KONFLIKT-AUSWERTUNG =========================
## =============================================================================

# Schreibt die aggregierten Konfliktkennzahlen als CSV.
def _write_csv_5d(results: list[dict]) -> None:
    os.makedirs(TomaKing5A_ResultDir, exist_ok=True)
    with open(TomaKing5D_ResultCsvPath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=TomaKing5D_CsvHeaderLabels,
                            delimiter=TomaKing5A_CsvDelimiter)
        writer.writeheader()
        for row in results:
            writer.writerow({k: row[k] for k in TomaKing5D_CsvHeaderLabels})
    print(TomaKing5D_LogCsvSavedTemplate.format(TomaKing5D_ResultCsvPath))
# Aggregiert die Konfliktkennzahlen pro Agentenkonfiguration.
def _aggregate_5d(results: list[dict]) -> list[dict]:
    grouped = {}
    for row in results:
        key = (row[TomaKing5A_CsvAgentStandardKey], row[TomaKing5A_CsvAgentExpressKey])
        grouped.setdefault(key, []).append(row)
    aggregated = []
    for (n_std, n_exp), rows in grouped.items():
        aggregated.append({
            TomaKing5A_CsvAgentStandardKey:      n_std,
            TomaKing5A_CsvAgentExpressKey:       n_exp,
            TomaKing5D_StatKeyCollisions:        statistics.mean(r[TomaKing5D_StatKeyCollisions] for r in rows),
            TomaKing5D_StatKeyReplans:           statistics.mean(r[TomaKing5D_StatKeyReplans] for r in rows),
            TomaKing5D_StatKeyCollisionsPerStep: statistics.mean(r[TomaKing5D_StatKeyCollisionsPerStep] for r in rows),
            TomaKing5D_StatKeyReplansPerStep:    statistics.mean(r[TomaKing5D_StatKeyReplansPerStep] for r in rows),
        })
    return aggregated
# Erzeugt ein einfaches Balkendiagramm fuer eine Konfliktkennzahl.
def _make_bar_5d(aggregated, value_key, path, title, ylabel) -> None:
    os.makedirs(TomaKing5A_ImageDir, exist_ok=True)
    xs = TomaKing5A_PlotXLabels
    ys = [row[value_key] for row in aggregated]
    fig, ax = plt.subplots(figsize=TomaKing5A_PlotFigureSize)
    ax.bar(xs, ys, width=TomaKing5A_PlotBarWidth,
           color=TomaKing5B_HistogramColor,
           edgecolor=TomaKing5A_PlotBarEdgeColor)
    ax.set_title(title)
    ax.set_xlabel(TomaKing5A_PlotXLabel)
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", alpha=TomaKing5A_PlotGridAlpha)
    fig.savefig(path, dpi=TomaKing5A_PlotDpi, bbox_inches="tight")
    plt.close(fig)
    print(TomaKing5D_LogPlotSavedTemplate.format(path))
# Erzeugt einen Doppelbalken-Vergleich fuer Kollisionen und Neuplanungen.
def _make_double_bar_5d(aggregated, path, title, ylabel,
                        label_a, label_b) -> None:
    import numpy as np
    os.makedirs(TomaKing5A_ImageDir, exist_ok=True)
    xs = TomaKing5A_PlotXLabels
    n = len(xs)
    width = TomaKing5A_PlotBarWidth / 2
    idx = np.arange(n)
    ys_a = [row[TomaKing5D_StatKeyCollisions] for row in aggregated]
    ys_b = [row[TomaKing5D_StatKeyReplans]    for row in aggregated]
    fig, ax = plt.subplots(figsize=TomaKing5A_PlotFigureSize)
    ax.bar(idx - width/2, ys_a, width=width,
           color=TomaKing5B_HistogramColor,
           edgecolor=TomaKing5A_PlotBarEdgeColor, label=label_a)
    ax.bar(idx + width/2, ys_b, width=width,
           color=TomaKing5D_SecondSeriesColor,
           edgecolor=TomaKing5A_PlotBarEdgeColor, label=label_b)
    ax.set_xticks(idx)
    ax.set_xticklabels(xs)
    ax.set_title(title)
    ax.set_xlabel(TomaKing5A_PlotXLabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    ax.grid(axis="y", alpha=TomaKing5A_PlotGridAlpha)
    fig.savefig(path, dpi=TomaKing5A_PlotDpi, bbox_inches="tight")
    plt.close(fig)
    print(TomaKing5D_LogPlotSavedTemplate.format(path))
# Gibt die aggregierten Konfliktkennzahlen auf der Konsole aus.
def _print_aggregate_5d(aggregated) -> None:
    sep = TomaKing5A_LogSeparatorChar * TomaKing5A_LogSeparatorLength
    print(TomaKing5A_LogSepTemplate.format(sep))
    print(TomaKing5D_LogAggregateHeaderT.format(TomaKing5A_RunCount))
    print(TomaKing5A_LogSepTemplate.format(sep))
    print(TomaKing5D_LogResultHeader)
    for row in aggregated:
        print(TomaKing5D_LogResultRowTemplate.format(
            row[TomaKing5A_CsvAgentStandardKey],
            row[TomaKing5A_CsvAgentExpressKey],
            row[TomaKing5D_StatKeyCollisions],
            row[TomaKing5D_StatKeyReplans],
            row[TomaKing5D_StatKeyCollisionsPerStep],
            row[TomaKing5D_StatKeyReplansPerStep]))
    print(TomaKing5A_LogSepTemplate.format(sep))

## =============================================================================
# ==================== AUFGABE 5A - DEMO-TESTLAUF ===============================
## =============================================================================

if __name__ == "__main__":
    results = run_experiments()
    _write_csv(results)
    aggregated = _aggregate(results)
    _print_aggregate(aggregated)
    _make_plot(aggregated, TomaKing5A_StatKeyAvgDeliveryTime, TomaKing5A_StatKeyStdDelivery,
               TomaKing5A_PlotTitleLieferzeit, TomaKing5A_PlotYLabelLieferzeit,
               TomaKing5A_PlotLieferzeitPath)
    _make_plot(aggregated, TomaKing5A_StatKeySuccessRate, TomaKing5A_StatKeyStdSuccess,
               TomaKing5A_PlotTitleErfolgsquote, TomaKing5A_PlotYLabelErfolgsquote,
               TomaKing5A_PlotErfolgsquotePath)
    _make_plot(aggregated, TomaKing5A_StatKeyAvgPathLength, TomaKing5A_StatKeyStdPath,
               TomaKing5A_PlotTitlePfadlaenge, TomaKing5A_PlotYLabelPfadlaenge,
               TomaKing5A_PlotPfadlaengePath)
    _write_csv_5b(results) # 5B
    aggregated_5b = _aggregate_5b(results) # 5B
    _print_aggregate_5b(aggregated_5b) # 5B
    raw = _collect_5b_raw(results) # 5B
    _make_histogram_5b(raw["all_expanded"], TomaKing5B_PlotExpandedHistoPath, # 5B
                       TomaKing5B_PlotTitleExpandedHisto, TomaKing5B_PlotXLabelExpanded) # 5B
    _make_boxplot_5b(raw["per_config_expanded"], TomaKing5B_PlotExpandedBoxPath, # 5B
                     TomaKing5B_PlotTitleExpandedBox, TomaKing5B_PlotXLabelExpanded) # 5B
    _make_histogram_5b(raw["all_times"], TomaKing5B_PlotTimeHistoPath, # 5B
                       TomaKing5B_PlotTitleTimeHisto, TomaKing5B_PlotXLabelTime) # 5B
    _make_boxplot_5b(raw["per_config_times"], TomaKing5B_PlotTimeBoxPath, # 5B
                     TomaKing5B_PlotTitleTimeBox, TomaKing5B_PlotXLabelTime) # 5B
    _make_bar_5b(aggregated_5b, TomaKing5B_PlotTimeMaxPath, # 5B
                 TomaKing5B_PlotTitleTimeMax, TomaKing5B_PlotYLabelMaxTime) # 5B
    _write_csv_5c(results) # 5C
    aggregated_5c = _aggregate_5c(results) # 5C
    _print_aggregate_5c(aggregated_5c) # 5C
    raw_c = _collect_5c_raw(results) # 5C
    _make_histogram_5b(raw_c["all_msgs"], TomaKing5C_PlotMsgHistoPath, # 5C
                       TomaKing5C_PlotTitleMsgHisto, TomaKing5C_PlotXLabelMsg, # 5C
                       log_template=TomaKing5C_LogPlotSavedTemplate) # 5C
    _make_histogram_5b(raw_c["all_bids"], TomaKing5C_PlotBidHistoPath, # 5C
                       TomaKing5C_PlotTitleBidHisto, TomaKing5C_PlotXLabelBid, # 5C
                       log_template=TomaKing5C_LogPlotSavedTemplate) # 5C
    _make_bar_5c(aggregated_5c, TomaKing5C_StatKeyMsgPerTaskAvg, # 5C
                 TomaKing5C_PlotMsgBarPath, # 5C
                 TomaKing5C_PlotTitleMsgBar, TomaKing5C_PlotYLabelAvg) # 5C
    _make_bar_5c(aggregated_5c, TomaKing5C_StatKeyBiddersPerAucAvg, # 5C
                 TomaKing5C_PlotBidBarPath, # 5C
                 TomaKing5C_PlotTitleBidBar, TomaKing5C_PlotYLabelAvg) # 5C
    _write_csv_5d(results) # 5D
    aggregated_5d = _aggregate_5d(results) # 5D
    _print_aggregate_5d(aggregated_5d) # 5D
    _make_bar_5d(aggregated_5d, TomaKing5D_StatKeyCollisions, # 5D
                 TomaKing5D_PlotCollisionsPath, # 5D
                 TomaKing5D_PlotTitleCollisions, TomaKing5D_PlotYLabelCount) # 5D
    _make_bar_5d(aggregated_5d, TomaKing5D_StatKeyReplans, # 5D
                 TomaKing5D_PlotReplansPath, # 5D
                 TomaKing5D_PlotTitleReplans, TomaKing5D_PlotYLabelCount) # 5D
    _make_double_bar_5d(aggregated_5d, TomaKing5D_PlotCombinedPath, # 5D
                        TomaKing5D_PlotTitleCombined, TomaKing5D_PlotYLabelCount, # 5D
                        TomaKing5D_PlotLegendCollisions, TomaKing5D_PlotLegendReplans) # 5D