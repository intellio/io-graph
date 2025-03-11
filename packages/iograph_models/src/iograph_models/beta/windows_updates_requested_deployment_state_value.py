from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesRequestedDeploymentStateValue(StrEnum):
	none = "none"
	paused = "paused"
	archived = "archived"
	unknownFutureValue = "unknownFutureValue"

