from __future__ import annotations
from enum import Enum


class EligibilityScheduleRequestFilterByCurrentUserOptions(Enum):
	principal = "principal"
	createdBy = "createdBy"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

