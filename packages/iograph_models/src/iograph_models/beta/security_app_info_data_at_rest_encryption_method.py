from __future__ import annotations
from enum import StrEnum


class SecurityAppInfoDataAtRestEncryptionMethod(StrEnum):
	aes = "aes"
	bitLocker = "bitLocker"
	blowfish = "blowfish"
	des3 = "des3"
	des = "des"
	rc4 = "rc4"
	rsA = "rsA"
	notSupported = "notSupported"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"

