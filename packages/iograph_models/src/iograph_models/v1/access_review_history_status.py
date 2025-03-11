from __future__ import annotations
from enum import StrEnum


class AccessReviewHistoryStatus(StrEnum):
	done = "done"
	inprogress = "inprogress"
	error = "error"
	requested = "requested"
	unknownFutureValue = "unknownFutureValue"

