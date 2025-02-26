from __future__ import annotations
from enum import Enum


class EligibilityFilteringEnabledEntities(Enum):
	none = "none"
	swapRequest = "swapRequest"
	offerShiftRequest = "offerShiftRequest"
	unknownFutureValue = "unknownFutureValue"
	timeOffReason = "timeOffReason"

