from __future__ import annotations
from enum import StrEnum


class SecurityVerdictCategory(StrEnum):
	none = "none"
	malware = "malware"
	phish = "phish"
	siteUnavailable = "siteUnavailable"
	spam = "spam"
	decryptionFailed = "decryptionFailed"
	unsupportedUriScheme = "unsupportedUriScheme"
	unsupportedFileType = "unsupportedFileType"
	undefined = "undefined"
	unknownFutureValue = "unknownFutureValue"

