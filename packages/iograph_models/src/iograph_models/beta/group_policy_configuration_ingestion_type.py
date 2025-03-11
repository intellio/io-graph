from __future__ import annotations
from enum import StrEnum


class GroupPolicyConfigurationIngestionType(StrEnum):
	unknown = "unknown"
	custom = "custom"
	builtIn = "builtIn"
	mixed = "mixed"
	unknownFutureValue = "unknownFutureValue"

