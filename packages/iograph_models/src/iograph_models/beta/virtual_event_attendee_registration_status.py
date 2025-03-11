from __future__ import annotations
from enum import StrEnum


class VirtualEventAttendeeRegistrationStatus(StrEnum):
	registered = "registered"
	canceled = "canceled"
	waitlisted = "waitlisted"
	pendingApproval = "pendingApproval"
	rejectedByOrganizer = "rejectedByOrganizer"
	unknownFutureValue = "unknownFutureValue"

