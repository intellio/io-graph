from __future__ import annotations
from enum import Enum


class ScheduleChangeState(Enum):
	pending = "pending"
	approved = "approved"
	declined = "declined"
	unknownFutureValue = "unknownFutureValue"

