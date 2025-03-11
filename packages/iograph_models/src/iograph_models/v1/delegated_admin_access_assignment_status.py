from __future__ import annotations
from enum import StrEnum


class DelegatedAdminAccessAssignmentStatus(StrEnum):
	pending = "pending"
	active = "active"
	deleting = "deleting"
	deleted = "deleted"
	error = "error"
	unknownFutureValue = "unknownFutureValue"

