from __future__ import annotations
from enum import Enum


class SecurityExportFileStructure(Enum):
	none = "none"
	directory = "directory"
	pst = "pst"
	unknownFutureValue = "unknownFutureValue"

