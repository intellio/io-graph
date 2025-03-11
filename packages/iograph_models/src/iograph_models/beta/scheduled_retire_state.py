from __future__ import annotations
from enum import StrEnum


class ScheduledRetireState(StrEnum):
	cancelRetire = "cancelRetire"
	confirmRetire = "confirmRetire"
	unknownFutureValue = "unknownFutureValue"

