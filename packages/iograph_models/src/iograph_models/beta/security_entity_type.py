from __future__ import annotations
from enum import StrEnum


class SecurityEntityType(StrEnum):
	userName = "userName"
	ipAddress = "ipAddress"
	machineName = "machineName"
	other = "other"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"

