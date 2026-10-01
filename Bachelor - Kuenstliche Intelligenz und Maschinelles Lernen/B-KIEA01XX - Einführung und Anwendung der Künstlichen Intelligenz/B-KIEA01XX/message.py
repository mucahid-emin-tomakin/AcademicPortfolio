# !/usr/bin/env python
# -*- coding: utf-8 -*-
# message.py

## =============================================================================
# =========================== AUFGABE 1C - MESSAGE CLASS ========================
## =============================================================================

class Message:
    # Kapselt eine Nachricht zwischen zwei Agenten (Sender, Empfänger, Typ, Nutzlast).
    def __init__(self, sender_id: int, receiver_id: int, msg_type: str, payload=None):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.msg_type = msg_type
        self.payload = payload
    # Eindeutige Repräsentation für Debugging.
    def __repr__(self) -> str:
        return f"Message(from={self.sender_id}, to={self.receiver_id}, type={self.msg_type})"