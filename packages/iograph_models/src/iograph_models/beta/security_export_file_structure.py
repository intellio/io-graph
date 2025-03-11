from __future__ import annotations
from enum import StrEnum


class SecurityExportFileStructure(StrEnum):
	none = "none"
	directory = "directory"
	pst = "pst"
	unknownFutureValue = "unknownFutureValue"
	msg = "msg"

