from __future__ import annotations
from enum import Enum


class BookingReminderRecipients(Enum):
	allAttendees = "allAttendees"
	staff = "staff"
	customer = "customer"
	unknownFutureValue = "unknownFutureValue"

