from __future__ import annotations
from enum import Enum


class MigrationStatus(Enum):
	ready = "ready"
	needsReview = "needsReview"
	additionalStepsRequired = "additionalStepsRequired"
	unknownFutureValue = "unknownFutureValue"

