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
        return simulation.get_statistics()
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