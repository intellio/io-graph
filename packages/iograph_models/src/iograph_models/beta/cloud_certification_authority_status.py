from __future__ import annotations
from enum import StrEnum


class CloudCertificationAuthorityStatus(StrEnum):
	unknown = "unknown"
	active = "active"
	paused = "paused"
	revoked = "revoked"
	signingPending = "signingPending"
	unknownFutureValue = "unknownFutureValue"

