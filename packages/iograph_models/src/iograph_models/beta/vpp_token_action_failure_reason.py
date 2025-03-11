from __future__ import annotations
from enum import StrEnum


class VppTokenActionFailureReason(StrEnum):
	none = "none"
	appleFailure = "appleFailure"
	internalError = "internalError"
	expiredVppToken = "expiredVppToken"
	expiredApplePushNotificationCertificate = "expiredApplePushNotificationCertificate"

