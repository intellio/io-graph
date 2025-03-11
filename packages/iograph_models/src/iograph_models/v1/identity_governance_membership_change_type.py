from __future__ import annotations
from enum import StrEnum


class IdentityGovernanceMembershipChangeType(StrEnum):
	add = "add"
	remove = "remove"
	unknownFutureValue = "unknownFutureValue"

