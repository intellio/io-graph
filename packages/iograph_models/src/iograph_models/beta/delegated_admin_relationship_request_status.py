from __future__ import annotations
from enum import StrEnum


class DelegatedAdminRelationshipRequestStatus(StrEnum):
	created = "created"
	pending = "pending"
	succeeded = "succeeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

