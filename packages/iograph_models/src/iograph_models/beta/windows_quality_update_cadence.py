from __future__ import annotations
from enum import StrEnum


class WindowsQualityUpdateCadence(StrEnum):
	monthly = "monthly"
	outOfBand = "outOfBand"
	unknownFutureValue = "unknownFutureValue"

