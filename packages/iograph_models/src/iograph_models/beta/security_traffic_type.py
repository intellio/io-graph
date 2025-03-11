from __future__ import annotations
from enum import StrEnum


class SecurityTrafficType(StrEnum):
	downloadedBytes = "downloadedBytes"
	uploadedBytes = "uploadedBytes"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"

