from __future__ import annotations
from enum import StrEnum


class BookingsAvailabilityStatus(StrEnum):
	available = "available"
	busy = "busy"
	slotsAvailable = "slotsAvailable"
	outOfOffice = "outOfOffice"
	unknownFutureValue = "unknownFutureValue"

