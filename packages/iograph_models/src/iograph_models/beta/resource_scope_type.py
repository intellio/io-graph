from __future__ import annotations
from enum import StrEnum


class ResourceScopeType(StrEnum):
	group = "group"
	chat = "chat"
	tenant = "tenant"
	unknownFutureValue = "unknownFutureValue"
	team = "team"

