from __future__ import annotations
from enum import Enum


class AssignmentScheduleRequestFilterByCurrentUserOptions(Enum):
	principal = "principal"
	createdBy = "createdBy"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

