from __future__ import annotations
from enum import StrEnum


class ScheduledPermissionsRequestFilterByCurrentUserOptions(StrEnum):
	principal = "principal"
	createdBy = "createdBy"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

