from __future__ import annotations
from enum import StrEnum


class CloudPcRestorePointFrequencyType(StrEnum):
	default = "default"
	fourHours = "fourHours"
	sixHours = "sixHours"
	twelveHours = "twelveHours"
	sixteenHours = "sixteenHours"
	twentyFourHours = "twentyFourHours"
	unknownFutureValue = "unknownFutureValue"

