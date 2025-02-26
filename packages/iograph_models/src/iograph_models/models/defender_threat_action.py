from __future__ import annotations
from enum import Enum


class DefenderThreatAction(Enum):
	deviceDefault = "deviceDefault"
	clean = "clean"
	quarantine = "quarantine"
	remove = "remove"
	allow = "allow"
	userDefined = "userDefined"
	block = "block"

