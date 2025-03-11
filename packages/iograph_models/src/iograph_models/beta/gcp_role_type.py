from __future__ import annotations
from enum import StrEnum


class GcpRoleType(StrEnum):
	system = "system"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

