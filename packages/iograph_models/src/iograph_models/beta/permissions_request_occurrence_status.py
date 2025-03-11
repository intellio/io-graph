from __future__ import annotations
from enum import StrEnum


class PermissionsRequestOccurrenceStatus(StrEnum):
	grantingFailed = "grantingFailed"
	granted = "granted"
	granting = "granting"
	revoked = "revoked"
	revoking = "revoking"
	revokingFailed = "revokingFailed"
	unknownFutureValue = "unknownFutureValue"

