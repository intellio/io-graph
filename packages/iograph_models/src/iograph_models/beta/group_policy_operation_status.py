from __future__ import annotations
from enum import StrEnum


class GroupPolicyOperationStatus(StrEnum):
	unknown = "unknown"
	inProgress = "inProgress"
	success = "success"
	failed = "failed"

