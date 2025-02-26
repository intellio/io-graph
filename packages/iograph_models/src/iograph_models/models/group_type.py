from __future__ import annotations
from enum import Enum


class GroupType(Enum):
	unifiedGroups = "unifiedGroups"
	azureAD = "azureAD"
	unknownFutureValue = "unknownFutureValue"

