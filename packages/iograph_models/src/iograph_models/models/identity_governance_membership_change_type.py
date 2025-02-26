from __future__ import annotations
from enum import Enum


class IdentityGovernanceMembershipChangeType(Enum):
	add = "add"
	remove = "remove"
	unknownFutureValue = "unknownFutureValue"

