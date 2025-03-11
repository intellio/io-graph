from __future__ import annotations
from enum import StrEnum


class AppleUserInitiatedEnrollmentType(StrEnum):
	unknown = "unknown"
	device = "device"
	user = "user"
	accountDrivenUserEnrollment = "accountDrivenUserEnrollment"
	webDeviceEnrollment = "webDeviceEnrollment"
	unknownFutureValue = "unknownFutureValue"

