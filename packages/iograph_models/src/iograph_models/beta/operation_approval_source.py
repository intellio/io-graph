from __future__ import annotations
from enum import StrEnum


class OperationApprovalSource(StrEnum):
	unknown = "unknown"
	adminConsole = "adminConsole"
	email = "email"
	unknownFutureValue = "unknownFutureValue"

