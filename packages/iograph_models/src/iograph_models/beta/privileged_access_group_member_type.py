from __future__ import annotations
from enum import StrEnum


class PrivilegedAccessGroupMemberType(StrEnum):
	direct = "direct"
	group = "group"
	unknownFutureValue = "unknownFutureValue"

