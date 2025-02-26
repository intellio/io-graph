from __future__ import annotations
from enum import Enum


class PrivilegedAccessGroupMemberType(Enum):
	direct = "direct"
	group = "group"
	unknownFutureValue = "unknownFutureValue"

