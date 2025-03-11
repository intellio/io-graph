from __future__ import annotations
from enum import StrEnum


class EdiscoveryCaseOperationStatus(StrEnum):
	notStarted = "notStarted"
	submissionFailed = "submissionFailed"
	running = "running"
	succeeded = "succeeded"
	partiallySucceeded = "partiallySucceeded"
	failed = "failed"

