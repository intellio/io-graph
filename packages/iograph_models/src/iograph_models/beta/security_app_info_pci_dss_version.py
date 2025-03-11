from __future__ import annotations
from enum import StrEnum


class SecurityAppInfoPciDssVersion(StrEnum):
	v1 = "v1"
	v2 = "v2"
	v3 = "v3"
	v3_1 = "v3_1"
	v3_2 = "v3_2"
	v3_2_1 = "v3_2_1"
	notSupported = "notSupported"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"
	v4 = "v4"

