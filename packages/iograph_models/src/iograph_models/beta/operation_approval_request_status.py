from __future__ import annotations
from enum import StrEnum


class OperationApprovalRequestStatus(StrEnum):
	unknown = "unknown"
	needsApproval = "needsApproval"
	approved = "approved"
	rejected = "rejected"
	cancelled = "cancelled"
	completed = "completed"
	expired = "expired"
	unknownFutureValue = "unknownFutureValue"

