from __future__ import annotations
from enum import StrEnum


class ApprovalState(StrEnum):
	pending = "pending"
	approved = "approved"
	denied = "denied"
	aborted = "aborted"
	canceled = "canceled"

