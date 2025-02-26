from __future__ import annotations
from enum import Enum


class PrivilegedAccessGroupRelationships(Enum):
	owner = "owner"
	member = "member"
	unknownFutureValue = "unknownFutureValue"

