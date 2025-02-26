from __future__ import annotations
from enum import Enum


class DelegatedAdminAccessAssignmentStatus(Enum):
	pending = "pending"
	active = "active"
	deleting = "deleting"
	deleted = "deleted"
	error = "error"
	unknownFutureValue = "unknownFutureValue"

