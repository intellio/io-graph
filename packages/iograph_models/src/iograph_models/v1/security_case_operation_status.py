from __future__ import annotations
from enum import StrEnum


class SecurityCaseOperationStatus(StrEnum):
	notStarted = "notStarted"
	submissionFailed = "submissionFailed"
	running = "running"
	succeeded = "succeeded"
	partiallySucceeded = "partiallySucceeded"
	failed = "failed"
	unknownFutureValue = "unknownFutureValue"

