from __future__ import annotations
from enum import StrEnum


class DefenderPotentiallyUnwantedAppAction(StrEnum):
	deviceDefault = "deviceDefault"
	block = "block"
	audit = "audit"

