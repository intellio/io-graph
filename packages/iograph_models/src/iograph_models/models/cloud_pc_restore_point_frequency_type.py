from __future__ import annotations
from enum import Enum


class CloudPcRestorePointFrequencyType(Enum):
	default = "default"
	fourHours = "fourHours"
	sixHours = "sixHours"
	twelveHours = "twelveHours"
	sixteenHours = "sixteenHours"
	twentyFourHours = "twentyFourHours"
	unknownFutureValue = "unknownFutureValue"

