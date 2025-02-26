from __future__ import annotations
from enum import Enum


class TeamsAppResourceSpecificPermissionType(Enum):
	delegated = "delegated"
	application = "application"
	unknownFutureValue = "unknownFutureValue"

