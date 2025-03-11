from __future__ import annotations
from enum import StrEnum


class SynchronizationStatusCode(StrEnum):
	NotConfigured = "NotConfigured"
	NotRun = "NotRun"
	Active = "Active"
	Paused = "Paused"
	Quarantine = "Quarantine"

