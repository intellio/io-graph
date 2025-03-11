from __future__ import annotations
from enum import StrEnum


class MembershipRuleProcessingStatusDetails(StrEnum):
	NotStarted = "NotStarted"
	Running = "Running"
	Failed = "Failed"
	Succeeded = "Succeeded"
	UnsupportedFutureValue = "UnsupportedFutureValue"

