from __future__ import annotations
from enum import Enum


class DelegatedAdminRelationshipRequestAction(Enum):
	lockForApproval = "lockForApproval"
	approve = "approve"
	terminate = "terminate"
	unknownFutureValue = "unknownFutureValue"
	reject = "reject"

