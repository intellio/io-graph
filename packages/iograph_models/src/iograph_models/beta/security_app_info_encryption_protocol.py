from __future__ import annotations
from enum import StrEnum


class SecurityAppInfoEncryptionProtocol(StrEnum):
	tls1_0 = "tls1_0"
	tls1_1 = "tls1_1"
	tls1_2 = "tls1_2"
	tls1_3 = "tls1_3"
	notApplicable = "notApplicable"
	notSupported = "notSupported"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"
	ssl3 = "ssl3"

