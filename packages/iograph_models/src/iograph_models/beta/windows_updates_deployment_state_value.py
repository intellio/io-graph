from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesDeploymentStateValue(StrEnum):
	scheduled = "scheduled"
	offering = "offering"
	paused = "paused"
	faulted = "faulted"
	archived = "archived"
	unknownFutureValue = "unknownFutureValue"

