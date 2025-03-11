from __future__ import annotations
from enum import StrEnum


class StatusDetail(StrEnum):
	submitted = "submitted"
	approved = "approved"
	completed = "completed"
	canceled = "canceled"
	rejected = "rejected"
	unknownFutureValue = "unknownFutureValue"

