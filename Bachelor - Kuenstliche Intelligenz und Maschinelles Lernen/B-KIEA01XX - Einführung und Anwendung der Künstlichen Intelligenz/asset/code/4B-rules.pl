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

% =============================================================================
% ============================= AUFGABE 4B - SUCHE =============================
% =============================================================================

% Breitensuche mit globaler Seen-Liste (besucht jeden Knoten höchstens einmal).
reachable(From, To) :-
    reachable_bfs([From], [From], To).
% Basisfall: Ziel steht an der Spitze der Queue.
reachable_bfs([To|_], _, To).
% Rekursion: Kopf expandieren, unbesuchte Nachbarn in Queue und Seen einfügen.
reachable_bfs([Node|Rest], Seen, To) :-
    findall(Next, (vertex(Node, Next, _), \+ memberchk(Next, Seen)), Nexts),
    append(Seen, Nexts, SeenNew),
    append(Rest, Nexts, QueueNew),
    reachable_bfs(QueueNew, SeenNew, To).
% Manhattan-Distanz zwischen zwei Punkten.
manhattan((X1, Y1), (X2, Y2), D) :-
    D is abs(X1 - X2) + abs(Y1 - Y2).
% Kandidat: minimale Gesamtdistanz, Tie-Break ueber Agent-ID.
candidate_agent(task(Depot, Target), Agent) :-
    findall(D-A, (
        agent(A, X, Y, _, Capacity, Battery, Cargo),
        Cargo + 1 =< Capacity,
        Battery > 0,
        reachable((X, Y), Depot),
        reachable(Depot, Target),
        manhattan((X, Y), Depot, D1),
        manhattan(Depot, Target, D2),
        D is D1 + D2
    ), Candidates),
    Candidates \= [],
    min_member(D-A, Candidates),
    Agent = A.