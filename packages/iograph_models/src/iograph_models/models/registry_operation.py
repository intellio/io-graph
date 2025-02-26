from __future__ import annotations
from enum import Enum


class RegistryOperation(Enum):
	unknown = "unknown"
	create = "create"
	modify = "modify"
	delete = "delete"
	unknownFutureValue = "unknownFutureValue"

