from __future__ import annotations
from enum import StrEnum


class DeviceManagementScriptRunState(StrEnum):
	unknown = "unknown"
	success = "success"
	fail = "fail"
	scriptError = "scriptError"
	pending = "pending"
	notApplicable = "notApplicable"
	unknownFutureValue = "unknownFutureValue"

