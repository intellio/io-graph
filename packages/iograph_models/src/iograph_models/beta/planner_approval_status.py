from __future__ import annotations
from enum import StrEnum


class PlannerApprovalStatus(StrEnum):
	requested = "requested"
	approved = "approved"
	rejected = "rejected"
	cancelled = "cancelled"
	unknownFutureValue = "unknownFutureValue"

