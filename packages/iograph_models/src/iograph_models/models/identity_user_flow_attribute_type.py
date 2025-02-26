from __future__ import annotations
from enum import Enum


class IdentityUserFlowAttributeType(Enum):
	builtIn = "builtIn"
	custom = "custom"
	required = "required"
	unknownFutureValue = "unknownFutureValue"

