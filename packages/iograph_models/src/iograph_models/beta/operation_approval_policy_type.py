from __future__ import annotations
from enum import StrEnum


class OperationApprovalPolicyType(StrEnum):
	unknown = "unknown"
	app = "app"
	script = "script"
	unknownFutureValue = "unknownFutureValue"

