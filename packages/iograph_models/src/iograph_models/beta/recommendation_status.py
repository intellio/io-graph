from __future__ import annotations
from enum import StrEnum


class RecommendationStatus(StrEnum):
	active = "active"
	completedBySystem = "completedBySystem"
	completedByUser = "completedByUser"
	dismissed = "dismissed"
	postponed = "postponed"
	unknownFutureValue = "unknownFutureValue"

