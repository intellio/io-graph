from __future__ import annotations
from enum import StrEnum


class DeviceIdentityAttestationStatus(StrEnum):
	unknown = "unknown"
	trusted = "trusted"
	unTrusted = "unTrusted"
	notSupported = "notSupported"
	incompleteData = "incompleteData"
	unknownFutureValue = "unknownFutureValue"

