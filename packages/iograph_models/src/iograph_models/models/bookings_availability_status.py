from __future__ import annotations
from enum import Enum


class BookingsAvailabilityStatus(Enum):
	available = "available"
	busy = "busy"
	slotsAvailable = "slotsAvailable"
	outOfOffice = "outOfOffice"
	unknownFutureValue = "unknownFutureValue"

