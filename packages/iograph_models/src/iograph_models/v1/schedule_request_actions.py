from __future__ import annotations
from enum import StrEnum


class ScheduleRequestActions(StrEnum):
	adminAssign = "adminAssign"
	adminUpdate = "adminUpdate"
	adminRemove = "adminRemove"
	selfActivate = "selfActivate"
	selfDeactivate = "selfDeactivate"
	adminExtend = "adminExtend"
	adminRenew = "adminRenew"
	selfExtend = "selfExtend"
	selfRenew = "selfRenew"
	unknownFutureValue = "unknownFutureValue"

