from __future__ import annotations
from enum import Enum


class VirtualEventAttendeeRegistrationStatus(Enum):
	registered = "registered"
	canceled = "canceled"
	waitlisted = "waitlisted"
	pendingApproval = "pendingApproval"
	rejectedByOrganizer = "rejectedByOrganizer"
	unknownFutureValue = "unknownFutureValue"

