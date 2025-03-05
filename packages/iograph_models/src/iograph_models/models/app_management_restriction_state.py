from __future__ import annotations
from enum import StrEnum


class AppManagementRestrictionState(StrEnum):
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"

