from __future__ import annotations
from enum import StrEnum


class SecurityAppInfoUploadedDataTypes(StrEnum):
	documents = "documents"
	mediaFiles = "mediaFiles"
	codingFiles = "codingFiles"
	creditCards = "creditCards"
	databaseFiles = "databaseFiles"
	none = "none"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"

