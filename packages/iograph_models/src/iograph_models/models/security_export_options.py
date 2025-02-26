from __future__ import annotations
from enum import Enum


class SecurityExportOptions(Enum):
	originalFiles = "originalFiles"
	text = "text"
	pdfReplacement = "pdfReplacement"
	tags = "tags"
	unknownFutureValue = "unknownFutureValue"

