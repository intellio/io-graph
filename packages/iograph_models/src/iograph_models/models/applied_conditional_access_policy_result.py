from __future__ import annotations
from enum import StrEnum


class AppliedConditionalAccessPolicyResult(StrEnum):
	success = "success"
	failure = "failure"
	notApplied = "notApplied"
	notEnabled = "notEnabled"
	unknown = "unknown"
	unknownFutureValue = "unknownFutureValue"
	reportOnlySuccess = "reportOnlySuccess"
	reportOnlyFailure = "reportOnlyFailure"
	reportOnlyNotApplied = "reportOnlyNotApplied"
	reportOnlyInterrupted = "reportOnlyInterrupted"

