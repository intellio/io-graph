from __future__ import annotations
from enum import StrEnum


class AzureRoleDefinitionType(StrEnum):
	system = "system"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

