from __future__ import annotations
from enum import StrEnum


class EligibilityScheduleRequestFilterByCurrentUserOptions(StrEnum):
	principal = "principal"
	createdBy = "createdBy"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

