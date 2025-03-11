from __future__ import annotations
from enum import StrEnum


class BookingStaffMembershipStatus(StrEnum):
	active = "active"
	pendingAcceptance = "pendingAcceptance"
	rejectedByStaff = "rejectedByStaff"
	unknownFutureValue = "unknownFutureValue"

