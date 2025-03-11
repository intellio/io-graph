from __future__ import annotations
from enum import StrEnum


class CloudCertificationAuthorityLeafCertificateStatus(StrEnum):
	unknown = "unknown"
	active = "active"
	revoked = "revoked"
	expired = "expired"
	unknownFutureValue = "unknownFutureValue"

