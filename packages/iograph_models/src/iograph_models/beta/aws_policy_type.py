from __future__ import annotations
from enum import StrEnum


class AwsPolicyType(StrEnum):
	system = "system"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

