from __future__ import annotations
from enum import StrEnum


class DeviceEnrollmentFailureReason(StrEnum):
	unknown = "unknown"
	authentication = "authentication"
	authorization = "authorization"
	accountValidation = "accountValidation"
	userValidation = "userValidation"
	deviceNotSupported = "deviceNotSupported"
	inMaintenance = "inMaintenance"
	badRequest = "badRequest"
	featureNotSupported = "featureNotSupported"
	enrollmentRestrictionsEnforced = "enrollmentRestrictionsEnforced"
	clientDisconnected = "clientDisconnected"
	userAbandonment = "userAbandonment"

