from __future__ import annotations
from enum import StrEnum


class DefenderThreatAction(StrEnum):
	deviceDefault = "deviceDefault"
	clean = "clean"
	quarantine = "quarantine"
	remove = "remove"
	allow = "allow"
	userDefined = "userDefined"
	block = "block"

