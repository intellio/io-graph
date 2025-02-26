from __future__ import annotations
from enum import Enum


class IdentityGovernanceWorkflowTriggerTimeBasedAttribute(Enum):
	employeeHireDate = "employeeHireDate"
	employeeLeaveDateTime = "employeeLeaveDateTime"
	unknownFutureValue = "unknownFutureValue"
	createdDateTime = "createdDateTime"

