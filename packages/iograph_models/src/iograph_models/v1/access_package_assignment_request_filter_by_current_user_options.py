from __future__ import annotations
from enum import StrEnum


class AccessPackageAssignmentRequestFilterByCurrentUserOptions(StrEnum):
	target = "target"
	createdBy = "createdBy"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

