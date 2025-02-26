from __future__ import annotations
from enum import Enum


class AppManagementRestrictionState(Enum):
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"

