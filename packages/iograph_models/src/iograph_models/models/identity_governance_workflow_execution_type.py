from __future__ import annotations
from enum import StrEnum


class IdentityGovernanceWorkflowExecutionType(StrEnum):
	scheduled = "scheduled"
	onDemand = "onDemand"
	unknownFutureValue = "unknownFutureValue"

