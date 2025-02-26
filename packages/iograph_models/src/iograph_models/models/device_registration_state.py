from __future__ import annotations
from enum import Enum


class DeviceRegistrationState(Enum):
	notRegistered = "notRegistered"
	registered = "registered"
	revoked = "revoked"
	keyConflict = "keyConflict"
	approvalPending = "approvalPending"
	certificateReset = "certificateReset"
	notRegisteredPendingEnrollment = "notRegisteredPendingEnrollment"
	unknown = "unknown"

