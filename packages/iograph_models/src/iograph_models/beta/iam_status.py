from __future__ import annotations
from enum import StrEnum


class IamStatus(StrEnum):
	active = "active"
	inactive = "inactive"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"

