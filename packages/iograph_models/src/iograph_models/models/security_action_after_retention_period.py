from __future__ import annotations
from enum import Enum


class SecurityActionAfterRetentionPeriod(Enum):
	none = "none"
	delete = "delete"
	startDispositionReview = "startDispositionReview"
	relabel = "relabel"
	unknownFutureValue = "unknownFutureValue"

