from __future__ import annotations
from enum import Enum


class DelegatedAdminRelationshipStatus(Enum):
	activating = "activating"
	active = "active"
	approvalPending = "approvalPending"
	approved = "approved"
	created = "created"
	expired = "expired"
	expiring = "expiring"
	terminated = "terminated"
	terminating = "terminating"
	terminationRequested = "terminationRequested"
	unknownFutureValue = "unknownFutureValue"

