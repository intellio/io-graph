from __future__ import annotations
from enum import Enum


class BookingsServiceAvailabilityType(Enum):
	bookWhenStaffAreFree = "bookWhenStaffAreFree"
	notBookable = "notBookable"
	customWeeklyHours = "customWeeklyHours"
	unknownFutureValue = "unknownFutureValue"

