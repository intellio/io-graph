from __future__ import annotations
from enum import Enum


class RoleEligibilityScheduleRequestFilterByCurrentUserOptions(Enum):
	principal = "principal"
	createdBy = "createdBy"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

