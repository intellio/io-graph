from __future__ import annotations
from enum import StrEnum


class TeamsAppResourceSpecificPermissionType(StrEnum):
	delegated = "delegated"
	application = "application"
	unknownFutureValue = "unknownFutureValue"

