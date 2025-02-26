from __future__ import annotations
from enum import Enum


class AccessPackageAssignmentRequestFilterByCurrentUserOptions(Enum):
	target = "target"
	createdBy = "createdBy"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

