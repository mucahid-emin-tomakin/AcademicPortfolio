% !/usr/bin/env swipl
% -*- mode: prolog -*-
% facts.pl

% =============================================================================
% ============================ AUFGABE 4A - FAKTEN =============================
% =============================================================================

% --- Richtungen (4-Nachbarschaft) ---
direction(0, 1).
...
% --- Kosten-Parameter ---
base_cost(1.0).
bottleneck_penalty(0.5).
bottleneck_max_neighbors(2).
% --- Befahrbare Felder ---
road(0, 0).
road(1, 0).
road(2, 0).
...
% --- Waende ---
wall(3, 2).
...
% --- Depots ---
depot(-1, 37, 13).
depot(-2, 43, 1).
% --- Ziele ---
target(0, 25, 0).
target(1, 36, 5).
target(2, 55, 4).
target(3, 70, 3).