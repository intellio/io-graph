from __future__ import annotations
from enum import StrEnum


class NonAdminSetting(StrEnum):
	false = "false"
	true = "true"
	unknownFutureValue = "unknownFutureValue"

