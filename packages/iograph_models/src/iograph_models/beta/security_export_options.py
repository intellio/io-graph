from __future__ import annotations
from enum import StrEnum


class SecurityExportOptions(StrEnum):
	originalFiles = "originalFiles"
	text = "text"
	pdfReplacement = "pdfReplacement"
	fileInfo = "fileInfo"
	tags = "tags"
	unknownFutureValue = "unknownFutureValue"
	splitSource = "splitSource"
	includeFolderAndPath = "includeFolderAndPath"
	friendlyName = "friendlyName"
	condensePaths = "condensePaths"
	optimizedPartitionSize = "optimizedPartitionSize"

