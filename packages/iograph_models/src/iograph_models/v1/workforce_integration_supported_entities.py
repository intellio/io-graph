from __future__ import annotations
from enum import StrEnum


class WorkforceIntegrationSupportedEntities(StrEnum):
	none = "none"
	shift = "shift"
	swapRequest = "swapRequest"
	userShiftPreferences = "userShiftPreferences"
	openShift = "openShift"
	openShiftRequest = "openShiftRequest"
	offerShiftRequest = "offerShiftRequest"
	unknownFutureValue = "unknownFutureValue"
	timeCard = "timeCard"
	timeOffReason = "timeOffReason"
	timeOff = "timeOff"
	timeOffRequest = "timeOffRequest"

