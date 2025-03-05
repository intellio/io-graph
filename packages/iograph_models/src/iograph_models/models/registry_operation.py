from __future__ import annotations
from enum import StrEnum


class RegistryOperation(StrEnum):
	unknown = "unknown"
	create = "create"
	modify = "modify"
	delete = "delete"
	unknownFutureValue = "unknownFutureValue"

