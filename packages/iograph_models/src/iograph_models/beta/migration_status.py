from __future__ import annotations
from enum import StrEnum


class MigrationStatus(StrEnum):
	ready = "ready"
	needsReview = "needsReview"
	additionalStepsRequired = "additionalStepsRequired"
	unknownFutureValue = "unknownFutureValue"

