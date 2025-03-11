from __future__ import annotations
from enum import StrEnum


class EligibilityFilteringEnabledEntities(StrEnum):
	none = "none"
	swapRequest = "swapRequest"
	offerShiftRequest = "offerShiftRequest"
	unknownFutureValue = "unknownFutureValue"
	timeOffReason = "timeOffReason"

