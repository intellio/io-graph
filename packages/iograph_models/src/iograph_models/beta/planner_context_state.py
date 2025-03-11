from __future__ import annotations
from enum import StrEnum


class PlannerContextState(StrEnum):
	active = "active"
	delinked = "delinked"
	unknownFutureValue = "unknownFutureValue"

