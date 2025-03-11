from __future__ import annotations
from enum import StrEnum


class PrivilegedAccessGroupRelationships(StrEnum):
	owner = "owner"
	member = "member"
	unknownFutureValue = "unknownFutureValue"

