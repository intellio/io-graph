from __future__ import annotations
from enum import StrEnum


class BookingsServiceAvailabilityType(StrEnum):
	bookWhenStaffAreFree = "bookWhenStaffAreFree"
	notBookable = "notBookable"
	customWeeklyHours = "customWeeklyHours"
	unknownFutureValue = "unknownFutureValue"

