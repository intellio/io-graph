from __future__ import annotations
from enum import StrEnum


class EdiscoveryExportOptions(StrEnum):
	originalFiles = "originalFiles"
	text = "text"
	pdfReplacement = "pdfReplacement"
	fileInfo = "fileInfo"
	tags = "tags"
	unknownFutureValue = "unknownFutureValue"

