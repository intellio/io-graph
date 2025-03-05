from __future__ import annotations
from enum import StrEnum


class ScheduleChangeState(StrEnum):
	pending = "pending"
	approved = "approved"
	declined = "declined"
	unknownFutureValue = "unknownFutureValue"

