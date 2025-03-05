from __future__ import annotations
from enum import StrEnum


class PrivilegedAccessGroupAssignmentType(StrEnum):
	assigned = "assigned"
	activated = "activated"
	unknownFutureValue = "unknownFutureValue"

