from __future__ import annotations
from enum import StrEnum


class RoleEligibilityScheduleRequestFilterByCurrentUserOptions(StrEnum):
	principal = "principal"
	createdBy = "createdBy"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

