from __future__ import annotations
from enum import StrEnum


class AuthorizationSystemActionType(StrEnum):
	delete = "delete"
	read = "read"
	unknownFutureValue = "unknownFutureValue"

