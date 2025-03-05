from __future__ import annotations
from enum import StrEnum


class SecurityExportOptions(StrEnum):
	originalFiles = "originalFiles"
	text = "text"
	pdfReplacement = "pdfReplacement"
	tags = "tags"
	unknownFutureValue = "unknownFutureValue"

