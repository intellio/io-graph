from __future__ import annotations
from enum import Enum


class ApprovalFilterByCurrentUserOptions(Enum):
	target = "target"
	createdBy = "createdBy"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

