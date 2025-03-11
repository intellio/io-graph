from __future__ import annotations
from enum import StrEnum


class AwsRoleType(StrEnum):
	system = "system"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

