# !/usr/bin/env python
# -*- coding: utf-8 -*-
# query.py

## =============================================================================
# =================================== IMPORTS ===================================
## =============================================================================

import subprocess
from config import (
    # AUFGABE 4C - SWI-Prolog-Aufruf
    TomaKing4C_SWIPrologPath,
    TomaKing4C_SubprocessTimeout,
    TomaKing4C_SWIPrologArgsTemplate,
    # AUFGABE 4C - Wissensbasis-Vorbereitung
    TomaKing4C_ConsultRulesGoal,
    TomaKing4C_ConsultAgentsGoal,
    TomaKing4C_GoalSeparator,
    # AUFGABE 4C - Antwort-Parsing
    TomaKing4C_PrologAnswerTrue,
    TomaKing4C_PrologAnswerFalse,
    TomaKing4C_PrologListPrefix,
    TomaKing4C_PrologListSuffix,
    TomaKing4C_PrologListSeparator,
    # AUFGABE 4C - Logging
    TomaKing4C_LogFallbackTemplate,
    # AUFGABE 4C - Error Handling
    TomaKing4C_ErrorInvalidAnswer,
)

## =============================================================================
# ==================== AUFGABE 4C - PROLOG-BRUECKE ==============================
## =============================================================================

# Fuehrt einen Goal aus, laedt vorher Wissensbasis und Agentendaten.
def run_goal_with_consult(goal: str) -> str | None:
    combined = (TomaKing4C_ConsultRulesGoal
              + TomaKing4C_GoalSeparator
              + TomaKing4C_ConsultAgentsGoal
              + TomaKing4C_GoalSeparator
              + goal)
    return run_goal(combined)
# Fuehrt einen PROLOG-Goal aus und liefert die Rohausgabe als String.
def run_goal(goal: str) -> str | None:
    args = [TomaKing4C_SWIPrologPath]
    for arg in TomaKing4C_SWIPrologArgsTemplate:
        args.append(arg.format(goal))
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=TomaKing4C_SubprocessTimeout,
        )
    except FileNotFoundError:
        print(TomaKing4C_LogFallbackTemplate)
        return None
    except subprocess.TimeoutExpired:
        print(TomaKing4C_LogFallbackTemplate)
        return None
    return result.stdout.strip()
# Prueft, ob eine PROLOG-Antwort den Wahrheitswert true hat.
def is_true(answer: str) -> bool:
    return answer == TomaKing4C_PrologAnswerTrue
# Prueft, ob eine PROLOG-Antwort den Wahrheitswert false hat.
def is_false(answer: str) -> bool:
    return answer == TomaKing4C_PrologAnswerFalse
# Parst eine PROLOG-Listenantwort der Form "L = [1,2,3]" in eine int-Liste.
def parse_int_list(answer: str) -> list[int]:
    text = answer.strip()
    if not text.startswith(TomaKing4C_PrologListPrefix):
        raise ValueError(TomaKing4C_ErrorInvalidAnswer.format(answer))
    if not text.endswith(TomaKing4C_PrologListSuffix):
        raise ValueError(TomaKing4C_ErrorInvalidAnswer.format(answer))
    inner = text[len(TomaKing4C_PrologListPrefix):-len(TomaKing4C_PrologListSuffix)].strip()
    if not inner:
        return []
    return [int(part.strip()) for part in inner.split(TomaKing4C_PrologListSeparator)]