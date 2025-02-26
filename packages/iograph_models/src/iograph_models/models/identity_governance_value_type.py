from __future__ import annotations
from enum import Enum


class IdentityGovernanceValueType(Enum):
	enum = "enum"
	string = "string"
	int = "int"
	bool = "bool"
	unknownFutureValue = "unknownFutureValue"

