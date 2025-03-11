from __future__ import annotations
from enum import StrEnum


class WindowsAutopilotDeviceRemediationState(StrEnum):
	unknown = "unknown"
	noRemediationRequired = "noRemediationRequired"
	automaticRemediationRequired = "automaticRemediationRequired"
	manualRemediationRequired = "manualRemediationRequired"
	unknownFutureValue = "unknownFutureValue"

