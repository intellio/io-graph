from __future__ import annotations
from enum import Enum


class TrainingAvailabilityStatus(Enum):
	unknown = "unknown"
	notAvailable = "notAvailable"
	available = "available"
	archive = "archive"
	delete = "delete"
	unknownFutureValue = "unknownFutureValue"

