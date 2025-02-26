from __future__ import annotations
from enum import Enum


class AccessReviewHistoryStatus(Enum):
	done = "done"
	inprogress = "inprogress"
	error = "error"
	requested = "requested"
	unknownFutureValue = "unknownFutureValue"

