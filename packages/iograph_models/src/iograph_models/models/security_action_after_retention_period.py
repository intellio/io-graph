from __future__ import annotations
from enum import StrEnum


class SecurityActionAfterRetentionPeriod(StrEnum):
	none = "none"
	delete = "delete"
	startDispositionReview = "startDispositionReview"
	relabel = "relabel"
	unknownFutureValue = "unknownFutureValue"

