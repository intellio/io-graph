from __future__ import annotations
from enum import Enum


class IdentityGovernanceWorkflowExecutionType(Enum):
	scheduled = "scheduled"
	onDemand = "onDemand"
	unknownFutureValue = "unknownFutureValue"

