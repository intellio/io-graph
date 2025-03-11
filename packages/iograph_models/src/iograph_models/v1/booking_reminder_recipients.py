from __future__ import annotations
from enum import StrEnum


class BookingReminderRecipients(StrEnum):
	allAttendees = "allAttendees"
	staff = "staff"
	customer = "customer"
	unknownFutureValue = "unknownFutureValue"

