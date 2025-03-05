from __future__ import annotations
from enum import StrEnum


class RoleAssignmentScheduleRequestFilterByCurrentUserOptions(StrEnum):
	principal = "principal"
	createdBy = "createdBy"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

