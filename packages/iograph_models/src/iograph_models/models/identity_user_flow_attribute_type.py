from __future__ import annotations
from enum import StrEnum


class IdentityUserFlowAttributeType(StrEnum):
	builtIn = "builtIn"
	custom = "custom"
	required = "required"
	unknownFutureValue = "unknownFutureValue"

