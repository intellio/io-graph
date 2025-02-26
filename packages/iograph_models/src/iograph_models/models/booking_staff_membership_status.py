from __future__ import annotations
from enum import Enum


class BookingStaffMembershipStatus(Enum):
	active = "active"
	pendingAcceptance = "pendingAcceptance"
	rejectedByStaff = "rejectedByStaff"
	unknownFutureValue = "unknownFutureValue"

