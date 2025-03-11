from __future__ import annotations
from enum import StrEnum


class FrontlineCloudPcAvailability(StrEnum):
	notApplicable = "notApplicable"
	available = "available"
	notAvailable = "notAvailable"
	unknownFutureValue = "unknownFutureValue"

