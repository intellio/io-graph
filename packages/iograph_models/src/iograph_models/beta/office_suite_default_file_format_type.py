from __future__ import annotations
from enum import StrEnum


class OfficeSuiteDefaultFileFormatType(StrEnum):
	notConfigured = "notConfigured"
	officeOpenXMLFormat = "officeOpenXMLFormat"
	officeOpenDocumentFormat = "officeOpenDocumentFormat"
	unknownFutureValue = "unknownFutureValue"

