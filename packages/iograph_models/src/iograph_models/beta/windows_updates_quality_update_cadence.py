from __future__ import annotations
from enum import StrEnum


class WindowsUpdatesQualityUpdateCadence(StrEnum):
	monthly = "monthly"
	outOfBand = "outOfBand"
	unknownFutureValue = "unknownFutureValue"

