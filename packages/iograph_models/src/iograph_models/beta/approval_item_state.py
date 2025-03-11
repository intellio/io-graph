from __future__ import annotations
from enum import StrEnum


class ApprovalItemState(StrEnum):
	canceled = "canceled"
	created = "created"
	pending = "pending"
	completed = "completed"
	unknownFutureValue = "unknownFutureValue"

