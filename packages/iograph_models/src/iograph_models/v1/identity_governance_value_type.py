from __future__ import annotations
from enum import StrEnum


class IdentityGovernanceValueType(StrEnum):
	enum = "enum"
	string = "string"
	int = "int"
	bool = "bool"
	unknownFutureValue = "unknownFutureValue"

