from __future__ import annotations
from enum import StrEnum


class GroupType(StrEnum):
	unifiedGroups = "unifiedGroups"
	azureAD = "azureAD"
	unknownFutureValue = "unknownFutureValue"

