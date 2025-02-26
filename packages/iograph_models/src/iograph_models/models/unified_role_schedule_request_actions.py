from __future__ import annotations
from enum import Enum


class UnifiedRoleScheduleRequestActions(Enum):
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

