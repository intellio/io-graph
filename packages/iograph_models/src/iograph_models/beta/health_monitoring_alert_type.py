from __future__ import annotations
from enum import StrEnum


class HealthMonitoringAlertType(StrEnum):
	unknown = "unknown"
	mfaSignInFailure = "mfaSignInFailure"
	managedDeviceSignInFailure = "managedDeviceSignInFailure"
	compliantDeviceSignInFailure = "compliantDeviceSignInFailure"
	unknownFutureValue = "unknownFutureValue"

