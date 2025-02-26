from __future__ import annotations
from enum import Enum


class DeviceEnrollmentFailureReason(Enum):
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

