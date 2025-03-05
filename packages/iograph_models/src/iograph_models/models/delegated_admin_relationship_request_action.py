from __future__ import annotations
from enum import StrEnum


class DelegatedAdminRelationshipRequestAction(StrEnum):
	lockForApproval = "lockForApproval"
	approve = "approve"
	terminate = "terminate"
	unknownFutureValue = "unknownFutureValue"
	reject = "reject"

