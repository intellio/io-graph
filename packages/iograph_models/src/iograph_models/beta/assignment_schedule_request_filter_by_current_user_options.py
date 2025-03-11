from __future__ import annotations
from enum import StrEnum


class AssignmentScheduleRequestFilterByCurrentUserOptions(StrEnum):
	principal = "principal"
	createdBy = "createdBy"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

