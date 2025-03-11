from __future__ import annotations
from enum import StrEnum


class EdiscoveryExportFileStructure(StrEnum):
	none = "none"
	directory = "directory"
	pst = "pst"
	unknownFutureValue = "unknownFutureValue"

