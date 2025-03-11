from __future__ import annotations
from enum import StrEnum


class DeviceManagementAlertStatusType(StrEnum):
	active = "active"
	resolved = "resolved"
	unknownFutureValue = "unknownFutureValue"

