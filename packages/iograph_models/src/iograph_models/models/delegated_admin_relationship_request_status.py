from __future__ import annotations
from enum import Enum


class DelegatedAdminRelationshipRequestStatus(Enum):
	created = "created"
	pending = "pending"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

