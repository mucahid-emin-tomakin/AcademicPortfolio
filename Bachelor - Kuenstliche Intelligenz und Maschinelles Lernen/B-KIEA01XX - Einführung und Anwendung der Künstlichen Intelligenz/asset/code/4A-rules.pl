% !/usr/bin/env swipl
% -*- mode: prolog -*-
% rules.pl

% =============================================================================
% ============================ AUFGABE 4A - REGELN =============================
% =============================================================================

:- include("facts.pl").
% Nachbarzahl eines Knotens (befahrbare Nachbarn in 4-Richtung)
neighbor_count(X, Y, N) :-
    findall(_, (direction(DX, DY), NX is X + DX, NY is Y + DY, road(NX, NY)), L),
    length(L, N).
% Engpass-Zelle: befahrbarer Knoten mit hoechstens N_max Nachbarn
bottleneck(X, Y) :-
    road(X, Y),
    neighbor_count(X, Y, N),
    bottleneck_max_neighbors(Max),
    N =< Max.
% Kantenkosten: Basis-Kosten plus Engpass-Aufschlag der Zielzelle
cost(X, Y, Cost) :-
    base_cost(Base),
    (bottleneck(X, Y) -> bottleneck_penalty(P), Cost is Base + P ; Cost = Base).
% Kante zwischen zwei benachbarten, befahrbaren Knoten
vertex((X1, Y1), (X2, Y2), Cost) :-
    road(X1, Y1),
    direction(DX, DY),
    X2 is X1 + DX,
    Y2 is Y1 + DY,
    road(X2, Y2),
    cost(X2, Y2, Cost).