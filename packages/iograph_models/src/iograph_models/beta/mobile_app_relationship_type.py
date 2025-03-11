from __future__ import annotations
from enum import StrEnum


class MobileAppRelationshipType(StrEnum):
	child = "child"
	parent = "parent"
	unknownFutureValue = "unknownFutureValue"

