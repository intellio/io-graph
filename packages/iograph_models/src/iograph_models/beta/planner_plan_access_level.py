from __future__ import annotations
from enum import StrEnum


class PlannerPlanAccessLevel(StrEnum):
	readAccess = "readAccess"
	readWriteAccess = "readWriteAccess"
	fullAccess = "fullAccess"
	unknownFutureValue = "unknownFutureValue"

