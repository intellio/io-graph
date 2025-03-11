from __future__ import annotations
from enum import StrEnum


class DeviceRegistrationState(StrEnum):
	notRegistered = "notRegistered"
	registered = "registered"
	revoked = "revoked"
	keyConflict = "keyConflict"
	approvalPending = "approvalPending"
	certificateReset = "certificateReset"
	notRegisteredPendingEnrollment = "notRegisteredPendingEnrollment"
	unknown = "unknown"

