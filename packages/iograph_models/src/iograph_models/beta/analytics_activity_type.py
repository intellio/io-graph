from __future__ import annotations
from enum import StrEnum


class AnalyticsActivityType(StrEnum):
	Email = "Email"
	Meeting = "Meeting"
	Focus = "Focus"
	Chat = "Chat"
	Call = "Call"

