from __future__ import annotations
from enum import StrEnum


class DeviceManagementOperatorType(StrEnum):
	greaterOrEqual = "greaterOrEqual"
	equal = "equal"
	greater = "greater"
	less = "less"
	lessOrEqual = "lessOrEqual"
	notEqual = "notEqual"
	unknownFutureValue = "unknownFutureValue"

