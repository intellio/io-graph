from __future__ import annotations
from enum import StrEnum


class IdentityGovernanceWorkflowTriggerTimeBasedAttribute(StrEnum):
	employeeHireDate = "employeeHireDate"
	employeeLeaveDateTime = "employeeLeaveDateTime"
	unknownFutureValue = "unknownFutureValue"
	createdDateTime = "createdDateTime"

