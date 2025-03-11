from __future__ import annotations
from enum import StrEnum


class SecurityTimelineEventType(StrEnum):
	originalDelivery = "originalDelivery"
	systemTimeTravel = "systemTimeTravel"
	dynamicDelivery = "dynamicDelivery"
	userUrlClick = "userUrlClick"
	reprocessed = "reprocessed"
	zap = "zap"
	quarantineRelease = "quarantineRelease"
	air = "air"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"

