from __future__ import annotations
from enum import StrEnum


class PrivilegeManagementElevationType(StrEnum):
	undetermined = "undetermined"
	unmanagedElevation = "unmanagedElevation"
	zeroTouchElevation = "zeroTouchElevation"
	userConfirmedElevation = "userConfirmedElevation"
	supportApprovedElevation = "supportApprovedElevation"
	unknownFutureValue = "unknownFutureValue"

