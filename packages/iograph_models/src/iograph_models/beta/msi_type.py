from __future__ import annotations
from enum import StrEnum


class MsiType(StrEnum):
	none = "none"
	userAssigned = "userAssigned"
	systemAssigned = "systemAssigned"
	unknownFutureValue = "unknownFutureValue"

