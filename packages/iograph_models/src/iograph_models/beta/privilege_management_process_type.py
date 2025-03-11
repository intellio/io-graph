from __future__ import annotations
from enum import StrEnum


class PrivilegeManagementProcessType(StrEnum):
	undefined = "undefined"
	parent = "parent"
	child = "child"
	unknownFutureValue = "unknownFutureValue"

