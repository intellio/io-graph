from __future__ import annotations
from enum import StrEnum


class ApprovalOperationStatus(StrEnum):
	scheduled = "scheduled"
	inProgress = "inProgress"
	succeeded = "succeeded"
	failed = "failed"
	timeout = "timeout"
	unknownFutureValue = "unknownFutureValue"

