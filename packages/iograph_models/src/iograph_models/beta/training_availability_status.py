from __future__ import annotations
from enum import StrEnum


class TrainingAvailabilityStatus(StrEnum):
	unknown = "unknown"
	notAvailable = "notAvailable"
	available = "available"
	archive = "archive"
	delete = "delete"
	unknownFutureValue = "unknownFutureValue"

